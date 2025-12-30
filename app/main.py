from fastapi import Depends, FastAPI
from datetime import date
from .schema import HotelSearchArgs, Booking

app = FastAPI()


@app.get("/hotels")
async def get_hotels(hotel_search_args: HotelSearchArgs = Depends()):
    return hotel_search_args


@app.post("/bookings")
async def create_booking(booking: Booking):
    return {"message": "Booking created successfully!"}
