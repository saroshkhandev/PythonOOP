result = None
x = int(input("Number 1: "))
y = int(input("Number 2: "))

try:
    result = x / y

except Exception as e: # Exception is the base class for all the exceptions
    print(type(e))

else:
    print("Inside Else")

finally:
    print("Inside Finally")

print("---New Line---")
print("Result: ", result)
