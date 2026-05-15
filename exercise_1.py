import csv

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

# --- Save student data to CSV ---
with open("students.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "name", "score"])
    writer.writeheader()
    writer.writerows(students)

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

# --- Load student data back from CSV (optional) ---
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    loaded_students = list(reader)

print("\nLoaded from file:")
for s in loaded_students:
    print(s)
