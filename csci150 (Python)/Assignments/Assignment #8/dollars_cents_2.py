#Name Jermaine Presbery
#File Name dollars_cents_2.py
#Asignment #7

# File Name: dollars_cents_2.py
# This code returns the number of bills and coins that sum to
# the value entered by a user.
def main():
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

main()
