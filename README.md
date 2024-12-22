# 🔬 FileFlow AI: Your Smart Document Classification Solution

---

## 🔧 Overview
FileFlow AI is an **innovative and intelligent document classification system** designed to simplify the workflow for Financial Institutions. Using a robust, Python-based technology stack, it offers:

🔑 **Comprehensive Document Handling:**
- Bank Applications: Credit card, savings account forms
- Identity Documents: Driver’s licenses, passports
- Financial Documents: Income statements, tax returns, pay stubs
- Receipts: Retail and service receipts

🌐 **Hierarchical Categorization:**
1. **Personalization:** Documents are associated with individuals via unique identifiers like names, government IDs, or email addresses.
2. **Efficient Organization:** Grouping documents by type ensures effortless retrieval.

---

## 🎯 Key Features
- 🖥️ **Multi-format Support:** Handles PDFs, images, and more.
- 🌟 **Accurate Classification:** Advanced machine learning models for reliable results.
- 🕵️ **Seamless OCR Integration:** Extract text with precision using Tesseract OCR.
- 🌐 **API Access:** FastAPI endpoints simplify backend interaction.
- 🏛️ **Intuitive Interface:** Clean and interactive design for all users.

---

## 🛠️ Installation Guide
### Prerequisites
Ensure the following are installed:
- **Python 3.8 or higher**
- **pip** (Python package installer)

### Installation Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/mohammeduvez29/FileFlowAI/
   cd FileFlowAI
   ```
2. **Set Up Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Install Tesseract OCR:**
   - **Linux:** `sudo apt-get install tesseract-ocr`
   - **macOS:** `brew install tesseract`
   - **Windows:** [Download Tesseract](https://github.com/tesseract-ocr/tesseract).
5. **Run the Application:**
   ```bash
   streamlit run frontend/streamlit_app.py
   ```

---

## 📘 Usage Instructions
### Upload and Classify Documents
1. Launch the application using:
   ```bash
   streamlit run frontend/streamlit_app.py
   ```
2. Open your browser and access the app interface.
3. Upload PDFs or images.
4. Review extracted text and classification results in real-time.

### API Interaction
FastAPI’s backend provides classification and text extraction endpoints. View documentation at:
`http://localhost:8000/docs`.

---

## 🤖 Technology Stack
### Frontend
- 🎮 **Streamlit:** User-friendly interactive web app framework.

### Backend
- 🌐 **FastAPI:** High-performance, interactive API platform.

### Core Components
- **Machine Learning:** 🧐 scikit-learn for precise document categorization.
- **OCR:** 🕵️ Tesseract OCR for seamless text extraction.
- **NLP:** 🎨 NLTK for efficient text processing.
- **Database:** 🏙 SQLite for lightweight metadata storage.
- **PDF Processing:** 🔖 PyPDF2 for robust document handling.

---

## 🔄 Project Structure
```
FileFlowAI/
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

---

## 👨‍💼 Contributors
Our team of talented individuals:

💎 **Mohammed Uvez Khan**  
💎 **Farman I**  
💎 **Arafat Farooqui**  
💎 **Aman Ramzan Sheikh**  

For inquiries or feedback, contact us at [mohammeduvezkhan@gmail.com](mailto:mohammeduvezkhan@gmail.com).

---

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## 🎉 Get Started Now!
Transform the way you manage documents with FileFlow AI. 🚀 Start automating your workflows today!

