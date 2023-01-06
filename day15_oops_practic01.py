class Vehical:
    speed=40
    def __init__(self,name,color,milage):
        self.name=name
        self.color=color
        self.milage=milage
class Bus(Vehical):
    pass
S_bus=Bus("school bus",'red',50)
print("vehical name: ",S_bus.name,
      "color is: ",S_bus.color,"milage is: ",S_bus.milage)    
        
