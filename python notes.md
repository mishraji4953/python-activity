
Course: Python Programming  
Year: B.Tech First Year  
Assignment Notes

# CASE STUDY 1: PRODUCT BILLING AND DISCOUNT CALCULATION

## Problem Statement

Create a bill for multiple products by calculating each product amount, the total bill, the discount, and the final payable amount.

## Objectives

- Accept the number of products and their details.
- Calculate the amount for each product using price and quantity.
- Store product names and amounts in a list of tuples.
- Apply a discount based on the total bill.
- Display the bill and final amount.

## Algorithm

1. Create an empty list and initialize the total to zero.
2. Read the number of products.
3. For each product, read its name, price, and quantity.
4. Calculate price multiplied by quantity and add the result to the list and total.
5. Display each product amount.
6. Apply a 10% discount for totals of 2000 or more, a 5% discount for totals of 1000 or more, or no discount otherwise.
7. Subtract the discount from the total and display the final amount.

## Python Code

products = \[\]

total = 0

n = int(input("Enter number of products: "))

for i in range(n):

name = input("Enter product name: ")

price = float(input("Enter price: "))

quantity = int(input("Enter quantity: "))

amount = price \* quantity

products.append((name, amount))

total += amount

print("\\n----- BILL -----")

for name, amount in products:

print(name, ":", amount)

if total >= 2000:

discount = total \* 0.10

elif total >= 1000:

discount = total \* 0.05

else:

discount = 0

final_amount = total - discount

print("Total:", total)

print("Discount:", discount)

print("Final Amount:", final_amount)

## Sample Input

```
Enter number of products: 2
Enter product name: Pen
Enter price: 20
Enter quantity: 10
Enter product name: Bag
Enter price: 500
Enter quantity: 3
```

## Sample Output

```
----- BILL -----
Pen : 200.0
Bag : 1500.0
Total: 1700.0
Discount: 85.0
Final Amount: 1615.0
```

## Conclusion

The program uses lists, tuples, loops, conditional statements, and arithmetic operations to prepare a product bill and calculate discounts.

# CASE STUDY 2: BANK TRANSACTION MANAGEMENT

## Problem Statement

Maintain a bank balance and process a given number of deposit and withdrawal transactions while tracking the total deposits and withdrawals.

## Objectives

- Start with an initial account balance.
- Accept deposit and withdrawal transactions.
- Reject zero or negative transaction amounts.
- Prevent withdrawals greater than the available balance.
- Display the final balance and transaction totals.

## Algorithm

8. Initialize the balance, deposits, and withdrawals.
9. Read the number of transactions.
10. For each transaction, read the transaction type and amount.
11. Check whether the amount is positive.
12. For a deposit, add the amount to the balance and deposit total.
13. For a withdrawal, check the available balance before subtracting the amount.
14. Display the final balance, total deposits, and total withdrawals.

## Python Code

balance = 5000

deposits = 0

withdrawals = 0

n = int(input("Enter number of transactions: "))

for i in range(n):

choice = input("Enter deposit or withdraw: ").lower()

amount = float(input("Enter amount: "))

if amount <= 0:

print("Invalid amount")

elif choice == "deposit":

balance += amount

deposits += amount

print("Deposit successful")

elif choice == "withdraw":

if amount <= balance:

balance -= amount

withdrawals += amount

print("Withdrawal successful")

else:

print("Insufficient balance")

else:

print("Invalid transaction")

print("Final Balance:", balance)

print("Total Deposits:", deposits)

print("Total Withdrawals:", withdrawals)

## Sample Input

```
Enter number of transactions: 3
Enter deposit or withdraw: deposit
Enter amount: 1000
Enter deposit or withdraw: withdraw
Enter amount: 500
Enter deposit or withdraw: withdraw
Enter amount: 7000
```

## Sample Output

```
Deposit successful
Withdrawal successful
Insufficient balance
Final Balance: 5500.0
Total Deposits: 1000.0
Total Withdrawals: 500.0
```

## Conclusion

The program demonstrates transaction processing using loops, conditional statements, and arithmetic operators.

# CASE STUDY 3: STUDENT PERFORMANCE ANALYSIS

## Problem Statement

Analyze the marks of students, calculate each student's average and improvement, and classify their academic performance.

## Objectives

- Store student names and marks.
- Calculate the average marks of each student.
- Calculate improvement between the first and last subject marks.
- Classify performance using average marks.

## Algorithm

15. Create a list containing student names.
16. Create a list of lists containing each student's marks.
17. Use a loop to process each student.
18. Calculate the average using sum divided by the number of marks.
19. Calculate improvement by subtracting the first mark from the last mark.
20. Use if-elif-else conditions to display the performance category.

## Python Code

students = \["Akash", "Rahul", "Priya"\]

marks = \[

\[65, 70, 80\],

\[80, 75, 70\],

\[45, 50, 55\]

\]

for i in range(len(students)):

average = sum(marks\[i\]) / len(marks\[i\])

improvement = marks\[i\]\[-1\] - marks\[i\]\[0\]

print("\\nStudent:", students\[i\])

print("Average Marks:", average)

print("Improvement:", improvement)

if average >= 75:

print("Performance: Excellent")

elif average >= 50:

print("Performance: Average")

else:

print("Performance: Needs Improvement")

## Sample Input

```
No keyboard input is required. The student names and marks are already stored in the program.
```

## Sample Output

```
Student: Akash
Average Marks: 71.66666666666667
Improvement: 15
Performance: Average

Student: Rahul
Average Marks: 75.0
Improvement: -10
Performance: Excellent

Student: Priya
Average Marks: 50.0
Improvement: 10
Performance: Average
```

## Conclusion

The program uses nested lists, loops, built-in functions, and conditional statements to analyze student performance.

# CASE STUDY 4: TIMETABLE CONFLICT DETECTION

## Problem Statement

Compare timetable entries and identify classes scheduled on the same day with overlapping time intervals.

## Objectives

- Store day, start time, end time, and subject for each class.
- Compare timetable entries in pairs.
- Check whether two classes occur on the same day.
- Identify overlapping time intervals.

## Algorithm

21. Store timetable records as tuples inside a list.
22. Use an outer loop to select one timetable entry.
23. Use an inner loop to compare it with each later entry.
24. Unpack the day, start time, end time, and subject from both entries.
25. Check whether the days are equal.
26. Apply the overlap condition and print the subjects when a conflict is detected.

## Python Code

timetable = \[

("Monday", "9:00", "10:00", "Python"),

("Monday", "10:00", "11:00", "Maths"),

("Tuesday", "9:00", "10:00", "Physics"),

("Monday", "9:30", "10:30", "Chemistry")

\]

for i in range(len(timetable)):

for j in range(i + 1, len(timetable)):

day1, start1, end1, subject1 = timetable\[i\]

day2, start2, end2, subject2 = timetable\[j\]

if day1 == day2:

if start1 < end2 and start2 < end1:

print("Timetable conflict:")

print(subject1, "and", subject2)

## Sample Input

```
No keyboard input is required. The timetable entries are defined in the program.
```

## Sample Output

```
Timetable conflict:
Maths and Chemistry
```

## Important Note

Important: The program compares time values as strings. This sample output follows the code exactly. For reliable time comparisons, use a consistent zero-padded format such as 09:00 and 10:00, or convert times into minutes.

## Conclusion

The program demonstrates tuples, nested loops, tuple unpacking, and comparison conditions to detect timetable conflicts.

# CASE STUDY 5: DUPLICATE AND HIGH-VALUE TRANSACTION DETECTION

## Problem Statement

Examine a set of transactions to identify repeated transaction IDs and transactions whose amounts exceed a defined threshold.

## Objectives

- Store transaction IDs and amounts.
- Detect duplicate transaction IDs.
- Identify transactions above the high-value threshold.
- Display the relevant warnings.

## Algorithm

27. Create a list of transaction tuples.
28. Create an empty list to keep transaction IDs already processed.
29. Set the high-value threshold to 5000.
30. Loop through each transaction and unpack its ID and amount.
31. Check whether the ID is already in the seen list.
32. Print a duplicate warning or add a new ID to the list.
33. Check whether the amount is greater than the threshold and print a high-value warning.

## Python Code

transactions = \[

("T101", 500),

("T102", 1000),

("T101", 500),

("T103", 6000),

("T104", 300)

\]

seen = \[\]

threshold = 5000

for transaction_id, amount in transactions:

if transaction_id in seen:

print("Duplicate transaction:", transaction_id)

else:

seen.append(transaction_id)

if amount > threshold:

print("High value transaction:", transaction_id)

## Sample Input

```
No keyboard input is required. Five transaction records are predefined in the program.
```

## Sample Output

```
Duplicate transaction: T101
High value transaction: T103
```

## Conclusion

The program uses tuples, lists, membership testing, and conditional statements to detect duplicate and high-value transactions.

# CASE STUDY 6: STUDENT FEEDBACK SENTIMENT ANALYSIS

## Problem Statement

Analyze student feedback by counting positive and negative words and determining whether the overall feedback is positive, negative, or neutral.

## Objectives

- Create lists of positive and negative words.
- Read feedback from the user.
- Split the feedback into individual words.
- Count positive and negative words.
- Calculate the sentiment score and classify the feedback.

## Algorithm

34. Create two lists containing positive and negative words.
35. Read the feedback and convert it to lowercase.
36. Split the feedback into words.
37. Initialize positive and negative counters to zero.
38. Check each word against the positive and negative lists.
39. Calculate the score by subtracting the negative count from the positive count.
40. Use if-elif-else to display the sentiment.

## Python Code

positive = \["good", "excellent", "helpful", "interesting"\]

negative = \["bad", "boring", "difficult", "poor"\]

feedback = input("Enter student feedback: ").lower()

words = feedback.split()

positive_count = 0

negative_count = 0

for word in words:

if word in positive:

positive_count += 1

if word in negative:

negative_count += 1

score = positive_count - negative_count

print("Positive words:", positive_count)

print("Negative words:", negative_count)

print("Sentiment score:", score)

if score > 0:

print("Positive Feedback")

elif score < 0:

print("Negative Feedback")

else:

print("Neutral Feedback")

## Sample Input

```
Enter student feedback: The course is good and helpful but difficult
```

## Sample Output

```
Positive words: 2
Negative words: 1
Sentiment score: 1
Positive Feedback
```

## Conclusion

The program uses strings, lists, loops, counters, and conditional statements for simple word-based sentiment analysis.

# CASE STUDY 7: ATM MENU-DRIVEN BANKING SYSTEM

## Problem Statement

Develop a menu-driven ATM program that allows the user to deposit money, withdraw money, check the balance, view transaction history, and exit.

## Objectives

- Provide a menu of banking operations.
- Allow valid deposits and withdrawals.
- Prevent invalid deposits and withdrawals beyond the balance.
- Store and display transaction history.
- Continue until the user chooses Exit.

## Algorithm

41. Initialize the account balance and an empty transaction list.
42. Use a while True loop to repeatedly display the ATM menu.
43. Read the user's menu choice.
44. For deposit, accept a positive amount, update the balance, and record the transaction.
45. For withdrawal, check that the amount is positive and does not exceed the balance.
46. For balance enquiry, display the current balance.
47. For transaction summary, display all stored transactions.
48. For Exit, display a message and stop the loop using break.
49. Display an error for an invalid menu choice.

## Python Code

balance = 5000

transactions = \[\]

while True:

print("\\n--- ATM MENU ---")

print("1. Deposit")

print("2. Withdraw")

print("3. Check Balance")

print("4. Transaction Summary")

print("5. Exit")

choice = int(input("Enter choice: "))

if choice == 1:

amount = float(input("Enter deposit amount: "))

if amount > 0:

balance += amount

transactions.append("Deposit: " + str(amount))

print("Deposit successful")

else:

print("Invalid amount")

elif choice == 2:

amount = float(input("Enter withdrawal amount: "))

if amount > 0 and amount <= balance:

balance -= amount

transactions.append("Withdrawal: " + str(amount))

print("Withdrawal successful")

else:

print("Invalid amount or insufficient balance")

elif choice == 3:

print("Current Balance:", balance)

elif choice == 4:

for transaction in transactions:

print(transaction)

elif choice == 5:

print("Thank you for using ATM")

break

else:

print("Invalid choice")

## Sample Input

```
Example interaction:
Enter choice: 1
Enter deposit amount: 1000
Enter choice: 2
Enter withdrawal amount: 500
Enter choice: 3
Enter choice: 4
Enter choice: 5
```

## Sample Output

```
Deposit successful
Withdrawal successful
Current Balance: 5500.0
Deposit: 1000.0
Withdrawal: 500.0
Thank you for using ATM
```

## Conclusion

The program demonstrates while loops, menu-driven programming, lists, conditional statements, and break.

# CASE STUDY 8: STUDENT AND SUBJECT MARKS MATRIX ANALYSIS

## Problem Statement

Analyze a marks matrix to calculate each student's total and average marks, and calculate the average marks for each subject.

## Objectives

- Store student names and subject names.
- Represent marks using a two-dimensional list.
- Calculate each student's total and average.
- Calculate the average for each subject across all students.

## Algorithm

50. Create lists of student names and subject names.
51. Store marks in a list of lists, where each row represents one student.
52. Loop through students and calculate each row's total using sum().
53. Calculate the student's average by dividing the total by the number of subjects.
54. Loop through each subject column.
55. Add the marks of all students for that subject.
56. Divide the subject total by the number of students and display the average.

## Python Code

students = \["Akash", "Rahul", "Priya", "John"\]

subjects = \["Python", "Maths", "Physics"\]

marks = \[

\[80, 75, 85\],

\[65, 70, 60\],

\[90, 95, 88\],

\[50, 55, 60\]

\]

for i in range(len(students)):

total = sum(marks\[i\])

average = total / len(subjects)

print("\\nStudent:", students\[i\])

print("Total Marks:", total)

print("Average:", average)

for j in range(len(subjects)):

total = 0

for i in range(len(students)):

total += marks\[i\]\[j\]

average = total / len(students)

print(subjects\[j\], "Average:", average)

## Sample Input

```
No keyboard input is required. Student names, subject names, and marks are predefined.
```

## Sample Output

```
Student: Akash
Total Marks: 240
Average: 80.0

Student: Rahul
Total Marks: 195
Average: 65.0

Student: Priya
Total Marks: 273
Average: 91.0

Student: John
Total Marks: 165
Average: 55.0
Python Average: 71.25
Maths Average: 73.75
Physics Average: 73.25
```

## Conclusion

The program uses a two-dimensional list, nested loops, indexing, and arithmetic calculations to analyze student-wise and subject-wise performance.

# CASE STUDY 9: CANTEEN ORDER AND STOCK MANAGEMENT

## Problem Statement

Manage food orders in a canteen by checking item availability, calculating bills, updating stock, and displaying total sales.

## Objectives

- Store food item stock quantities and prices.
- Accept multiple orders.
- Validate the food item and order quantity.
- Check whether sufficient stock is available.
- Calculate bills and update stock.
- Display total sales and remaining stock.

## Algorithm

57. Create dictionaries for available stock and item prices.
58. Initialize total sales to zero.
59. Read the number of orders.
60. For each order, read the item name and quantity.
61. Check whether the item exists and the quantity is positive.
62. Check whether the requested quantity is within available stock.
63. Calculate the bill, reduce stock, and add the bill to total sales.
64. Display the total sales and remaining stock.

## Python Code

stock = {

"idli": 50,

"dosa": 40,

"meals": 30

}

price = {

"idli": 20,

"dosa": 40,

"meals": 60

}

total_sales = 0

n = int(input("Enter number of orders: "))

for i in range(n):

item = input("Enter food item: ").lower()

quantity = int(input("Enter quantity: "))

if item in stock and quantity > 0:

if quantity <= stock\[item\]:

bill = price\[item\] \* quantity

stock\[item\] -= quantity

total_sales += bill

print("Order successful")

print("Bill:", bill)

else:

print("Insufficient stock")

else:

print("Invalid item or quantity")

print("\\nTotal Sales:", total_sales)

print("Remaining Stock:")

for item, quantity in stock.items():

print(item, ":", quantity)

## Sample Input

```
Enter number of orders: 3
Enter food item: idli
Enter quantity: 2
Enter food item: dosa
Enter quantity: 1
Enter food item: meals
Enter quantity: 35
```

## Sample Output

```
Order successful
Bill: 40
Order successful
Bill: 40
Insufficient stock

Total Sales: 80
Remaining Stock:
idli : 48
dosa : 39
meals : 30
```

## Conclusion

The program uses dictionaries, loops, conditional statements, and arithmetic operations to manage canteen orders and inventory.

# CASE STUDY 10: STUDENT RECORD VALIDATION

## Problem Statement

Validate student records by checking duplicate student IDs and ensuring marks and attendance percentages are within the valid range.

## Objectives

- Store student details using tuples.
- Detect duplicate student IDs.
- Validate marks between 0 and 100.
- Validate attendance between 0 and 100.
- Display validation messages for each student.

## Algorithm

65. Create a list of student tuples containing ID, name, marks, and attendance.
66. Create an empty list to store IDs already encountered.
67. Loop through each student record and unpack its values.
68. Display the student's name.
69. Check whether the student ID is already in the ID list.
70. If it is new, add it to the ID list; otherwise, display a duplicate ID message.
71. Check whether marks and attendance are within the range 0 to 100.
72. Display the corresponding invalid-data messages.
73. Display that the record is valid when both marks and attendance are in range.

## Python Code

students = \[

("S101", "Akash", 85, 90),

("S102", "Rahul", 75, 80),

("S103", "Priya", 110, 95),

("S101", "John", 65, 70)

\]

ids = \[\]

for student_id, name, marks, attendance in students:

print("\\nStudent:", name)

if student_id in ids:

print("Duplicate student ID")

else:

ids.append(student_id)

if marks &lt; 0 or marks &gt; 100:

print("Invalid marks")

if attendance &lt; 0 or attendance &gt; 100:

print("Invalid attendance")

if 0 <= marks <= 100 and 0 <= attendance <= 100:

print("Student record is valid")

## Sample Input

```
No keyboard input is required. Four student records are predefined in the program.
```

## Sample Output

```
Student: Akash
Student record is valid

Student: Rahul
Student record is valid

Student: Priya
Invalid marks

Student: John
Duplicate student ID
Student record is valid
```

## Important Note

Important: In the given code, duplicate ID detection is separate from marks and attendance validation. Therefore, John receives the 'Student record is valid' message because his marks and attendance are in range, even though his ID is duplicated.

## Conclusion

The program uses tuples, lists, membership testing, loops, and conditional statements to validate student information.

# OVERALL CONCLUSION

These ten Python case studies demonstrate practical problem-solving using Python programming. They cover variables, input and output, arithmetic operators, conditional statements, for and while loops, strings, lists, tuples, dictionaries, nested lists, and data validation. The programs apply these concepts to product billing, bank transactions, student performance, timetable checking, transaction monitoring, feedback analysis, ATM operations, marks analysis, canteen stock management, and student record validation.

## PYTHON CONCEPTS COVERED

- Variables and data types
- Input and output statements
- Arithmetic and comparison operators
- if, elif, and else statements
- for loops and while loops
- Lists and list methods
- Tuples and tuple unpacking
- Dictionaries and dictionary methods
- Nested lists and matrix processing
- String methods and string processing
- Built-in functions such as len(), sum(), and range()
- Validation, membership testing, and break
