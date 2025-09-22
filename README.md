# ATS System - Resume Matching Application

## 📋 Project Overview

This is an intelligent **Applicant Tracking System (ATS)** designed specifically for companies and HR departments to efficiently screen and rank resumes. When companies receive hundreds of resumes for a single job posting, this AI-powered system helps identify the top candidates by analyzing resume quality, keyword matching, and compatibility with job requirements.

**Perfect for HR Teams**: Streamline your recruitment process by quickly identifying the most qualified candidates from a large pool of applicants.

## 🚀 Features

### For HR Teams & Companies:
- **Bulk Resume Screening**: Process multiple resumes quickly and efficiently
- **Automated Ranking**: AI automatically ranks candidates based on job requirements
- **Time-Saving**: Reduce manual screening time from hours to minutes
- **Consistent Evaluation**: Eliminate human bias with standardized AI analysis
- **Top Candidate Identification**: Instantly identify the best matches from hundreds of applications

### Technical Features:
- **PDF Resume Processing**: Supports both text-based and image-based PDFs
- **AI-Powered Analysis**: Uses Groq's LLaMA 3.3 70B model for intelligent analysis
- **Dual Extraction Methods**: Direct text extraction + OCR fallback for scanned PDFs
- **Interactive Web Interface**: Built with Streamlit for easy use
- **Detailed Feedback**: Provides percentage match, missing keywords, and recommendations

## 🛠️ How It Works

### For Companies with High Volume Applications:

#### Step 1: Job Description Setup
1. HR team enters the complete job description with requirements, skills, and qualifications
2. System creates a comprehensive profile for candidate matching

#### Step 2: Resume Processing Pipeline
1. Upload multiple resumes (one by one or in batches)
2. System automatically extracts text from each PDF using advanced OCR technology
3. Each resume is processed and stored for analysis

#### Step 3: AI-Powered Screening
1. AI analyzes each resume against the job requirements
2. System calculates compatibility scores and ranks candidates
3. Identifies top performers and highlights key strengths

#### Step 4: Candidate Ranking & Selection
1. View ranked list of candidates with percentage match scores
2. Review detailed analysis for each candidate
3. Identify missing skills and qualifications
4. Select top candidates for interview rounds

### Technical Process:
- **PDF Processing**: Direct text extraction + OCR fallback for scanned documents
- **AI Analysis**: Groq LLaMA 3.3 70B model provides intelligent candidate evaluation
- **Scoring System**: Automated percentage matching and ranking
- **Detailed Reports**: Comprehensive feedback for each candidate

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

### For HR Teams & Recruiters:

#### 1. Start the Application
```bash
streamlit run app.py
```

#### 2. Set Up Job Requirements
- Enter the complete job description in the text area
- Include all requirements, skills, qualifications, and experience needed
- Be specific about technical skills, soft skills, and education requirements

#### 3. Process Resumes
- Upload each candidate's resume PDF
- System will automatically extract and analyze the content
- Repeat for all received applications

#### 4. Analyze Candidates
- **"Tell Me About the Resume"**: Get detailed candidate evaluation
- **"Percentage Match"**: Get compatibility score for ranking

#### 5. Make Informed Decisions
- Review AI analysis for each candidate
- Compare percentage match scores
- Identify top candidates for interview rounds
- Use detailed feedback to prepare interview questions

### Workflow for High Volume Applications:
1. **Batch Processing**: Process resumes in groups of 10-20
2. **Ranking**: Sort candidates by percentage match scores
3. **Shortlisting**: Select top 20-30% for detailed review
4. **Interview Selection**: Choose final candidates based on AI insights

## 🔍 Features Explained

### For HR Teams:
- **Bulk Processing**: Handle hundreds of resumes efficiently
- **Automated Ranking**: AI automatically sorts candidates by compatibility
- **Time Efficiency**: Reduce screening time from days to hours
- **Bias Elimination**: Consistent, objective evaluation of all candidates
- **Quality Assurance**: Identify top talent from large applicant pools

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
2. **Enter Job Description**: Paste the complete job description with all requirements
3. **Upload Resumes**: Upload candidate resumes one by one for analysis
4. **Get Analysis**: Click either "Tell Me About the Resume" or "Percentage Match" buttons
5. **Review Results**: Compare candidates and identify top performers

### Demo Features for HR Teams:
- ✅ **Bulk Resume Processing**: Handle multiple candidates efficiently
- ✅ **Automated Ranking**: AI automatically scores and ranks candidates
- ✅ **Time-Saving**: Reduce manual screening time significantly
- ✅ **Objective Evaluation**: Consistent, bias-free candidate assessment
- ✅ **Top Candidate Identification**: Instantly spot the best matches
- ✅ **Professional Interface**: Clean, user-friendly design for HR teams

**Perfect for Testing**: Try the live demo with your actual job descriptions and candidate resumes to see how it can streamline your recruitment process.

**Note**: The live demo uses the same AI technology (Groq LLaMA 3.3 70B) as the local installation, providing identical results and analysis quality.
