class Car():
    def Benz(self):
        print("This is a Benz Car")
class Bike():
    def Bmw(self):
        print("This is a BMW Bike")
class Bus():
    def Volvo(self):
        print("This is a volvo Bus")
class Truck():
        def Eicher(self):
            print("This is a Eicher Truck")
class Plane():
    def Indigo(self):
        print("This is a Indigo plane")
class Transport(Car,Bike,Bus,Truck,Plane):
    def Main(self):
        print("This is the main class")
B=Transport()
B.Benz()
B.Bmw()
B.Volvo()
B.Eicher()
B.Indigo()
B.Main()
    