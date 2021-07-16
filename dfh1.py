fh = open("C:\\Users\\lumia\\PythonLearn\\File\\Example.txt", "w")
#we use \\ because \U \l \F does mean something in python

for i in range(1, 11):
    fh.write("Line: %d \n" %i)

fh.close()