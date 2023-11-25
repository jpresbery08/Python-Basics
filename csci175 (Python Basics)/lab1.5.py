#Name: Jermaine Presbery
#Assignment: lab1.5.py
#Date: 09/15/2020


def main():

    #Asking for user to input any Amount of money
    user = eval(input("Enter in any amount of money: "))



    dollars = user // 1.0
    dol = user % 1.0
    print("Dollars: ", dollars)
    print("")

    quarters = dol // .25
    qua = dol % .25
    print("Quarters: ", quarters)
    print("")



    dimes = qua // .10
    dim = qua % .10
    print("Dimes: ", dimes)
    print("")

    nickles = dim // .05
    nic = dim % .05
    print("Nickles: ", nickles)
    print("")


    pennies = nic // .01
    print("Pennies: ", pennies)
    print("")

    print("Your total is: $", user)








main()
