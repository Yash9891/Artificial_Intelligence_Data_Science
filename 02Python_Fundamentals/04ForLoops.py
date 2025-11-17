string = "This is good"
for i in range(0, len(string)):
    print(string[i] + "-", end="")
if "T" in string:
    print("Ohh")

# range(start, stop, step)

for i in range(1, 10, 2):
    print(i, end="")
