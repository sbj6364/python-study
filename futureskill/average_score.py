import random  as r

score = []
class_score = []
student = []
subject = []
for i in range(5):
    row = []
    subject.append(row)

for i in range(30):
    for j in range(5):
        score.append(r.randint(1, 100))
        subject[j].append(score[j])
    student.append(score)
    score = []

# print(subject)
# print(student)
ave_student = []
ave_subject = []
for row in student:
    ave_student.append(int(sum(row)/5))
for row in subject:
    ave_subject.append(int(sum(row)/30))
print(ave_subject)
print(ave_student)
