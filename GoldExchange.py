# GoldExchange.py
#
# Assignment 1
# CMPT 120
#
# Michael Chang
# June 15, 2018
#
# state the variable
amount_gold = 0     # Amount of gold the user have
emerald_coin = 0   # Emerald coin, worth 80 ounces of gold
sapphire_coin = 35  # Sapphire coin, worth 35 ounces of gold
ruby_coin = 10      # Ruby coin, worth 10 ounces of gold
amber_coin = 1      # Amber coin, worth 1 ounce of gold
left_over = 0       # Amount of left over as the original amount of gold subtract by emerald coin
left_over_2 = 0     # Amount of left over as the first left over amount of gold subtract by sapphire coin

# a warm welcome to the user
print("Welcome to the Gold Exchange Station!\n\n-------------\nProgram Input\n-------------\n")

# Ask the user to enter the amount of gold they have
amount_gold = int(input("Please, enter the amount of gold mined in ounces (integer): "))

print("\n-------------\nProgram Output\n-------------\n")

# if the amount of user's gold is equal to zero, the program will say "Sorry, Dude. Work harder next time. Good Luck!"
if amount_gold == 0:
    # Display the statement
    print("\tSorry, Dude. Work harder next time.\n\n--- Good Luck! ---")

# if the amount of user's gold is less than zero, the program will say "Come on. Be positive!"
elif amount_gold < 0:
    # Display the statement
    print("\tCome on...\n\n--- Be positive! ---")

# if the amount of user's gold is greater than zero, the program will do the calculation
elif amount_gold > 0:
    # The amount of emerald coin is the amount of user's gold divide from the amount of emerald's worth of gold 
    emerald_coin = (amount_gold//80)
   
    left_over = amount_gold - emerald_coin*80
    # The amount of Sapphire coin is the amount of the left over divide from the amount of emerald's worth of gold 
    sapphire_coin = (int(left_over)//35)

    left_over_2 = left_over - sapphire_coin*35

    ruby_coin = (int(left_over_2)//10)

    amber_coin = left_over_2 - ruby_coin*10

    # Display all the result
    print("The Gemstone coin equivalent to %d ounces of gold are:\n\n \t %d Emerald Coin, \n \t %d Sapphire Coin, \n \t %d Ruby Coin, \n \t %d Amber Coin. \n\n --- See you again! ---" %(amount_gold, emerald_coin, sapphire_coin, ruby_coin, amber_coin))
