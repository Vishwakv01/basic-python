# find out leap year
# year = int(input("Enter the year you wanted to test the leap year/not: "))

# if year % 4 == 0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is leap year.")
#         else:
#             print(f"{year} is not a leap year.")
#     else:
#         print(f"{year} is a leap year.")
# else:
#     print(f"{year} is not a leap year.hgchjbk")


# ==============================================================
# this program to check the conditions and the logical operator

print("Welcome to Treasure Island.\n Your mission is to find the treasure.")
direction = input("You're at a cross road. where do you want to go? 'left' or 'right' ")
if direction == "left":
    do_what = input("You come to lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat Type 'swim' to swim across. ")
    if do_what == "wait":
        door_color = input("You arrive at the island unharmed. There is a house with 3 doors. one red, one yellow and one blue whcih color do you choose? ")
        if door_color == "yellow":
            print("You found the tressure. You won!!")
        else:
            print(f"You have chose {door_color}: Game Over.")
    else:
        print(f"You chose to {do_what} so some Big blue well attacked you so Game Over.")
else:
    print(f"You taken the {direction} direction: Game over.")