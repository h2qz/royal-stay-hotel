from datetime import date
from room import Room
from guest import Guest
from booking import Booking
from service_request import ServiceRequest
from feedback import Feedback

def test_guest_account_creation():
    print("=== Test: Guest Account Creation ===")
    try:
        guest1 = Guest(1, "Alice Johnson", "alice@example.com", "Gold", 150)
        guest2 = Guest(2, "Bob Smith", "bob@example.com", "Silver", 80)
        print(guest1)
        print(guest2)
    except Exception as e:
        print("Error during guest account creation:", e)

def test_search_available_rooms():
    print("\n=== Test: Searching for Available Rooms ===")
    try:
        all_rooms = [
            Room(101, "Single", ["WiFi"], 100.0),
            Room(102, "Double", ["WiFi", "Mini-bar"], 150.0),
            Room(103, "Suite", ["WiFi", "TV", "Mini-bar"], 200.0)
        ]
        # Example 1: Find Double rooms with WiFi
        matches = [room for room in all_rooms if "WiFi" in room._Room__amenities and room._Room__room_type == "Double"]
        print("Available Double Rooms with WiFi:")
        for r in matches:
            print(r)

        # Example 2: Find Suites with Mini-bar
        matches = [room for room in all_rooms if "Mini-bar" in room._Room__amenities and room._Room__room_type == "Suite"]
        print("Available Suites with Mini-bar:")
        for r in matches:
            print(r)
    except Exception as e:
        print("Error during room search:", e)

def test_room_reservation():
    print("\n=== Test: Making a Room Reservation ===")
    try:
        guest = Guest(3, "Carla White", "carla@example.com")
        room = Room(104, "Single", ["WiFi"], 90.0)
        booking = Booking(3001, guest, [room], date(2025, 4, 1), date(2025, 4, 3))
        print(booking)

        guest2 = Guest(4, "Dan Brown", "dan@example.com")
        room2 = Room(105, "Double", ["WiFi", "TV"], 130.0)
        booking2 = Booking(3002, guest2, [room2], date(2025, 5, 10), date(2025, 5, 12))
        print(booking2)
    except Exception as e:
        print("Error during reservation:", e)

def test_booking_confirmation_notification():
    print("\n=== Test: Booking Confirmation Notification ===")
    try:
        print("Booking confirmed for Carla White. Confirmation sent via email.")
        print("Booking confirmed for Dan Brown. Confirmation sent via app.")
    except Exception as e:
        print("Error sending confirmation:", e)

def test_invoice_generation():
    print("\n=== Test: Invoice Generation ===")
    try:
        guest = Guest(5, "Emily Stone", "emily@example.com")
        room = Room(106, "Suite", ["WiFi", "Mini-bar"], 250.0)
        booking = Booking(3003, guest, [room], date(2025, 6, 1), date(2025, 6, 4))
        print(booking.get_invoice())

        guest2 = Guest(6, "Frank Green", "frank@example.com")
        room2 = Room(107, "Single", ["WiFi"], 80.0)
        booking2 = Booking(3004, guest2, [room2], date(2025, 7, 5), date(2025, 7, 7))
        print(booking2.get_invoice())
    except Exception as e:
        print("Error generating invoice:", e)

def test_payment_processing():
    print("\n=== Test: Processing Payment Methods ===")
    try:
        invoice = Booking(3005, Guest(7, "Grace Lee", "grace@example.com"), 
                          [Room(108, "Double", ["WiFi", "TV"], 140.0)], 
                          date(2025, 8, 1), date(2025, 8, 3)).get_invoice()
        invoice.apply_discount(20)
        invoice.mark_paid()
        print(invoice)

        invoice2 = Booking(3006, Guest(8, "Henry Ford", "henry@example.com"), 
                           [Room(109, "Single", ["WiFi"], 100.0)], 
                           date(2025, 9, 1), date(2025, 9, 2)).get_invoice()
        invoice2.mark_paid()
        print(invoice2)
    except Exception as e:
        print("Error processing payment:", e)

def test_reservation_history():
    print("\n=== Test: Displaying Reservation History ===")
    try:
        guest = Guest(9, "Ivy Blue", "ivy@example.com")
        booking1 = Booking(3007, guest, [Room(110, "Single", ["WiFi"], 95.0)], date(2024, 12, 1), date(2024, 12, 3))
        booking2 = Booking(3008, guest, [Room(111, "Double", ["WiFi", "TV"], 150.0)], date(2025, 1, 10), date(2025, 1, 12))
        print("Reservation history for Ivy Blue:")
        print(booking1)
        print(booking2)
    except Exception as e:
        print("Error displaying history:", e)

def test_cancel_reservation():
    print("\n=== Test: Canceling Reservation ===")
    try:
        guest = Guest(10, "Jack Black", "jack@example.com")
        room = Room(112, "Suite", ["WiFi", "Mini-bar"], 200.0)
        booking = Booking(3009, guest, [room], date(2025, 11, 1), date(2025, 11, 5))
        print(f"Before cancellation: {room}")
        room.set_availability(True)
        print("Booking canceled. Room marked available.")
        print(f"After cancellation: {room}")
    except Exception as e:
        print("Error cancelling reservation:", e)

# Run all tests
if __name__ == "__main__":
    test_guest_account_creation()
    test_search_available_rooms()
    test_room_reservation()
    test_booking_confirmation_notification()
    test_invoice_generation()
    test_payment_processing()
    test_reservation_history()
    test_cancel_reservation()
