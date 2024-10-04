class Car:
    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

    def signal(self):
        return "Би-би!"

    def car(self):
        return self.mark , self.model , self.year

my_car = Car("Toyota", "Camry", 2022)
print(my_car.car())
print(my_car.signal())