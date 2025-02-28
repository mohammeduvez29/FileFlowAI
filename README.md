# 🔬 FileFlow AI: Your Smart Document Classification Solution

PRESENTATION DECK: https://stdntpartners-my.sharepoint.com/:p:/g/personal/mohammeduvez_khan_studentambassadors_com/EeAd0pirnMdEpSf9fBtbskkBb8YsHqWJEan8DRCqXSb6hg?e=YQO0yI
---

## 🔧 Overview
FileFlow AI is an **innovative and intelligent document classification system** designed to simplify the workflow for Financial Institutions. Using a robust, AI-driven technology stack, it offers:

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
- 🖥️ **AI-Driven Document Intelligence:** Automatically categorizes and retrieves documents.
- 🌟 **Hyper-Personalized Automation:** Predicts and suggests document classification, cutting human effort by 80%.
- 🕵️ **Seamless OCR Integration:** Extract text with precision using Azure AI Document Intelligence.
- 🔒 **Fraud Detection & Compliance:** Ensures adherence to strict KYC & AML standards.
- 🌐 **Enterprise-Grade Integration:** Works with existing banking & CRM systems.

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
4. **Run the Application:**
   ```bash
   python app/main.py
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
FastAPI backend provides classification and text extraction endpoints. View documentation at:
`http://localhost:8000/docs`.

---

## 🤖 Technology Stack
### Backend
- ⚡ **FastAPI:** High-speed processing for document handling.
- 🧠 **AI/ML:** Custom-trained NLP model, OCR (Tesseract), PyTorch.
- 🔍 **Data Processing:** Pandas, NLTK, spaCy.

### Storage & Security
- 📦 **Storage:** Azure Blob Storage (Free Tier) for secure document storage.
- 📝 **Database:** Azure Cosmos DB (Free Tier) for scalable, NoSQL document storage.
- 🔐 **Monitoring & Security:** Azure Application Insights (Free Tier) for performance monitoring.

### OCR & AI
- 🕵️ **OCR:** Azure AI Document Intelligence (Free Tier) for accurate text extraction.

### Compute & Deployment
- 🚀 **Deployment:** Azure App Service (Free Tier) for scalable API hosting.

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

For inquiries or feedback, contact us at [mohammeduvezkhan@gmail.com](mailto:mohammeduvezkhan@gmail.com).

---

## 📜 License
This project is licensed under the **MIT License**. See the [LICENSE](./LICENSE) file for details.

---

## 🎉 Get Started Now!
Transform the way you manage documents with FileFlow AI. 🚀 Start automating your workflows today!

