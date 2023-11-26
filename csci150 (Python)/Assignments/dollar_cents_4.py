#Name: Jermaine Presbery
#File Name: dollar_cents_4

import my_function

def main():
    num = eval(input("If you want to compute values using variables Enter the number '0'. If you want to compute values using lists Enter the number '1': "))

    if(num == 0):
        print("The computed value using a varaible is: ")
        result_val = my_function.dollars_val()
        print(result_val)
    elif(num == 1):
        print("The computed value using a list is: ")
        result_list = my_function.dollars_list()
        print(result_list)
    else:
        print("The value you entered is not valid.")

main()
