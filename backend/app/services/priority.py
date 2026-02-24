# app/services/priority.py
"""
Email priority detection logic.
"""

def detect_priority(subject: str, body: str) -> str:
    """
    Determine the priority of the email.
    Very simple rule-based for now.
    """
    high_keywords = ['urgent', 'asap', 'immediately', 'important']
    medium_keywords = ['review', 'follow up', 'tomorrow']

    text = f"{subject} {body}".lower()

    if any(word in text for word in high_keywords):
        return "High"
    elif any(word in text for word in medium_keywords):
        return "Medium"
    else:
        return "Low"
