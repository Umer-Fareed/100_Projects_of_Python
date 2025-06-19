#Dictionary Comprehension
#new_dict= {new_key:new_value for (key,value) in dict.item() if item}
import random
names= ["umar" , "adeel", "haroon", "maan", "sayam"]
# student_Score= {
#     "umar": 64,
#     "adeel": 89,
#     "haroon": 87,
#     "maan": 98,
#     "sayyam": 67
# }
students_score= {student:random.randint(1,100) for student in names}
print(students_score)

passed_students= {student:score for(student,score) in students_score.items() if score >= 40}
print(passed_students)
