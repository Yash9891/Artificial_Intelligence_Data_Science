# Try, except, else, finally

try:
    x=int(input("Enter a num"))
    ans=10/x
except ZeroDivisionError:
    print("Divide not allowed")
else:
    print(f"ans= {ans}")
finally:
    print("Program is ended")