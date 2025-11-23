info=[
    ("Alice","Math"),
    ("Bob","Science"),
    ("Alice","Science"),
    ("Charlie","Math"),
    ("Bob","Math"),
    ("Alice","English"),
    ("Charlie","English"),
    
]

# List unique course
unique_course=set()
for el in info:
    unique_course.add(el[1])
print(unique_course)

# list student enroll in eng
for name, course in info:
    if course=="English":
        print(name)


# create dict (students, set of courses)
Stu_dict={}
for name, course in info:
    if name not in Stu_dict:
        Stu_dict[name]={course}  # create a new set
    else:
        Stu_dict[name].add(course) #  add to existing set
print(Stu_dict)
        
