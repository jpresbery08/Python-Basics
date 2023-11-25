#Lab 11 Sycracuse Sequence


def main():
    #Ask user to enter in Starting Value
    n = eval(input("Enter in starting value: "))

    print("The postive integer you entered: ", n)
    print()
    print("Syracuse sequence generated: ")
    print(str(n) + ",", end = " ")

    while n != 1:
        if n % 2 == 0:      #If x is even
            n = n // 2      #Using // for integer division prevents decimals
        else:
            n = 3*n + 1

        if n != 1:
            print(str(n) + ",", end = " ") #THis prints out the sequence on the same line with the end=
        else:
            print(1)

main()
