#operator overloading
class Vehicle:
    def __init__(self,make,model,price):
        self.make=make
        self.model=model
        self.price=price
    def __str__(self):
        return "The Car is from {} and its price is {}".format(self.make,self.price)
    #overloading + operator
    def __add__(self,other):
        return self.price + other.price
    #overloading - operator
    def __sub__(self,other):
        return self.price - other.price
    
obj1 = Vehicle('Tesla',"Electric",40)
obj2 = Vehicle('Ford','Petrol',80)

print(obj1)
print(obj2)

print(obj1+obj2)
print(obj2-obj1)
