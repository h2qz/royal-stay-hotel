from datetime import datetime

class Feedback:
    """Handles feedback provided by guests."""

    def __init__(self, feedback_id: int, guest_id: int, rating: int, comments: str):
        self.__feedback_id = feedback_id
        self.__guest_id = guest_id
        self.__rating = rating
        self.__comments = comments
        self.__date = datetime.now().date()

    def __str__(self):
        return f"Feedback #{self.__feedback_id} by Guest {self.__guest_id} | Rating: {self.__rating}/5 | Comment: {self.__comments}"
