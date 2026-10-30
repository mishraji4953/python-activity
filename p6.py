positive = ["good", "excellent", "helpful", "interesting"]
negative = ["bad", "boring", "difficult", "poor"]

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
