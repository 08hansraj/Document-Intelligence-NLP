# AI-Powered Document Intelligence & Translation System (NLP)

An end-to-end Document Intelligence system built using Transformer-based NLP models that enables automated document ingestion, text preprocessing, summarization, and translation. The system is designed with a modular architecture to support real-world document analytics workflows.

---

## Overview

This project processes unstructured documents (such as PDFs), extracts clean text, applies Natural Language Processing techniques, and generates meaningful outputs such as summaries and translations using pretrained Hugging Face Transformer models.

The system emphasizes **modularity, reusability, and production-readiness**, rather than notebook-only experimentation.

---

## Key Capabilities

* PDF document ingestion and text extraction
* Text cleaning and normalization utilities
* Abstractive text summarization using Transformer models
* Multilingual text translation using pretrained NLP pipelines
* Modular NLP components for easy extensibility
* Streamlit-based interactive interface

---

## Project Structure

```
doc_intelligence/
│
├── app.py                     # Main application entry point (Streamlit UI)
├── README.md
├── requirements.txt
│
├── nlp/
│   ├── __init__.py
│   ├── summarizer.py          # Transformer-based text summarization
│   └── translator.py          # NLP-based text translation
│
├── utils/
│   ├── __init__.py
│   ├── pdf_reader.py          # PDF text extraction logic
│   └── text_utils.py          # Text cleaning and preprocessing utilities
│
└── venv/                      # Local virtual environment (ignored in Git)
```

---

## NLP Models & Techniques

* Hugging Face Transformers
* Abstractive summarization pipelines
* Sequence-to-sequence language translation
* Tokenization and text normalization

The system leverages pretrained Transformer architectures to ensure high-quality language understanding and generation.

---

## Tech Stack

* Python
* Hugging Face Transformers
* PyTorch
* Streamlit
* PDF parsing libraries
* NLP preprocessing utilities

---

## How to Run the Project

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/document-intelligence-nlp.git
cd document-intelligence-nlp
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the Application

```bash
streamlit run app.py
```

Open the browser at:

```
http://localhost:8501
```

---

## Design Highlights

* **Modular NLP Pipeline**: Each NLP task (summarization, translation, preprocessing) is isolated into reusable modules
* **Transformer-Based Intelligence**: Uses state-of-the-art pretrained models rather than rule-based NLP
* **Scalable Architecture**: Easy to extend with additional NLP tasks such as NER or classification
* **Clean Separation of Concerns**: UI, NLP logic, and utilities are clearly decoupled

---

## Future Enhancements

* Named Entity Recognition (NER)
* Multi-document summarization
* Support for scanned PDFs with OCR
* API-based deployment using FastAPI
* Model switching and configuration support

---

## Summary

AI-powered Document Intelligence system leveraging Transformer-based NLP models for document ingestion, summarization, and translation, designed with modular architecture and real-world extensibility in mind.

---

## License

This project is intended for educational and demonstration purposes.
