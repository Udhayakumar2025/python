#Convert Python → JSON
import json

student = {
    "name":"Udhaya",
    "age":23
}

json_data = json.dumps(student)

print(json_data)

#JSON → Python
import json

student = {
    "name":"Udhaya",
    "age":23
}

json_data = json.dumps(student)

print(json_data)

#Save JSON File
import json

student = {
    "name":"Udhaya",
    "age":23
}

with open("student.json","w") as file:
    json.dump(student,file)

#Read JSON File
import json

with open("student.json","r") as file:
    data = json.load(file)

print(data)