class vehicle:

    def __init__(self,seating_capacity):
        self.seating_capacity =seating_capacity

    def get_fare(self):
        return self.seating_capacity*100
    
class Bus(vehicle):

    def __init__(self,seating_capacity):
        super().__init__(seating_capacity)

    def get_fare(self):
        vehicle_fare =super().get_fare()
        maintenance_fare=0.1*vehicle_fare
        total_fare = vehicle_fare + maintenance_fare
        return total_fare
    
vehicle1 =vehicle(50)
print("vechical fare:",vehicle1.get_fare())

bus1=Bus(50)
print("Bus fare: ",bus1.get_fare())