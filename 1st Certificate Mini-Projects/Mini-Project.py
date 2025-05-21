#Function to calculate the average grade
def totalGrade(finalGrade):
    average = sum(finalGrade) / len(finalGrade)
    return average

# Function to check if the student has passed or failed
def studentGradeFinal(name, grade):
    if grade >= 75:
        return "passed"
    else:
        return "failed"

#Prompt on How many Students can be entered
studentNo = int(input("Enter a Number of Students: "))
name = []
grade = []
passedList = []
failedList = []

#Input Loop based on the number of students
for i  in range(1,studentNo + 1):
    studentName = str.capitalize(input(f"Enter Student Name {i}: "))
    studentGrade = int(input(f"Enter {studentName}'s Grade: "))
    name.append(studentName)
    grade.append(studentGrade)

#Average Grade
finalAverage = totalGrade(grade)
print("Average Grade: ", finalAverage)

#Loop for each Student Grade
for i in range(studentNo):
    result = studentGradeFinal(name[i], grade[i])
    if result == "passed":
        passedList.append(name[i])
    else:
        failedList.append(name[i])

print("Passed Students: ", passedList[:])
print("Failed Students: ", failedList[:])
    