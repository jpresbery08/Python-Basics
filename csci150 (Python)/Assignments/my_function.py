#Name: Jermaine Presbery
#File Name my_function.property.py
#This file is the mod_file for dollar_cents_4.py



def dollars_val():
    #Get user input
	money = eval(input("Please enter a monetary value: "))

	#Convert to cents
	cents = money * 100


	#Calculate change
	Hundreds = cents // 10000
	cents = cents % 10000

	Fifties = cents // 5000
	cents = cents % 5000

	Twenties = cents // 2000
	cents = cents % 2000

	Tens = cents // 1000
	cents = cents % 1000

	Fives = cents // 500
	cents = cents % 500

	Ones = cents // 100
	cents = cents % 100

	Quarters = cents // 25
	cents = cents % 25

	Nickels = cents // 5
	cents = cents % 5

	Dimes = cents // 10
	cents = cents % 10

	Pennies = cents // 1
	cents = cents % 1
	#Print results to screen

	print("Hundreds: ", Hundreds)
	print("Fifties: ",Fifties)
	print("Twenties: ",Twenties)
	print("Tens: ", Tens)
	print("Fives: ", Fives)
	print("Ones: ", Ones)
	print("Quarters: ", Quarters)
	print("Dimes: ", Dimes)
	print("Nickels: ", Nickels)
	print("Pennies: ", Pennies)

	#Calulate/print checksum
	checksum = (Hundreds * 100) + (Fifties*50) + (Twenties*20) + (Tens*10) + (Fives*5) + (Ones*1) + (Quarters*.25) + (Dimes*.10) + (Nickels*.05) + (Pennies*.01)
	print(checksum)
	print("The user entered $ ", money, ". You caluclated $ ", checksum,'.')

#It may be off a penny because of calucation above


dollars_val()


def dollars_list():
# --------------------- Get User Input --------------------- #
    print()
    money = eval(input("Enter im a momentary values(BE SURE TO ENTER A COMMA AFTER EVERY VALUE !!!)"))
    print()
# -------------------- Calculate Change -------------------- #
# Convert to cents
    cents = int(money * 100)
# Create empty list of denomination amounts
    change_nums = []
# Create list of denomination values in dollars
    change_vals = [100.00, 50.00, 20.00, 10.00, 5.00, 1.00, 0.25, 0.10, 0.05, 0.01]
# Create list of denomination names
    change_names = ["Hundreds", "Fifties", "Twenties", "Tens", "Fives", "Ones", "Quarters", "Dimes", "Nickels", "Pennies"]
# Calculate exact change
    for i in :
        change_nums.append()
        cents = cents % change_vals
# --------------- Print Results and Checksum --------------- #
# Initialize variable
checksum = 0
    for loop_index in :
        print()
        checksum =

    print()
    print("The user entered $", money, ". You calculated $", checksum, ".")
    print()

dollars_list()
