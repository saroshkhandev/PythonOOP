def shop(item, price):
    print("Item: ", item)
    print("Price: ", price)
    global z 
    z = price + 2

shop("Sugar", 50)
print(z)
#We can use variable outside the function also just by passing it as global variable
#like: global z
#      z = 10

# So this is the backend course which will help in making api's and backends of various sites