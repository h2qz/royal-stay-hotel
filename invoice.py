class Invoice:
    """Represents the invoice for a booking."""

    def __init__(self, invoice_id: int, total_amount: float, payment_status: str, discount: float = 0.0):
        self.__invoice_id = invoice_id
        self.__total_amount = total_amount
        self.__payment_status = payment_status
        self.__discount = discount

    def apply_discount(self, discount: float):
        self.__discount = discount
        self.__total_amount -= discount

    def mark_paid(self):
        self.__payment_status = "Paid"

    def __str__(self):
        return f"Invoice #{self.__invoice_id} - Amount: ${self.__total_amount:.2f} | Status: {self.__payment_status} | Discount: ${self.__discount:.2f}"
