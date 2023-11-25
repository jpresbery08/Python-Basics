#File Name: final.py



def main():

#Getting player one information

    player1 = str(input("Enter the player's last name: "))
    jersey1 = int(input("Enter the player's jersey number: "))

    if jersey1 > 0 or jersey1 < 99:
        print("")


    sum = 0
    for i in range(0,5):
        list1 = eval(input("Enter the player's total yards in game: "))
        sum = sum + list1
        player1_avg = sum / 5

# Getting player 2 information

    player2 = str(input("Enter the player's last name: "))
    jersey2 = int(input("Enter the player's jersey number: "))

    if jersey2 > 0 or jersey2 < 99:
        print("")

    sum2 = 0
    for i in range(0,5):
        list2 = eval(input("Enter the player's total yards in game: "))
        sum2 = sum2 + list2
        player2_avg = sum2 / 5


#Prints out best draft pick based on average
    print("Player number ", str(jersey1), player1 + "'s", "average yards per game was: ", player1_avg)
    print("Player number ", str(jersey2), player2 + "'s", "average yards per game was: ", player2_avg)
    if player1_avg > player2_avg:
        print(player1, " is the better draft pick.")
    else:
        print(player2, " is the better draft pick.")



main()
