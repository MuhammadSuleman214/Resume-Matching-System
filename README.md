# ATS System - Resume Matching Application

## 📋 Project Overview

This is an intelligent **Applicant Tracking System (ATS)** that uses AI to analyze resumes against job descriptions. The system provides detailed feedback on resume quality, keyword matching, and compatibility with job requirements.

## 🚀 Features

- **PDF Resume Processing**: Supports both text-based and image-based PDFs
- **AI-Powered Analysis**: Uses Groq's LLaMA 3.3 70B model for intelligent analysis
- **Dual Extraction Methods**: Direct text extraction + OCR fallback for scanned PDFs
- **Interactive Web Interface**: Built with Streamlit for easy use
- **Detailed Feedback**: Provides percentage match, missing keywords, and recommendations

## 🛠️ How It Works

### Step 1: PDF Upload and Processing
1. User uploads a PDF resume through the web interface
2. System attempts direct text extraction using PyMuPDF
3. If no text found, falls back to OCR using Tesseract
4. Extracted text is stored for analysis

### Step 2: Job Description Input
1. User enters job description in the text area
2. System combines job description with extracted resume text

### Step 3: AI Analysis
1. System sends combined data to Groq AI (LLaMA 3.3 70B)
2. AI analyzes resume against job requirements
3. Returns detailed feedback including:
   - Resume strengths and weaknesses
   - Percentage match with job description
   - Missing keywords
   - Final recommendations

### Step 4: Results Display
1. System displays AI analysis results
2. User can view extracted text preview
3. Results include actionable insights for improvement

## 📦 Installation

### Prerequisites

1. **Python 3.8+** installed on your system
2. **Tesseract OCR** for text extraction from images
3. **Poppler** for PDF to image conversion
4. **Groq API Key** for AI analysis

### Step-by-Step Installation

#### 1. Clone the Repository
```bash
git clone <your-repository-url>
cd ATS-System
```

#### 2. Install Python Dependencies
```bash
pip install -r requirements.txt
```

#### 3. Install System Dependencies

**For Windows:**
```bash
# Install Tesseract OCR
# Download from: https://github.com/UB-Mannheim/tesseract/wiki
# Install to: C:\Program Files\Tesseract-OCR\

# Install Poppler
# Download from: https://github.com/oschwartz10612/poppler-windows/releases
# Extract to: C:\games\ML\poppler-25.07.0\
```

**For Linux/Ubuntu:**
```bash
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install poppler-utils
```

#### 4. Set Up Environment Variables
Create a `.env` file in the project root:
```env
GROQ_API_KEY=your_groq_api_key_here
```

#### 5. Get Groq API Key
1. Visit [Groq Console](https://console.groq.com/)
2. Sign up/Login to your account
3. Generate an API key
4. Add the key to your `.env` file

#### 6. Run the Application
```bash
streamlit run app.py
```

## 📁 Project Structure

```
ATS-System/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── packages.txt          # System dependencies
├── logo.png             # Application logo
├── temp_resume.pdf      # Temporary file for processing
├── .env                 # Environment variables (create this)
└── README.md            # This file
```

## 🔧 Technical Details

### Core Technologies

- **Streamlit**: Web application framework
- **Groq AI**: LLaMA 3.3 70B model for analysis
- **PyMuPDF**: Direct PDF text extraction
- **Tesseract OCR**: Optical Character Recognition
- **Pillow**: Image processing
- **pdf2image**: PDF to image conversion

### Key Functions

1. **`input_pdf_setup()`**: Handles PDF processing and text extraction
2. **`get_groq_response()`**: Communicates with Groq AI API
3. **`get_base64_image()`**: Converts images to base64 for web display

### AI Prompts / AI Prompts

The system uses two main prompts:

1. **Resume Analysis**: Evaluates strengths and weaknesses
2. **Percentage Match**: Calculates compatibility score with job requirements

## 🎯 Usage Instructions

### 1. Start the Application
```bash
streamlit run app.py
```

### 2. Upload Resume
- Click "Browse files" to upload a PDF resume
- Wait for "PDF Uploaded Successfully" message

### 3. Enter Job Description
- Paste the job description in the text area
- Include requirements, skills, and qualifications

### 4. Choose Analysis Type
- **"Tell Me About the Resume"**: Get detailed feedback
- **"Percentage Match"**: Get compatibility score

### 5. View Results
- Review the AI analysis
- Check extracted text in the preview section
- Use insights to improve your resume

## 🔍 Features Explained

### PDF Processing
- **Direct Extraction**: Fast text extraction from text-based PDFs
- **OCR Fallback**: Handles scanned/image-based PDFs
- **Preview**: Shows extracted text for verification

### AI Analysis
- **Smart Matching**: Compares resume with job requirements
- **Keyword Analysis**: Identifies missing important keywords
- **Scoring**: Provides percentage match for quick assessment
- **Recommendations**: Suggests improvements for better compatibility

### User Interface
- **Responsive Design**: Works on desktop and mobile
- **Real-time Processing**: Instant feedback and analysis
- **Professional Look**: Clean, modern interface with branding

## 🚨 Troubleshooting

### Common Issues

1. **"Groq API key not found"**
   - Create `.env` file with `GROQ_API_KEY=your_key`
   - Restart the application

2. **"Tesseract not found"**
   - Install Tesseract OCR
   - Update path in `app.py` if needed

3. **"Poppler not found"**
   - Install Poppler utilities
   - Update path in `app.py` for Windows

4. **PDF Processing Errors**
   - Ensure PDF is not password protected
   - Try with a different PDF file
   - Check file size (should be reasonable)

### Performance Tips

- Use text-based PDFs for faster processing
- Keep job descriptions concise but comprehensive
- Ensure good internet connection for AI analysis

## 🔒 Security Notes

- API keys are stored in `.env` file (not committed to git)
- Temporary files are cleaned up after processing
- No personal data is stored permanently

## 📈 Future Enhancements

- Support for multiple file formats (DOCX, TXT)
- Batch processing for multiple resumes
- Custom scoring criteria
- Integration with job boards
- Resume optimization suggestions

## 👨‍💻 Developer Information

**Developed by**: Muhammad Suleman  
**Company**: Section Soft  
**Version**: 1.0  
**Last Updated**: 2024

## 📞 Support

For issues, questions, or contributions:
- Create an issue in the repository
- Contact: [Your contact information]

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

**Note**: This application requires an active internet connection for AI analysis and a valid Groq API key for functionality.

## 🌐 Live Demo

**Try the application online without installation!**

The ATS System is currently running and accessible at:

🔗 **[https://resume-matching-system-vcut3s4lzrglkpstjct9j7.streamlit.app/](https://resume-matching-system-vcut3s4lzrglkpstjct9j7.streamlit.app/)**

### How to Use the Live Demo:

1. **Visit the Link**: Click on the link above to access the live application
2. **Upload Resume**: Upload your PDF resume using the file uploader
3. **Enter Job Description**: Paste the job description you want to match against
4. **Get Analysis**: Click either "Tell Me About the Resume" or "Percentage Match" buttons
5. **View Results**: Review the AI-powered analysis and recommendations

### Demo Features:
- ✅ **Real-time Processing**: Instant resume analysis
- ✅ **AI-Powered Insights**: Detailed feedback on resume quality
- ✅ **Percentage Matching**: Compatibility score with job requirements
- ✅ **Keyword Analysis**: Missing keywords identification
- ✅ **Professional Interface**: Clean, user-friendly design

**Note**: The live demo uses the same AI technology (Groq LLaMA 3.3 70B) as the local installation, providing identical results and analysis quality.
