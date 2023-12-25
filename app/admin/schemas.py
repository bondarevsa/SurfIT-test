from datetime import datetime

from pydantic import BaseModel

from app.database import ComplaintType


class ComplaintBase(BaseModel):
    id: int
    complaint_type: ComplaintType
    text: str
    advertisement_id: int
    created_by: int
    created_at: datetime
