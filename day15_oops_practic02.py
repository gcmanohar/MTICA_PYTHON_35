class Vehical:
    speed=40
    def __init__(self,name,color,milage):
        self.name=name
        self.color=color
        self.milage=milage

    def seating_capacity(self,capacity):
        return f'the seating capacity of a {self.name}\
                is {capacity} passengers' 
class Bus(Vehical):
    def seating_capacity(self,capacity=50):
        return super().seating_capacity(capacity=80)

S_bus=Bus("school bus",'red',50)
print("vehical name: ",S_bus.name,
      "color is: ",S_bus.color,"milage is: ",S_bus.milage,
      'and seating capacity',S_bus.seating_capacity())
