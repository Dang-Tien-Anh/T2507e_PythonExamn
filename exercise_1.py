n = int(input("Enter number of students: "))

students = []

for i in range(n):
    student_id = input("Enter student ID: ")
    name = input("Enter full name: ")
    score = float(input("Enter python score: "))
    students.append({
        "id": student_id,
        "name": name,
        "score": score
    })

print("\nAll students:")
for s in students:
    print(s)

def get_score(student):
    return student["score"]

highest = max(students, key=get_score)
print("\nHighest score:", highest)

avg = sum(s["score"] for s in students) / n
print("Average score:", avg)


passed = [s for s in students if s["score"] >= 5]
print("\nStudents who passed:")
for s in passed:
    print(s)
