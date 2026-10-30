students = ["Akash", "Rahul", "Priya"]

marks = [
    [65, 70, 80],
    [80, 75, 70],
    [45, 50, 55]
]

for i in range(len(students)):
    average = sum(marks[i]) / len(marks[i])
    improvement = marks[i][-1] - marks[i][0]

    print("\nStudent:", students[i])
    print("Average Marks:", average)
    print("Improvement:", improvement)

    if average >= 75:
        print("Performance: Excellent")
    elif average >= 50:
        print("Performance: Average")
    else:
        print("Performance: Needs Improvement")
