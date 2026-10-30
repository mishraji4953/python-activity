timetable = [
    ("Monday", "9:00", "10:00", "Python"),
    ("Monday", "10:00", "11:00", "Maths"),
    ("Tuesday", "9:00", "10:00", "Physics"),
    ("Monday", "9:30", "10:30", "Chemistry")
]

for i in range(len(timetable)):
    for j in range(i + 1, len(timetable)):
        day1, start1, end1, subject1 = timetable[i]
        day2, start2, end2, subject2 = timetable[j]

        if day1 == day2:
            if start1 < end2 and start2 < end1:
                print("Timetable conflict:")
                print(subject1, "and", subject2)
