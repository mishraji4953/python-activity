students = [
    ("S101", "Akash", 85, 90),
    ("S102", "Rahul", 75, 80),
    ("S103", "Priya", 110, 95),
    ("S101", "John", 65, 70)
]

ids = []

for student_id, name, marks, attendance in students:

    print("\nStudent:", name)

    if student_id in ids:
        print("Duplicate student ID")
    else:
        ids.append(student_id)

    if marks < 0 or marks > 100:
        print("Invalid marks")

    if attendance < 0 or attendance > 100:
        print("Invalid attendance")

    if 0 <= marks <= 100 and 0 <= attendance <= 100:
        print("Student record is valid")
