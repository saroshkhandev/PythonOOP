"""
_singleunderscore - "weak" internal use indicator or we can say partially private

__doubleunderscore -  private can be used inside the parameters of declaration
"""
class Sarosh:
    def __init__(self):
        self.x = 10
        self._y = 20
        self.__z = 30
    
    def public_method(self):
        print(self.x)
        print(self._y)
        print(self.__z)
        self.__private_method()
    
    def __private_method(self):
        print(self.__z, "Working")

s = Sarosh()
s.public_method()