from transformers import pipeline


# Load the summarization pipeline once
# This downloads the model the first time and caches it locally
summarizer = pipeline(
    task="summarization",
    model="facebook/bart-large-cnn"
)


def summarize_text(text: str, max_length: int = 150) -> str:
    """
    Generates a summary for the given text using a pretrained transformer.

    Parameters:
        text (str): Clean input text
        max_length (int): Maximum length of the summary

    Returns:
        str: Generated summary
    """
    if not text or len(text.strip()) == 0:
        return ""

    summary = summarizer(
        text,
        max_length=max_length,
        min_length=40,
        do_sample=False
    )

    return summary[0]["summary_text"]
