students = ["Akash", "Rahul", "Priya", "John"]
subjects = ["Python", "Maths", "Physics"]

marks = [
    [80, 75, 85],
    [65, 70, 60],
    [90, 95, 88],
    [50, 55, 60]
]

for i in range(len(students)):
    total = sum(marks[i])
    average = total / len(subjects)

    print("\nStudent:", students[i])
    print("Total Marks:", total)
    print("Average:", average)

for j in range(len(subjects)):
    total = 0

    for i in range(len(students)):
        total += marks[i][j]

    average = total / len(students)
    print(subjects[j], "Average:", average)
