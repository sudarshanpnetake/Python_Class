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
            # Check flight number (should be string, not numeric like 0.0)
            if not isinstance(flight_no, str):
                raise FlightNotFoundError("Invalid Flight Number")
            seats = int(total_seats)
            # Manually raise ValueError if seats <= 0
            if seats <= 0:
                raise ValueError("Total seats must be greater than 0.")

            # Assign values if everything is valid
            flight_no = flight_no
            source = source
            destination = destination
            total_seats = total_seats

            print("Flight added successfully!")

        except ValueError as ve:
            print("ValueError:", ve)

        except FlightNotFoundError as fe:
            print("FlightNotFoundError:", fe)

        except Exception as e:
            print("Something went wrong:", e)


# ------------------ Testing ------------------

f1 = Flight("", "", "", 0)

# Correct case
f1.add_flight("AI101", "Pune", "Delhi", "90")

# Invalid seats (negative)
f1.add_flight("AI102", "Pune", "Mumbai", "-90")

# Invalid seats (string error)
f1.add_flight("AI103", "Pune", "Goa", "90abc")

# Invalid flight number (numeric)
f1.add_flight(0.0, "Pune", "Chennai", "50")
