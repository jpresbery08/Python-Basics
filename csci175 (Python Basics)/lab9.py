def findAverage():
    paper_comp = input("Did you complete the paper? Enter Yes or No: ")
    if paper_comp == "yes" or paper_comp == "Yes":
        print()
    elif paper_comp == "no" or paper_comp == "No":
        print()
        print("Since you didn't complete the paper you didn't pass: ")
        print("Your average is a(n): 0")
        print("You earned a(n): F")
    else:
        print("Please enter a better response")


    print()

    n_grades = eval(input("Enter in the number of grades you have: "))

    sum = 0
    for i in range(0, n_grades):
        grades = eval(input("Enter each grade to receive average: "))
        sum = sum + grades
        avg = sum / n_grades



    if 90 <= avg < 100:
        print("Your average is a(n): ", avg)
        print("You earned a(n): A")
    elif 80 <= avg < 89:
        print("Your average is a(n): ", avg)
        print("You earned a(n): B")
    elif 70 <= avg < 79:
        print("Your average is a(n): ", avg)
        print("You earned a(n): C")
    elif 60 <= avg < 69:
        print("Your average is a(n): ", avg)
        print("You earned a(n): D")
    else:
        print("Your average is a(n): ", avg)
        print("You earned a(n): F")



def main():
    findAverage()


main()
