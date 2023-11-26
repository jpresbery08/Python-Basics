#Name Jermaine Presbery
# File: convert_temp.def # This program converts temperatures in C to F
# This program converts temperatures in C to F


def main():
    #Get user input
    print()
    C = eval(input("What is the temperature mesaured in C: "))
    #Process Data
    F = (9.0/5.0) * C + 32.0
    # Return Output Data
    print()
    print("The temperature", C , "Celcius is equal to", F , "Fahrenheit.")
    print()
main()
