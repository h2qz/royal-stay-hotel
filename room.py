class Room:
    """Represents a hotel room."""

    def __init__(self, room_number: int, room_type: str, amenities: list, price_per_night: float, is_available: bool = True):
        self.__room_number = room_number
        self.__room_type = room_type
        self.__amenities = amenities
        self.__price_per_night = price_per_night
        self.__is_available = is_available

    def get_room_number(self):
        return self.__room_number

    def is_available(self):
        return self.__is_available

    def set_availability(self, status: bool):
        self.__is_available = status

    def get_price(self):
        return self.__price_per_night

    def __str__(self):
        return f"Room {self.__room_number} ({self.__room_type}) - ${self.__price_per_night}/night | Available: {self.__is_available}"
