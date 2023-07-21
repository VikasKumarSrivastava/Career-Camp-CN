class NegativeCarValue(Exception):
    def __init__(self,value,message="Negative value of the car"):
        self.value = value
        self.message=message
        super().__init__(self.message)
    def __str__(self):
        return f'{self.message}-->{self.value}'


class Vehicle():
    def __init__(self,make,model,fuel):
        self.make=make
        self.model=model
        self.fuel=fuel
        self.current_year=2023
    def get_value(self):
        age = self.current_year - self.model
        if age<0:
            raise NegativeCarValue(age)
        else:
            return 1000*(1/age)

myobj= Vehicle("Tesla",2025,"Electric")
myobj.get_value()
