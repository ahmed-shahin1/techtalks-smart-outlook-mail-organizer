# app/models/email.py
"""
Pydantic schemas for email processing.
"""

from pydantic import BaseModel, Field, EmailStr
from typing import List, Optional
from datetime import datetime

class EmailRequest(BaseModel):
    """
    Schema for an incoming email request to the backend.
    """
    subject: str = Field(..., example="Meeting Reminder")
    sender: EmailStr = Field(..., example="boss@example.com")
    body: str = Field(..., example="Please attend the meeting at 10 AM.")
    received_date: Optional[datetime] = Field(None, example="2026-02-03T10:00:00Z")
    attachments: Optional[List[str]] = Field(default_factory=list, example=["agenda.pdf", "notes.docx"])

class EmailSummaryResponse(BaseModel):
    """
    Schema for summarization/categorization response.
    """
    email_id: str = Field(..., example="12345")
    summary: str = Field(..., example="Meeting scheduled at 10 AM, attendance required.")
    category: str = Field(..., example="Work")
    priority: str = Field(..., example="High")
    action_items: Optional[List[str]] = Field(default_factory=list, example=["Attend meeting", "Prepare slides"])
    sentiment: Optional[str] = Field(None, example="Neutral")
    key_points: Optional[List[str]] = Field(default_factory=list, example=["Meeting time: 10 AM", "Location: Zoom"])
