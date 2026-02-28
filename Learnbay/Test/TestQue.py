class flight:
    def __init__(self, flight_no, source, destination, base_fare):
        self.flight_no = flight_no
        self.source = source
        self.destination = destination
        self.base_fare = base_fare
        print("Flight Constructor Called")

    def update_route(self, source=None, destination=None):
        if source is not None:
            self.source = source
        if destination is not None:
            self.destination = destination

    def display_flight_info(self):
        print(f"flight_no: {self.flight_no}")
        print(f"source: {self.source}")
        print(f"destination: {self.destination}")

    def calculate_fare(self, passenger_count, discount_percent=0):
        total_fare = self.base_fare * passenger_count
        if discount_percent > 0:
            total_fare = total_fare - (total_fare * discount_percent/100)
        return total_fare

flight = flight("AI202", "Pune", "Delhi", 1000)
flight.display_flight_info()

total_fare = flight.calculate_fare(5, 10)

print("Total Fare:", total_fare)

# only one passenger

fare_discount1 = flight.calculate_fare(3)
print("fair_discount", fare_discount1)

# pssenger count + discoun

fare_discount2 = flight.calculate_fare(3 ,5)
print("fare_discount2 5% = ", fare_discount2)

# Update route
flight.update_route(destination="Mumbai")
flight.display_flight_info()

flight.update_route(source="Banglore", destination="Hydrabad")
flight.display_flight_info()