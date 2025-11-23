"""
Q4. Given a tuple of integers, create:
• A tuple of all even numbers
• A tuple of all odd numbers
"""

# nums = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# even_nums = tuple(n for n in nums if n % 2 == 0)
# odd_nums = tuple(n for n in nums if n % 2 != 0)

# print("Even:", even_nums)
# print("Odd:", odd_nums)


"""
Q5. Create a dictionary where:
• Keys = student names
• Values = marks (integer)
Write a menu-based program where user presses a key (ʼAʼ, ‘Bʼ, ‘Cʼ, ‘Dʼ) depending on
the operation they want to perform on the dictionary:"""

# data = {}

# user = input("Enter the Operation: A (Add), U (Update), S (Search), D (Delete), Q (Quit): ")

# while user.lower() != "q":

#     if user.lower() == "a":
#         student = input("Enter student name: ")
#         marks = int(input("Enter marks: "))
#         data[student] = marks
#         print("Added:", data)

#     elif user.lower() == "u":
#         student = input("Enter student name to update: ")
#         if student in data:
#             marks = int(input("Enter new marks: "))
#             data[student] = marks
#             print("Updated:", data)
#         else:
#             print("Student not found!")

#     elif user.lower() == "s":
#         student = input("Enter student name: ")
#         if student in data:
#             print(f"The marks of {student} is {data[student]}")
#         else:
#             print("Student not found!")

#     elif user.lower() == "d":
#         student = input("Enter student name to delete: ")
#         if student in data:
#             del data[student]
#             print("Deleted:", data)
#         else:
#             print("Student not found!")

#     else:
#         print("Invalid Input")

#     # 🔄 Ask again for next operation
#     user = input("\nEnter A/U/S/D or Q to quit: ")

# print("Program Ended")


"""
Q6. Given a list of words:
Create a dictionary that maps each word to its length."""

# words = ["apple", "banana", "kiwi", "cherry", "mango"]
# dict={}
# for word in words:
#     dict[word]=len(word)
# print(dict)

"""
Q9. Given a list, print all elements that appear more than once in the list.
[Hint - use sets]"""

nums = [1, 2, 3, 2, 4, 5, 1, 6, 3, 3]

seen=set()
duplicates=set()

for n in nums:
    if n not in seen:
        seen.add(n)
    else:
        duplicates.add(n)

print("Repeated elements:", duplicates)