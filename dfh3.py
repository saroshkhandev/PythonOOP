fh = open("demo.txt", "r")
kt = open("test.txt", "w")

kt.write(fh.readline())

fh.close()
kt.close()
