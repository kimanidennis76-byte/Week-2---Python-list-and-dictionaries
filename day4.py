# Day 4
weekly_log = [
      {"day":    "Monday", "steps": 9200, "protocal": "OMAD"},
      {"day":   "Tuesday", "steps": 10500, "protocal": "2MAD"},
      {"day": "Wednesday", "steps":8800, "protocal": "OMAD"},
      {"day":  "Thursday", "steps": 11000, "protocal":"Autophagy Marathon"},
      {"day":    "Friday", "steps":7600, "protocal": "OMAD"}

]

total = 0

for log in weekly_log:
    print(log["day"], "|", log["steps"], "steps" "|", log["protocal"])  
    total += log["steps"]

average = total / len(weekly_log)
print()
print("Average steps:", average)


#Student and grade
students = [
     {"name": "Maina Maingi", "grade": "A"},
     {"name": "Xosa Millan", "grade": "B"},
     {"name": "Vila Rosa", "grade": "C"}
]

print("=============  STUDENT GRADES =================")
for student in students:
    print(f"{student['name']}:{student['grade']}")