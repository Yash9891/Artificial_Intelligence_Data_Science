# Json Module- JavaScript object notation

import json

#convert json string to python object
# json_str='{"name":"Yash","Teacher":true}'
# py_obj=json.loads(json_str)
# print(type(json_str))
# print(type(py_obj))
# print(py_obj)

#convert python obj to json string
# py_ob={
#     "name":"Superman",
#     "correct":False
# }
# json_string=json.dumps(py_ob)
# print(type(json_string),json_string)


# If want to read from file json.load() - not use loads

# with open("05FileIO/data.json","r") as f:
#     py_obj=json.load(f)
#     print(type(py_obj), py_obj)


# If want to overwrite the json file with python obj use dump()

data={
    "Name":"Yash",
    "Co":True
}
with open("05FileIO/data.json","w") as f:
    json.dump(data,f,indent=4, sort_keys=True)
    