class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
vehicle1 = Vehicle(240,18)
print(vehicle1.max_speed,end =" ")
print(vehicle1.mileage)    