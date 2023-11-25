#Jermaine Presbery
#Exam 1


import math

def main ():
    x = eval(input("Please enter how many numbers you'd like to calculate the standard deviation of: "))
    print("")
    sum = 0
    # m = 0

    # Prompting user to enter in numbers in order to recieve mean

    for i in range(0,x):
        num = eval(input("Enter a number: " ))
        sum = sum + num
        avg = sum / x
    print("")
    print("The mean is: ", avg)



    # Standard Deviation Part

    y = 0

    for i in range(0,x):
        num = eval(input("Enter a number: " ))
        dif = ((num - avg) * (num - avg))
        y = y + x

    std = math.sqrt(dif/(y - 1))
    print("")
    print("The sample standard deviation is: ", std)
main()
