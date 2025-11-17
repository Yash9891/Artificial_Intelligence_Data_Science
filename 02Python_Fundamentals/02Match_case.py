color=input("Enter color: ")

match color:
    case "Green":
        print("Go")
    case "Yellow":
        print("Ready")
    case "Red":
        print("Stop")
    case _:
        print("Blue")
    