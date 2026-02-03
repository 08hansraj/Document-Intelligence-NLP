import streamlit as st

from utils.pdf_reader import extract_text_from_pdf
from utils.text_utils import clean_text
from nlp.summarizer import summarize_text
from nlp.translator import translate_text

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI-Powered Document Intelligence",
    layout="centered"
)

st.title("AI-Powered Document Intelligence & Translation System")

st.write(
    "Upload a PDF or paste text below, then choose the task you want to perform."
)

# ---------------- Input Section ----------------
uploaded_file = st.file_uploader(
    "Upload a PDF file",
    type=["pdf"]
)

text_input = st.text_area(
    "Or paste text here",
    height=200
)

# ---------------- Task Selection ----------------
task = st.selectbox(
    "Select task",
    ["Extract Text", "Summarize", "Translate", "Summarize + Translate"]
)

language = None
if task in ["Translate", "Summarize + Translate"]:
    language = st.selectbox(
        "Select target language",
        ["Hindi", "French", "German", "Spanish"]
    )

# ---------------- Process Button ----------------
if st.button("Process"):
    if not uploaded_file and not text_input.strip():
        st.warning("Please upload a PDF or paste some text.")
    else:
        with st.spinner("Processing..."):
            # Step 1: Extract raw text
            if uploaded_file:
                raw_text = extract_text_from_pdf(uploaded_file)
            else:
                raw_text = text_input

            # Step 2: Clean text
            cleaned_text = clean_text(raw_text)

            # Step 3: Perform selected task
            if task == "Extract Text":
                output = cleaned_text

            elif task == "Summarize":
                output = summarize_text(cleaned_text)

            elif task == "Translate":
                output = translate_text(cleaned_text, language)

            else:  # Summarize + Translate
                summary = summarize_text(cleaned_text)
                output = translate_text(summary, language)

        # ---------------- Output Section ----------------
        st.subheader("Output")
        st.text_area(
            "Result",
            output,
            height=300
        )
