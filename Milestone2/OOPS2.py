#single inheritance
class Vehicle:
    __current_year = 2023
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.__year = year
    def __str__(self):
        return "This is a Vehicle class"
    def __print_hello(self):
        print("hello from private")
    def get_current_year(self):
        print('get current year from parent')
        return Vehicle.__current_year #class attributes can be accessed only using class name
class Car(Vehicle):
    def __init__(self, make,model,year,air_conditioner,wheels):
        super(Car,self).__init__(make,model,year)
        
        self.air_conditioner =air_conditioner
        self.wheels=wheels
    def get_current_year(self): #method overriding
        print('get current year from child')
        Vehicle.current_year = 2024
        return Vehicle.current_year
    
obj6= Vehicle("hyundai","XUV",2022)
print(obj6) # type is Vehicle
print(obj6.__str__()) #type is string
obj5 = Car('Maruti','alto',2023,True,4)
obj5.__dict__
obj5._Vehicle__year #accessing private instance variable using class name workaround
obj3 = Car('Tesla','X7',2023,True,4)
print(obj3.get_current_year())
obj4 = Vehicle("Ford","petrol",2023) # calling the parent method using the object from the parent class
print(obj4.get_current_year())
print(obj4._Vehicle__current_year) # accessing the private class attribute using subclass object
obj = Car('Tesla','X7',2023,True,4)
obj2=Car('TATA','C7',2020,True,4)
obj.__dict__
obj.year =2022
obj.year
obj2.year
obj._Vehicle__print_hello()
# Python example to show the working of multiple inheritance

class Base1():
    def __init__(self):
        self.str1 = "Geek1"
        print("Base1")


class Base2():
    def __init__(self):
        self.str2 = "Geek2"
        print("Base2")


class Derived(Base1,Base2):
    def __init__(self):

        # Calling constructors of Base1
        # and Base2 classes
        Base1.__init__(self)
        Base2.__init__(self)
        print("Derived")

    def printStrs(self):
        print(self.str1, self.str2)


ob = Derived()
ob.printStrs()

class Account:
    def __init__(self,owner,balance):
        self.owner= owner
        self.balance = balance
    def __repr__(self):
        return f'Account ({self.owner!r},{self.balance!r})'
    def deposit(self,amount):;f;f;;;;;;;;ljk;;ljkjlkj;llkf;dkljlkdjlkj'
        self.balance +=amount
    def withdraw(self,amount):
        self.balance -= amount
    def inquiry(self):
        return self.balance
        
acc1 = Account('Vikas',10089)
acc1.inquiry()
acc1.__dict__
acc1.__repr__()
acc1.__repr__()
