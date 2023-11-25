def main():
    phrase = input("Enter in a phrase to recieve acronym: ")

    ac = phrase.split()
    first_letter = ''

    for char in ac:
        first_letter = first_letter + char[0].upper()

    print("Here is the Acronym for your phrase: ", first_letter)


main()
