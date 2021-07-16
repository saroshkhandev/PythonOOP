result = None
x = int(input("Number 1: "))
y = int(input("Number 2: "))

try:
    result = x / y

# except Exception as e: # Exception is the base class for all the exceptions
#     print("Error with our code. ", e)
#     print(type(e))

except TypeError as e:  # TypeError is the class for all the TypeError 
    print("Inside TypeError", e)
    print(type(e))

except ZeroDivisionError as e: # ZeroDivisionError is the class for all Zero Division errors 
    print("Inside ZeroDivisionError", e)
    print(type(e))

print("---New Line---")
print("Result: ", result)
