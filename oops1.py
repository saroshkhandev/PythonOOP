class Speed:
    def __init__(self):
        self.__speed = 10
    def get_speed(self):
        return self.__speed
    def set_speed(self, new_speed):
        self.__speed = new_speed
    def doubleSpeed(self):
        self.__speed = self.__speed * 2
    
    
s = Speed()
print(s.get_speed())
s.set_speed(100)
print(s.get_speed())
s.doubleSpeed()
print(s.get_speed())

# __ two underscore before any variable name makes it private and can be accessed through that particular
#class only, Note: we cant access that variable outside the class, but we can modify its value
# so in order to restrict its modification we use getter and setter
