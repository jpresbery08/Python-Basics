#Name: Jermaine Presbery
#Date: 09-03-20
#File Name: lab1.py

#Program Details:


    #defines function called main
def average():
    print("Enter in five values to receive average: ")
    print("")
    num1 = eval(input("Enter in a value 1: "))
    num2 = eval(input("Enter in a value 2: "))
    num3 = eval(input("Enter in a value 3: "))
    num4 = eval(input("Enter in a value 4: "))
    num5 = eval(input("Enter in a value 5: "))
    print("")
    sum = num1 + num2 + num3 + num4 + num5

    avg = sum / 5
    print("The Average is: ", avg)

average()
