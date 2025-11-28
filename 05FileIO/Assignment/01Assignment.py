"""
Q1. Create a program that:
1. Opens a file "names.txt" in write mode
2. Writes 5 names (one per line) entered by the user
3. Then opens the same file in read mode and prints all names"""


# with open("05FileIO/Assignment/names.txt","w+") as f:
#     print("Enter 5 names (or 'q' to quit):")

#     count=0
#     while count<5:
#         user=input("Enter name: ")
#         if user=="q":
#             break
#         f.write(user+"\n")
#         count+=1
    
#     # Move cursor back to start to read the file
#     f.seek(0)

#     print("\n--- Names in File ---")
#     print(f.read())


"""
Q2. Create a program that:
1. Opens a file "log.txt" in append mode
2. Adds a new log entry (like "Program run successfully")
3. Opens the file in read mode and prints all logs
"""

# Q2 Solution

# # Step 1: Append a new log entry
# with open("05FileIO/Assignment/log.txt", "a") as f:
#     f.write("Program run successfully\n")

# # Step 2: Read and print all log entries
# with open("05FileIO/Assignment/log.txt", "r") as f:
#     print("--- Log Entries ---")
#     print(f.read()) 


"""
Q3. Create a program that:
1. Has a list of numbers: [5, 10, 15, 20, 25]
2. Uses a list comprehension to create a new list with only numbers greater
than 15
3. Prints the new list"""
 
# numbers = [5, 10, 15, 20, 25]
# nums=[x for x in numbers if x>15]
# print(nums)


"""Q4
"cities.json"
1. Then load the JSON and print each city and its population.
2. Ask the user for a new city & its population - update this info in the json
file."""

import json

file_path = "05FileIO/Assignment/cities.json"
