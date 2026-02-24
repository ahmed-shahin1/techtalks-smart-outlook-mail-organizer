import pytest
from app.services import classifier, summarizer, priority

def test_classify_keywords():
    email_text = "Urgent: Project deadline is today. Finance needs your report."
    categories = classifier.classify_email(email_text)
    assert "Work" in categories or "Finance" in categories

def test_summarizer_short_email():
    text = "Please review the attached document."
    summary = summarizer.summarize_email(text)
    assert summary != ""  # Should produce a summary

def test_priority_detection():
    urgent_email = "This is urgent! We need your response immediately."
    level = priority.detect_priority(urgent_email)
    assert level == "High"
    
    normal_email = "Just a friendly reminder about our meeting next week."
    level = priority.detect_priority(normal_email)
    assert level == "Normal"
