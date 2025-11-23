# Dict= key value pair

info={
    "name":"Yash",
    "cgpa":9.2,
    "score":900,
    "games":["Pokimon", "Ninja"]

}

print(info["cgpa"])

print(info.keys())
print(info.values())
print(info.items())

# return value acc to key- it does not give error if not present
print(info.get("name2")) # None

# add new item in dis=ct
info["city"]="NCR"
info.update({"country":"Indimania"})
print(info)