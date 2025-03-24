from datetime import datetime

class ServiceRequest:
    """Handles guest service requests."""

    def __init__(self, request_id: int, guest_id: int, request_type: str, status: str = "Pending"):
        self.__request_id = request_id
        self.__guest_id = guest_id
        self.__request_type = request_type
        self.__status = status
        self.__timestamp = datetime.now()

    def mark_resolved(self):
        self.__status = "Resolved"

    def __str__(self):
        return f"Service Request #{self.__request_id} by Guest {self.__guest_id} - {self.__request_type} | Status: {self.__status}"
