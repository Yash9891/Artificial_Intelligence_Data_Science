# Operations- Open , read and close

#If the file is in root folder then it is called as absolute path but here it is not absolute path

f=open("05FileIO/data.txt", "r")

#Read-----------------------------------
# data=f.read()

data=f.readline() # reading line by line (Pointer type concept)
print(data)
data=f.readline() # reading line by line
print(data)

f.close()

