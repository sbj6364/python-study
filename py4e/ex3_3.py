score = float(input("Enter Score: "))
if score < 0.6:
    grade = 'F'
elif score < 0.7:
    grade = 'D'
elif score < 0.8:
    grade = 'C'
elif score < 0.9:
    grade = 'B'
elif score <= 1.0:
    grade = 'A'
print("Your grade is: ", grade)