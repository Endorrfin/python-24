import my_gui

class Car:
    def __init__(self, **kw):
        self.make = kw['make']
        self.model = kw['model']

my_car = Car(make="Tesla", model="Model S")
print('🚘', my_car.make, my_car.model)



class Transport:
    def __init__(self, **kw):
        self.make = kw.get('make')
        self.model = kw.get('model')
        self.color = kw.get('colour')
        self.seats = kw.get('seats')

my_transport = Transport(make="Mercedes-Benz", model="atego 815", color='🟨 yellow', seats='3')
print('🚚', my_transport.make, my_transport.model, my_transport.color, my_transport.seats)
