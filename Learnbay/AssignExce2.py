class FlightNotFoundError(Exception):
    pass


class Flight:
    def __init__(self, flight_no, source, destination, total_seats):
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.total_seats = total_seats

    def add_flight(self, flight_no, source, destination, total_seats):
        try:
            if not isinstance(flight_no, str):
                raise FlightNotFoundError("Invalid Flight Number")

            seats = int(total_seats)

            if seats <= 0:
                raise ValueError("Total seats must be greater than 0.")

            # ✅ Correct assignment
            self.flight_no = flight_no
            self.source = source
            self.destination = destination
            self.total_seats = seats

            print("Flight added successfully!")

        except ValueError as ve:
            print("ValueError:", ve)

        except FlightNotFoundError as fe:
            print("FlightNotFoundError:", fe)

        except Exception as e:
            print("Something went wrong:", e)

    # --------------------------------------------------
    # NEW METHOD: book_seat()
    # --------------------------------------------------

    def book_seat(self):

        # -------- First Try Block (Check Flight Exists) ----------
        try:
            flight_number = input("Enter flight number: ")

            if flight_number != self.flight_no:
                raise FlightNotFoundError("Flight not found!")

            print("Flight found:", self.flight_no)

        except FlightNotFoundError as fe:
            print("FlightNotFoundError:", fe)
            return  # stop execution if flight not found

        except Exception as e:
            print("Unexpected error:", e)
            return

        # -------- Second Try Block (Seat Booking Logic) ----------
        try:
            seats_to_book = input("Enter number of seats to book: ")
            seats_to_book = int(seats_to_book)

            if seats_to_book <= 0:
                raise ValueError("Seat count must be greater than 0")

            if seats_to_book > self.total_seats:
                raise RuntimeError("Not enough seats available")

            # Deduct seats
            self.total_seats -= seats_to_book

            print("Seats booked successfully!")
            print("Remaining seats:", self.total_seats)

        except ValueError as ve:
            print("ValueError:", ve)

        except RuntimeError as re:
            print("RuntimeError:", re)


# ------------------ Testing ------------------

f1 = Flight("", "", "", 0)

f1.add_flight("AI101", "Pune", "Delhi", "90")

# Now test booking
f1.book_seat()