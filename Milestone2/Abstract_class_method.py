from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def get_value(self):
        pass
class Car(Vehicle):
    def __init__(self,make,model,fare):
        self.make=make
        self.model=model
        self.fare=fare
    def get_value(self):
        return 1000*self.fare
myobj=Car('Tesla',2019,40)

from abc import ABC,abstractmethod
class TextReaderAbstract(ABC):
    def __init__(self,path,filename):
        self.path=path
        self.filename=filename
    @abstractmethod
    def get_path(self): #this is just a interface or a rule
        pass
    @abstractmethod
    def get_filename(self):
        pass
    
class TextReader(TextReaderAbstract):
#     def __init__(self): not allowed
#         pass
    def get_path(self):
        return self.path
    def get_filename(self):
        return self.filename
myobj=TextReader('user/demo/','sample.txt')

from abc import ABC,abstractmethod
class Bank(ABC):
    @abstractmethod
    def get_interest(self):
        pass
class HDFC(Bank):
    def get_interest(self):
        return 8.9
myobj1=HDFC()
