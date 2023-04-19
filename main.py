# Python DA - 1
# Author - Sanjay Kumar B
# Last updated date - 21/10/21

# Calculate average mark

def cal_average():
    mark = []
    tot = 0
    for i in range(5):
        mark.insert(i, int(input("Enter subject marks: ")))
    for i in range(5):
        tot = tot + mark[i]
    average = tot / 5
    percentage = (tot / 500) * 100
    try:
        if average < 40:
            raise ValueError
        else:
            print(end="\nAverage Mark = ")
            print(average)
    except ValueError:
        print("The average mark is less than A Grade !!!")
    print(end="Percentage Mark = ")
    print(percentage)


# Check student department

def student_department():
    try:
        if dept == "CSE":
            raise ValueError
        else:
            print("Student is not belongs to CSE department !!!")
    except ValueError:
        print("Student is belongs to CSE department", dept)


dept = input("Enter the department: ")


# get student details

def student_details(name, age):
    print("Entered Student name:", name)
    try:
        if age < 15:
            raise ValueError
        else:
            print("Student age: ", age)
    except ValueError:
        print("Age is less than 15 !!!")


name = input("Enter the name: ")
age = int(input("Enter the age: "))
cal_average()
student_department()
student_details(name, age)
