class Car:

    fuel="petrol"
    status="new"

    def __init__(self, brand,number):
        self.brand = brand
        self.number = number

    def drive(self):
        print(f'Sending foto {self.brand} with {self.number}')

class Passenger_Car(Car):
    def drive(self):
        print(f'Sending {self.status} foto {self.brand} with {self.number}')

class Truck(Car):
    def drive(self, color):
        print(f'Sending {self.status} foto {self.brand} {color} with {self.number}')

hundai = Car("hundai","AX12345")
hundai.drive()
nissan = Passenger_Car("nissan","AX54678")
nissan.drive()
vaz = Truck("vaz","AX55678")
vaz.drive("red")

