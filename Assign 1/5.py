# Input marks for 6 subjects
marks = []
for i in range(1, 7):
    m = float(input(f"Enter marks for subject {i}: "))
    marks.append(m)


total = sum(marks)
average = total / 6
percentage = (total / 600) * 100   #subject is out of 100

# Determine grade
if percentage >= 85:
    grade = "Distinction"
elif percentage >= 70:
    grade = "First Division"
elif percentage >= 55:
    grade = "Second Division"
elif percentage >= 45:
    grade = "Third Division"
else:
    grade = "Fail"

# Display results
print(f"Total Marks = {total}")
print(f"Average Marks = {average:.2f}")
print(f"Percentage = {percentage:.2f}%")
print(f"Grade = {grade}")