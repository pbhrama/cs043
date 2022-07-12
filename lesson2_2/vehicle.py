class Vehicle:
    def __init__(self, weight, passengers, vehicle_economy):
        self.weight = weight
        self.passengers = passengers
        self.vehicle_economy = vehicle_economy

    def __repr__(self):
        return ("<" + self.__class__.__name__ +
                " weight=" + str(self.weight) +
                " passengers=" + str(self.passengers) +
                " vehicle_economy=" + str(self.vehicle_economy) +
                ">")

    def weight_per_passenger(self):
        return self.weight / self.passengers

    def passenger_economy(self):
        return self.vehicle_economy * self.passengers

    def passenger_distance_cost(self, fuel_price):
        return fuel_price / self.passenger_economy()
