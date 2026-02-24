import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Outlook Organizer API is running"}

def test_classify_email():
    email_data = {
        "subject": "Meeting Reminder",
        "body": "Please join the project meeting tomorrow at 10 AM."
    }
    response = client.post("/classify", json=email_data)
    assert response.status_code == 200
    assert "category" in response.json()
    assert "priority" in response.json()
    assert "summary" in response.json()

def test_empty_email():
    email_data = {"subject": "", "body": ""}
    response = client.post("/classify", json=email_data)
    assert response.status_code == 400
