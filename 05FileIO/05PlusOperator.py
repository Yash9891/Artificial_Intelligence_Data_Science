#r+= read + write, w+ = write+read, a+ = append+read

# in read mode pointer is at first-----------------
f=open("05FileIO/sample.txt", "r+")
f.write("123")
data=f.read()
print(data)
f.close()

#in append mode pointer is at last (after appending 123)
# f=open("05FileIO/sample.txt", "a+")
# f.write("123")
# data=f.read() # we can not see anything in terminal beacuse pointer is at last 123 added at last and after that nothing is there to print
# print(data)
# f.close()

# for w+ also nothing will print it will overite -123 pointer at last nothing will print