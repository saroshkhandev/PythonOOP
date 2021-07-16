# def function_name_print(a, b, c, d):
#     print(a, b, c, d)

# function_name_print("Sarosh", "Faraz", "Atiq", "Sabiha")

def funargs(owner, *args, **kwargs):
    print("Normal Arguments")
    print(owner)
    print("Printing arguments (*args)")
    for name in args:
        print(name)
    print("Printing **kwargs")
    for key, value in kwargs.items():
        print(f"{key} is a {value}")

names = ["Sarosh", "Faraz", "Atiq", "Sabiha"]
owner = "sarosh1"
kw = {"Sarosh": "Programmer", "Faraz": "Doctor", "Daddy": "Advocate"}

funargs(owner, *names, **kw)
