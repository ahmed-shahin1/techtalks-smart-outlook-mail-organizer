# utils/text_cleaner.py

import re

def clean_text(text: str) -> str:
    """
    Clean and normalize email text:
    - Remove extra spaces and newlines
    - Remove special characters except basic punctuation
    - Convert to lowercase
    """
    if not text:
        return ""
    
    # Remove newlines and extra spaces
    text = text.replace("\n", " ").replace("\r", " ")
    text = re.sub(r"\s+", " ", text).strip()
    
    # Remove unwanted special characters (keep letters, numbers, basic punctuation)
    text = re.sub(r"[^a-zA-Z0-9.,!?@ ]+", "", text)
    
    # Convert to lowercase
    text = text.lower()
    
    return text
