def main():
    y = eval(input("Enter in the amount of numbers: "))
    sum = 0
    for i in range(0,y):
        x = eval(input("Enter a number:  "))
        sum = sum + x
        print(sum)

main()
