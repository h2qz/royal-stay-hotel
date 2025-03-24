from datetime import date
from invoice import Invoice

class Booking:
    """Handles booking information for a guest."""

    def __init__(self, booking_id: int, guest, rooms: list, check_in_date: date, check_out_date: date, status: str = "Confirmed"):
        self.__booking_id = booking_id
        self.__guest = guest
        self.__rooms = rooms
        self.__check_in = check_in_date
        self.__check_out = check_out_date
        self.__status = status
        self.__invoice = self.__generate_invoice()

    def __generate_invoice(self):
        total = sum(room.get_price() for room in self.__rooms) * (self.__check_out - self.__check_in).days
        return Invoice(self.__booking_id, total, "Pending", 0.0)

    def get_invoice(self):
        return self.__invoice

    def __str__(self):
        return f"Booking #{self.__booking_id} for Guest {self.__guest.get_id()} from {self.__check_in} to {self.__check_out} | Status: {self.__status}"
