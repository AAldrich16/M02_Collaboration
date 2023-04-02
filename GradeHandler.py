## @Name: GradeHandler.py
## @Author: Anthony Aldrich
## @Description: A python program that checks a students GPA to see if they qualify for Deans List or Honor Roll.

while True:

    ## lastName, firstName store the users name by using the "input" function to get a input from the user
    lastName = input("Enter students last name or ZZZ to quit: ")
    if lastName == "ZZZ": ## If user enters ZZZ the program ends.
        break
    firstName = input("Enter students first name: ")
    GPA = float(input("Enter Students GPA: ")) ## User enters a float as a GPA

    if GPA >= 3.5:
        print(firstName, lastName, " has achieved Deans List")
    elif GPA >= 3.25:
        print(firstName, lastName, "has achieved Honor Roll")
    else:
        print("this student has not achieved Dean's list OR Honor Roll.")