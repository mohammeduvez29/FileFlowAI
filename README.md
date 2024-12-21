# FileFlow AI

## Document Classification System

## Project Description
FileFlow AI is a robust document classification system leveraging a free, Python-based technology stack. It allows users to upload and classify documents into predefined categories while processing text and metadata efficiently. The system supports various document formats, including PDFs and images, and provides a user-friendly interface for interaction. It addresses the challenge of automating the categorization and summarization of diverse document types such as:
- Applications for bank accounts (e.g., credit card, savings account)
- Identity documents (e.g., driver’s license, passports)
- Supporting financial documents (e.g., income statements, tax returns, paystubs)
- Receipts

The system ensures hierarchical categorization by:
1. Associating documents with the correct individual using identifiers like name, government ID, or email address.
2. Grouping documents by type for efficient organization.

## Installation Instructions

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8 or higher
- pip (Python package installer)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/mohammeduvez29/FileFlowAI/
   cd FileFlowAI
   ```
2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Install Tesseract OCR:
   - **Linux**: `sudo apt-get install tesseract-ocr`
   - **MacOS**: `brew install tesseract`
   - **Windows**: Download and install Tesseract from [official website](https://github.com/tesseract-ocr/tesseract).
5. Run the application:
   ```bash
   streamlit run frontend/streamlit_app.py
   ```

## Usage Guide

### Upload and Classify Documents
1. Launch the application using the command `streamlit run frontend/streamlit_app.py`.
2. Navigate to the web application in your browser.
3. Upload documents in PDF or image formats.
4. View the extracted text and classification results on the dashboard.

### API Interaction
The backend API is built using FastAPI and provides endpoints for classification and text extraction. Access interactive documentation at `http://localhost:8000/docs` once the FastAPI server is running.

## Technology Stack Overview

### Frontend
- **Streamlit**: Interactive web application framework for Python.

### Backend
- **FastAPI**: High-performance API framework with automatic documentation.

### Machine Learning
- **scikit-learn**: Comprehensive library for machine learning algorithms.

### OCR
- **Tesseract OCR**: Open-source OCR engine accessed via `pytesseract`.

### NLP
- **NLTK**: Toolkit for text preprocessing and natural language processing.

### Database
- **SQLite**: Lightweight, file-based database for storing document metadata and results.

### PDF Processing
- **PyPDF2**: Library for extracting text and handling PDF files.

## Project Structure Explanation
```
fileflow ai/
├── README.md
├── requirements.txt
├── app/
│   ├── main.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── document_classifier.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── ocr.py
│   │   ├── pdf_processor.py
│   │   └── text_preprocessor.py
│   └── api/
│       ├── __init__.py
│       └── routes.py
├── data/
│   └── sample_documents/
├── notebooks/
│   └── model_development.ipynb
├── tests/
│   ├── __init__.py
│   ├── test_classifier.py
│   └── test_utils.py
└── frontend/
    └── streamlit_app.py
```

## Team Members
- Mohammed Uvez Khan        [Mohammed Uvez Khan](images/uvez.jpg)
- Farman I
- Arafat Farooqui
- Aman Ramzan Sheikh

