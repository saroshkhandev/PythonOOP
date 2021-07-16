fh = open("demo.txt", "r")

# Remember one thing about datafilehandling accessing files is based on cursor..
# the cursor will output data from the last position it was taken to.
# print(fh.read(3))#output first 3 characters.. 
# print(fh.readline())#gives output of the line in which cursor is
# print(fh.readlines())#gives output as an array of lines
# print(fh.readlines()[2])#Each line have different index value
# print(len(fh.readlines()[2]))#outputs the length of that particular line
for line in fh:
    # print(line.split(" "))# splits each word with respect to the spaces and outputs it as a string
    print(len(line.split(" ")))#outputs length of each array

fh.close()
