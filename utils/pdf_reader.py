import pdfplumber


def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a PDF file using pdfplumber.

    Parameters:
        pdf_file: Uploaded PDF file object (from Streamlit or file path)

    Returns:
        text (str): Combined text from all pages
    """
    text = ""

    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    return text
