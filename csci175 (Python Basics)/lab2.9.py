import math

def main():
    n = int(input("Enter in the number of terms you want to add too "))
    sum = 0
    pie = math.pi

    for i in range(0, n):
        sum = sum + (4/(2(n)+1)) * (-1)**n
        dif = pie - sum #"Enter SUM of Numbers Here"
        print("The Difference is: ",  dif )

main()
