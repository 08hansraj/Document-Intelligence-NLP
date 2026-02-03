def clean_text(text: str) -> str:
    """
    Cleans raw extracted text for NLP processing.

    Steps:
    - Handles empty input
    - Removes line breaks
    - Normalizes extra whitespace

    Parameters:
        text (str): Raw extracted text

    Returns:
        str: Cleaned text
    """
    if not text:
        return ""

    # Replace newlines with spaces
    text = text.replace("\n", " ")

    # Remove extra spaces
    text = " ".join(text.split())

    return text
