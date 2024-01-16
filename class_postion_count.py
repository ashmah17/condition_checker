
Amina = 0
Zainab = 0
Halimatu = 0
Maryam = 0

# subjects = 4

for i in range (1, 4):
    print(f"Subject  {i} is")

    Amina = int(input("\n Write Amina's Score "))
    Zainab = int(input("\n Write Zainab's Score "))
    Halimatu = int(input("\n Write Halimatu's Score "))
    Maryam = int(input("\n Write Maryam's Score "))


    students = {
       'Amina' : Amina,
       'Zainab' : Zainab, 
       'Halimatu' : Halimatu, 
       'Maryam' : Maryam 
    }

    highest_score = max (students, key=students.get)


    if students[highest_score] >= 4 and all (students[highest_score] >=  vote for vote in students.values()):

        print(f"{highest_score} is the overaller of the with {students[highest_score]} scores")
    else:
        print("No student meets the requirements")