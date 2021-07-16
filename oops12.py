class TeaHotException(Exception):
    def __init__(self, arg):
        self.msg = arg

class TeaColdException(Exception):
    def __init__(self, arg):
        self.msg = arg

class Tea:
    def __init__(self, temperature):
        self.__temperature =  temperature
    
    def drink_tea(self):
        if self.__temperature > 85:
            raise TeaHotException("Tea's too Hot")
        
        elif self.__temperature < 65:
            raise TeaColdException("Cold to drink")
        
        else:
            print("Tea's Ok to drink")
    
t1 = Tea(50)
t1.drink_tea()
