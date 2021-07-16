class Books:
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):
        return self.pages + other.pages
    
    def __mul__(self, other):
        return self.pages * other.pages

    def __gt__(self, other):
        return self.pages > other.pages
  
b1 = Books(100)
b2 = Books(150)

print(b1 + b2)  # b1.__add__(b2)
print(b1 * b2)  # b1.__mul__(b2)
print(b1 > b2)  # b1.__gt__(b2)
