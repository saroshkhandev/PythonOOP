class Parent:
    def __init__(self, name):
        print("Parent __init__ ", name)

class Parent2:
    def __init__(self, name):
        print("Parent __init__ ", name)

class Child(Parent, Parent2):
    def __init__(self):
        print("Child __init__")
        super().__init__("Sarosh")
        Parent2.__init__(self, "John")

child_obj = Child()
print(Child.__mro__)
