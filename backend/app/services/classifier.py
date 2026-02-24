# app/services/classifier.py
"""
Email categorization logic with extended keywords.
"""

def classify_email(subject: str, body: str) -> str:
    """
    Categorize emails into Work, Finance, Social, or General.
    Extended keywords for better detection.
    """
    subject_lower = subject.lower()
    body_lower = body.lower()
    text = f"{subject_lower} {body_lower}"

    # Work-related keywords
    work_keywords = [
        'meeting', 'project', 'deadline', 'schedule', 'presentation', 
        'report', 'task', 'update', 'agenda', 'client', 'team', 'review'
    ]

    # Finance-related keywords
    finance_keywords = [
        'invoice', 'payment', 'billing', 'receipt', 'due', 'salary', 
        'expense', 'budget', 'refund', 'financial', 'statement'
    ]

    # Social-related keywords
    social_keywords = [
        'party', 'celebration', 'birthday', 'congratulations', 
        'invitation', 'wedding', 'event', 'gathering', 'meetup', 'fun'
    ]

    # Check categories
    if any(word in text for word in work_keywords):
        return "Work"
    elif any(word in text for word in finance_keywords):
        return "Finance"
    elif any(word in text for word in social_keywords):
        return "Social"
    else:
        return "General"
