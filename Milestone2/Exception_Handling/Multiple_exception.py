#Handling Multiple Exceptions
class Vehicle():
    def __init__(self,make,model,fuel):
        self.make=make
        self.model=model
        self.fuel=fuel
    def get_value(self):
        try:
            age=2021-self.model
            return 1000*(1/age) 
        except TypeError:
            try:
                age=2021-int(self.model)
                return 1000*(1/age)
            except ZeroDivisionError:
                age=2021-int(self.model)
                return 1000*(2)  
            except:
                return "You Have entered Model year in incorrect format" 
        except ZeroDivisionError:
            age=2021-int(self.model)
            return 1000*(1)
  
