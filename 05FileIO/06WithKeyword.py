# With keyword close the file by default

with open("05FileIO/sample.txt", "r") as f:
    data=f.read()
    print(data)
    print(len(data))