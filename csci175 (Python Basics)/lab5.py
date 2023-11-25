

def main():
    # User Key input
    key = eval(input("Please enter in a number key"))

    # User Message Input
    message = input("Enter in a Message to be Encrpted: ")

    #Prints out the unicode values
    print("Here are the unicode values: ")

    for char in message:
        print((ord(char) + key), end = " ")

    print("Here's the orignal: ", message)
    print()

main()
