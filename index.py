

student_name = str(input("Enter your name: \n"))
student_age = int(input("Enter your age: \n"))

for i in range(student_age):
    while student_age < 18:
        print(f"{student_name} will be {student_age} years old next year")
        student_age += 1