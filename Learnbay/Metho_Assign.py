class Flight:
    def __init__(self, flight_no, base_price, total_seats):
        self.flight_no = flight_no
        self.base_price = base_price
        self.total_seats = total_seats
        print("Flight Constructor Called")

    def display_flight_info(self):
        print(f"Flight No: {self.flight_no}")
        print(f"Base Price: {self.base_price}")
        print(f"Total Seats: {self.total_seats}")


class DomesticFlight(Flight):
    def __init__(self, flight_no, base_price, total_seats, tax_percent):
        super().__init__(flight_no, base_price, total_seats)
        self.tax_percent = tax_percent
        print("DomesticFlight Constructor Called")

    def calculate_price(self):
        final_price = self.base_price + (self.base_price * self.tax_percent / 100)
        return final_price


class BookingFlight(DomesticFlight):
    def __init__(self, flight_no, base_price, total_seats, tax_percent):
        super().__init__(flight_no, base_price, total_seats, tax_percent)
        self.booked_seats = 0
        print("BookingFlight Constructor Called")

    def check_seat_availability(self, requested_seats):
        available_seats = self.total_seats - self.booked_seats
        if requested_seats <= available_seats:
            print("Seats Available")
            return True
        else:
            print("Seats Not Available")
            return False

    def book_seats(self, requested_seats):
        if self.check_seat_availability(requested_seats):
            self.booked_seats += requested_seats
            print(f"{requested_seats} seats booked successfully")
        else:
            print("Booking Failed")

    def get_final_price(self, no_of_tickets):
        price_per_ticket = self.calculate_price()
        return price_per_ticket * no_of_tickets


flight1 = BookingFlight("AI202", 5000, 100, 10)

flight1.display_flight_info()

flight1.book_seats(5)

total_amount = flight1.get_final_price(5)

print("Total Amount to Pay:", total_amount)
