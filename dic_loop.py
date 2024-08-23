# subject = {"computer":"54","math":"71","physics":"72"}
# #print(subject
# for key in subject.keys():
#   # print(subject[key])
#   print(f"your mark in {key} subject is ")
  
  
  
  
  
#   #wap to ask subject and their mark and print their percentage and division
# total_marks = 0 
# num_subject = 4
# subject = []

# for i in range(1,4):
#     subject = input("enter subject name: ")
#     marks = int(input(f"enter your marks in {subject} subject: "))

#     total_marks += marks
#     subject.append(f"{subject} {marks}")
    
# percentage = (total_marks/400)*100
     
# if percentage >= 80:
#   division = "first"
# elif percentage>= 70:
#   division = "second" 
# elif percentage >= 60:
#   division = "third"
# elif percentage >= 50:
#   division = "fourth"
# else:
#   division = "you should try harder"
 
# print(",".join(subject), end=",")
 
# print(f"your percentage is {percentage}%, and division is {division}")

  

# num_students = 2 
# num_subjects = 4  

# for _ in range(num_students):
#     student_name = input("Enter student's name: ")
#     total_marks = 0
#     subjects = []

#     for i in range(num_subjects):
#         subject = input("Enter subject name: ")
#         marks = int(input(f"Enter your marks for {subject}: "))
#         total_marks += marks
#         subjects.append(f"{subject} {marks}")

#     percentage = (total_marks / (num_subjects * 100)) * 100

#     if percentage >= 80:
#         division = "first"
#     elif percentage >= 70:
#         division = "second"
#     elif percentage >= 60:
#         division = "third"
#     elif percentage >= 50:
#         division = "fourth"
#     else:
#         division = "You should try harder!"

#     print(f"{student_name}: ", end="")
#     print(", ".join(subjects), end=", ")
#     print(f"and percentage is {percentage}%, and division is {division}.")

#     print()



list = ["math", "english","nepali"]

first_list = list[0]
second_list = list[2]

list.append("computer")

for list in list:
  print(list)
  
  
  
data = {"physics":"78","chemistry":"67","english":"75"} 
data["math"] = "71"
print(data)

math_score = data["math"]
print("Math score:", math_score)
data["chemistry"] = "68"
print(data)

for keys in data.keys():
  print(f"your score is {data}")



data = [{'name':"salman",'percentage':"45"}]

for student in data:
  if int(student['percentage']) < 45:
    print(f"{student['name']},you are fail")
  else:
    print(f"{student['name']},you are pass")


