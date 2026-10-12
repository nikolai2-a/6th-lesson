# 2 zadanie
#
#def set_age(age):
#    if age < 0:
#        raise ValueErroe("out of range")


# 3 zadanie

#import logging
#except ConnectionError as e:
#    logging.error("ошибка сети")
#    raise ConnectionError("ошибка сети")
#
#except ConnectionError:
#    logging.error("ошибка сети")
#    raise


# 4 zadanie

#class BaseParser:
#    def parse(self, data):
#        raise NotImplementedError(
#            f"Класс {self.__class__.__name__} должен реализовать метод parse")


# 5 xadanie

#import json
#data = {"name": "Ivan",
#        "is_student": True,
#        "grades": [4, 5, 5]}
#json_string = json.dumps(data, ensure_ascii = False)
#
#parced_data = json.loads(json_string)


# 6 zadanie

#with open("data.json", "w", encoding = "utf-8") as f:
#    json.dump(data, f, indent = 4, ensure_ascii = False)

#with open("data.json", "r", encoding = "utf-8") as f:
#    loaded_data = json.load(f)
#print(loaded_data)

# 7 zadanie

#import json
#class Student:
#    def __init__(self, name, age):
#        self.name = name
#        self.age = age
#
#stud = Student("Петр", 19)
#def student_to_dict(obj):
#    if isinstance(obj, Student):
#        return {"name": obj.name, "age": obj.age, "type": "Student"}
#    raise TypeError("Unknown object type")
#
#json_str = json.dumps(stud, default = student_to_dict, ensure_ascii = False)
#print(json_str)


# 8 zadanie

import json

with open("students_db.json", "r", encoding = "utf-8") as f:
    students = json.load(f)

print("Активные студенты:")


for student in students:
    if student["is_active"]:
        print(student["name"])

for student in students:
    if not student["is_active"] and student["scholarship"] != 0:
        student["scholarship"] = 0
print(students)
        

