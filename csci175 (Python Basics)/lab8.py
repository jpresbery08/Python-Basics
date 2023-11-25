#Sums

def sumN(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i
    print("The sum of first", n , "postive integers", "is", sum)


def sumCubeN(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + i**3
    print("The sum of Cubes for the first", n , "postive integers", "is", sum)


def main():
    n = eval(input("Enter in a postive integer: "))
    sumN(n)
    sumCubeN(n)






main()
