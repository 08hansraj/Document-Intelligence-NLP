# AI-Powered Document Intelligence & Translation System (NLP)

An end-to-end **Document Intelligence** system built using **Transformer-based NLP models** that supports automated document ingestion, text preprocessing, summarization, and translation. The project follows a clean, modular structure so it can be extended into real-world document analytics workflows.

---

## Overview

This project processes unstructured documents (such as PDFs), extracts clean text, applies Natural Language Processing techniques, and generates meaningful outputs such as **summaries** and **translations** using pretrained Hugging Face Transformer models.

The focus is on **modularity and reusability** (not just notebook experimentation).

---

## Key Capabilities

* PDF document ingestion and text extraction
* Text cleaning and normalization utilities
* Abstractive text summarization using Transformer models
* Multilingual text translation using pretrained NLP pipelines
* Modular NLP components for easy extensibility
* Streamlit-based interactive UI

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

> **Note:** The `venv/` folder should not be committed to GitHub.

---

## NLP Models & Techniques

* Hugging Face Transformers
* Abstractive summarization pipelines
* Sequence-to-sequence translation
* Tokenization and text normalization

The system uses pretrained Transformer architectures for strong language understanding and generation.

---

## Tech Stack

* Python
* Hugging Face Transformers
* PyTorch
* Streamlit
* PDF parsing libraries

---

## Setup & Run

### 1) Clone the Repository

```bash
git clone https://github.com/<your-username>/document-intelligence-nlp.git
cd document-intelligence-nlp
```

---

### 2) Create and Activate Virtual Environment (Recommended)

> **Recommended Python version:** 3.10 or 3.11 (best compatibility for Transformers + PyTorch)

**Windows (PowerShell):**

```powershell
python -m venv venv
venv\Scripts\activate
```

---

### 3) Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4) Run the Application

> Always run Streamlit using `python -m` to avoid environment conflicts.

```bash
python -m streamlit run app.py
```

Open your browser at:

```
http://localhost:8501
```

---

## Common Troubleshooting

### First run is slow (model download)

The first time you use summarization or translation, Hugging Face will download the required model weights and cache them locally. This is expected and may take a few minutes depending on your internet speed.

Subsequent runs will be significantly faster because models are loaded from the local cache.

---

### Streamlit runs from the wrong Python

If you have multiple Python versions installed, always run:

```bash
python -m streamlit run app.py
```

Instead of:

```bash
streamlit run app.py
```

---

### Verify your environment

```bash
python -c "import sys; print(sys.executable)"
```

Expected output should include:

```
...\doc_intelligence\venv\Scripts\python.exe
```

---

## License

This project is intended for educational and demonstration purposes.
