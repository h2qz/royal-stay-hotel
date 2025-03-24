
class Guest:
    """Represents a hotel guest."""

    def __init__(self, guest_id: int, name: str, contact_info: str, loyalty_status: str = "Regular", points: int = 0):
        self.__guest_id = guest_id
        self.__name = name
        self.__contact_info = contact_info
        self.__loyalty_status = loyalty_status
        self.__points = points

    def get_id(self):
        return self.__guest_id

    def add_points(self, amount: int):
        self.__points += amount

    def redeem_points(self, amount: int):
        if amount <= self.__points:
            self.__points -= amount

    def __str__(self):
        return f"Guest {self.__name} (ID: {self.__guest_id}) - {self.__loyalty_status} | Points: {self.__points}"
