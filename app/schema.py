from fastapi import Query
from pydantic import BaseModel
from datetime import date


class HotelSearchArgs():
    def __init__(self, location: str,
                 date_from: date,
                 date_to: date,
                 stars: int = Query(None, ge=1, le=5),
                 has_wifi: bool = Query(None)):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.stars = stars
        self.has_wifi = has_wifi


class Booking(BaseModel):
    room_id: int
    date_from: date
    date_to: date
