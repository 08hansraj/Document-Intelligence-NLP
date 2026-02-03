from transformers import pipeline

# Mapping from UI language to MarianMT model
LANGUAGE_MODEL_MAP = {
    "Hindi": "Helsinki-NLP/opus-mt-en-hi",
    "French": "Helsinki-NLP/opus-mt-en-fr",
    "German": "Helsinki-NLP/opus-mt-en-de",
    "Spanish": "Helsinki-NLP/opus-mt-en-es"
}

# Cache loaded pipelines so we don't reload models repeatedly
_TRANSLATOR_CACHE = {}


def get_translator(target_language: str):
    if target_language not in LANGUAGE_MODEL_MAP:
        raise ValueError("Unsupported language selected")

    if target_language not in _TRANSLATOR_CACHE:
        model_name = LANGUAGE_MODEL_MAP[target_language]
        _TRANSLATOR_CACHE[target_language] = pipeline(
            f"translation_en_to_{model_name.split('-')[-1]}",
            model=model_name
        )

    return _TRANSLATOR_CACHE[target_language]


def translate_text(text: str, target_language: str) -> str:
    if not text or len(text.strip()) == 0:
        return ""

    translator = get_translator(target_language)
    result = translator(text)

    return result[0]["translation_text"]
