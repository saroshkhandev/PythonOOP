from square import Square
from triangle import Triangle

s1 = Square()
s1.set_value(10, 20)
s1.set_color("Red")
print(s1.area(), s1.get_color())

t1 = Triangle()
t1.set_color("Blue")
t1.set_value(11, 10)
print(t1.area(), t1.get_color())
