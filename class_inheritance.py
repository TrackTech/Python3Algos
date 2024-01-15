
from abc import ABC,abstractmethod

class Vehicle(ABC):
    def __init__(self,name,model,price):
        self.name = name
        self.model = model
        self.price = price

    def __str__(self):
        return "Vehicle name is--" + self.name
    
    @abstractmethod
    def service_schedule(self):
        pass

class Sedan(Vehicle):
    def service_schedule(self):
        print("Once in 6 months")

class Truck(Vehicle):
    def service_schedule(self):
        print("Once in 3 months")

if __name__=="__main__":
    try:
        v = Vehicle("GreenPeace","Subaru",20000)
        print("Did it work?")
    except Exception as e:
        print("Exception occured-",e)

    s1 = Sedan("GreenPeace","Subaru",20000)
    
    s1.service_schedule()

    t1 = Truck("Transformer","Tata",3000000)

    t1.service_schedule()
