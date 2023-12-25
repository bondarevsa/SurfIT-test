from datetime import datetime

from pydantic import BaseModel, Field

from app.database import AdvertisementType, ComplaintType


class AdvertisementBase(BaseModel):
    id: int
    adv_type: AdvertisementType
    header: str
    created_at: datetime
    created_by: int


class AdvertisementCreateResponse(AdvertisementBase):
    body: str


class AdvertisementCreate(BaseModel):
    body: str
    adv_type: AdvertisementType
    header: str


class ReviewCreate(BaseModel):
    text: str
    rating: int = Field(ge=1, le=5)


class ComplaintBase(BaseModel):
    text: str
    complaint_type: ComplaintType


class ComplaintResponse(ComplaintBase):
    id: int
    advertisement_id: int
    created_at: datetime
    created_by: int
