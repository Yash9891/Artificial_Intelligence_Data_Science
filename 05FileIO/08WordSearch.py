data=True
line=1
with open("05FileIO/Sample.txt", "r") as f:
    while data:
        data=f.readline()

        if "solved" in data:
            print(f"{line} : {data}")
            break
        line+=1
