# app/api/routes.py
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.summarizer import summarize_email

router = APIRouter()

class EmailRequest(BaseModel):
    subject: str
    body: str
    sender: str
    category: str
    priority: str

class EmailDataResponse(BaseModel):
    subject: str
    body: str
    sender: str
    category: str
    priority: str
    summary: str
    action_items: list
    suggested_reply: str

@router.post("/get-email-data", response_model=EmailDataResponse)
def get_email_data(email: EmailRequest):
    try:
        ai_result = summarize_email(
            subject=email.subject,
            body=email.body,
            category=email.category,
            priority=email.priority
        )

        return {
            "subject": email.subject,
            "body": email.body,
            "sender": email.sender,
            "category": email.category,
            "priority": email.priority,
            "summary": ai_result.get("summary", ""),
            "action_items": ai_result.get("action_items", []),
            "suggested_reply": ai_result.get("suggested_reply", "")
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))