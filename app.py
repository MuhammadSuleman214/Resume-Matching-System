from dotenv import load_dotenv

load_dotenv()

import base64
import streamlit as st
import os
import io
import shutil
from PIL import Image
import pdf2image
import pytesseract
import fitz  # PyMuPDF for extracting text directly
from groq import Groq

# ---------------- Configure Tesseract Path ----------------
# Windows ke liye hardcoded path, Linux ke liye auto-detect
pytesseract.pytesseract.tesseract_cmd = (
    shutil.which("tesseract") or r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# ---------------- Configure Groq AI ----------------
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.error("⚠️ Groq API key not found! Please create a .env file with your GROQ_API_KEY")
    st.stop()
else:
    client = Groq(api_key=api_key)


# ---------------- Groq Response Function ----------------
def get_groq_response(input_text, pdf_content, prompt):
    try:
        # Extracted resume text
        resume_text = pdf_content.get("extracted_text", "")

        full_prompt = f"""
        {prompt}

        Job Description: {input_text}

        Resume Text (extracted from PDF):
        {resume_text}

        Please analyze the resume text against the job description and provide your response.
        """

        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {"role": "system",
                 "content": "You are an experienced Technical Human Resource Manager and ATS expert."},
                {"role": "user", "content": full_prompt}
            ],
            temperature=0.1,
            max_tokens=1024
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"❌ Error calling Groq AI: {str(e)}")
        return "Sorry, there was an error processing your request."


# ---------------- Hybrid PDF Extraction ----------------
def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        try:
            # Save uploaded file temporarily
            temp_path = "temp_resume.pdf"
            with open(temp_path, "wb") as f:
                f.write(uploaded_file.read())

            # Step 1: Try direct text extraction
            extracted_text = ""
            with fitz.open(temp_path) as doc:
                for page in doc:
                    extracted_text += page.get_text()

            # Step 2: If direct extraction fails, fallback to OCR
            if not extracted_text.strip():
                st.info("📄 No direct text found, using OCR...")

                # Poppler path (Linux mai zarurat nahi, Windows ke liye rakhna hoga)
                poppler_path = None
                if os.name == "nt":  # Windows
                    poppler_path = r"C:\games\ML\poppler-25.07.0\Library\bin"

                images = pdf2image.convert_from_path(temp_path, poppler_path=poppler_path)
                first_page = images[0]
                extracted_text = pytesseract.image_to_string(first_page)

                # Convert first page to bytes (for preview)
                img_byte_arr = io.BytesIO()
                first_page.save(img_byte_arr, format='JPEG')
                img_byte_arr = img_byte_arr.getvalue()
                image_data = base64.b64encode(img_byte_arr).decode()
            else:
                # For preview, create blank image placeholder
                image_data = None

            pdf_parts = {
                "extracted_text": extracted_text,
                "image_data": image_data
            }
            return pdf_parts
        except Exception as e:
            st.error(f"❌ Error processing PDF: {str(e)}")
            return None
    else:
        raise FileNotFoundError("No file uploaded")


# ---------------- Streamlit App ----------------
st.set_page_config(page_title="Resume Matching System")
st.header("Resume Matching System")


# Function to convert image file to base64
def get_base64_image(image_file):
    with open(image_file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


# Convert logo.png into base64 string
logo_base64 = get_base64_image("logo.png")  # make sure logo.png is in same folder as app.py

# Inject header with logo + text
st.markdown(
    f"""
    <style>
    .custom-header {{
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: black;
        color: white;
        padding: 10px 20px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 18px;
        font-weight: bold;
        z-index: 9999;
    }}

    .custom-header .left {{
        display: flex;
        align-items: center;
        gap: 10px;
    }}

    .custom-header img {{
        height: 35px;  /* adjust logo size */
    }}

    [data-testid="stAppViewContainer"] {{
        margin-top: 60px;
    }}
    </style>

    <div class="custom-header">
        <div class="left">
            <img src="data:image/png;base64,{logo_base64}" alt="Logo">
            <span>Section Soft</span>
        </div>
        <div>Developed by Muhammad Suleman</div>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------- UI Inputs ----------------
input_text = st.text_area("Job Description: ", key="input")
uploaded_file = st.file_uploader("Upload your resume (PDF)...", type=["pdf"])

if uploaded_file is not None:
    st.write("✅ PDF Uploaded Successfully")

    # Show extracted text
    pdf_content = input_pdf_setup(uploaded_file)
    if pdf_content is not None:
        with st.expander("📄 Extracted Resume Text (Preview)"):
            st.text_area("Resume Text:", pdf_content.get("extracted_text", ""), height=200)

# ---------------- Buttons ----------------
submit1 = st.button("Tell Me About the Resume")
submit3 = st.button("Percentage Match")

input_prompt1 = """
You are an experienced Technical Human Resource Manager. 
Review the provided resume against the job description. 
Highlight strengths and weaknesses of the applicant in relation to the job.
"""

input_prompt3 = """
You are an ATS (Applicant Tracking System) scanner with deep knowledge of resume screening. 
Evaluate the resume against the provided job description. 
Return output in this format:
1. Percentage Match
2. Missing Keywords
3. Final Thoughts
"""

# ---------------- Actions ----------------
if submit1:
    if uploaded_file is not None and pdf_content is not None:
        response = get_groq_response(input_text, pdf_content, input_prompt1)
        st.subheader("Evaluation Result")
        st.write(response)
    else:
        st.warning("⚠️ Please upload the resume first")

elif submit3:
    if uploaded_file is not None and pdf_content is not None:
        response = get_groq_response(input_text, pdf_content, input_prompt3)
        st.subheader("Matching Result")
        st.write(response)
    else:
        st.warning("⚠️ Please upload the resume first")
