exam_points = {
    "Mariusz": 30,
    "Mateusz": 55,
    "Marta": 76,
    "Roman": 30,
    "Arleta": 59,
    "Adrian": 96,
    "Monika": 91,
    "Andrzej": 22,
    "Krzysztof": 83,
    "Krystyna": 93,
    "Piotr": 44,
    "Dawid": 10,
    "Agnieszka": 15
}
failed_students = []
top_students = []
best_student = ("", 0)

# assigning fails
for s, p in exam_points.items():
    if p < 45:
        failed_students.append(s)
    elif p > 90:
        top_students.append(s)

# checking for the best score
best_score = 0
student = " "
for s, p in exam_points.items():
    if p > best_score:
        best_score = p
        student = s
# assigning stats
best_student = (student, best_score)

# printing results

print(f"Students that has failed: \n{failed_students}")
print(f"Top students: \n{top_students}")
print(f"Best student: \n{best_student}")
