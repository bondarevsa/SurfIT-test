from datetime import datetime

from pydantic import BaseModel


class AllAdvertisements(BaseModel):
    adv_type: str
    header: str
    timestamp: datetime
    user_id: int


class AdvertisementBase(BaseModel):
    id: int
    body: str
    adv_type: str
    header: str
    timestamp: datetime
    user_id: int
