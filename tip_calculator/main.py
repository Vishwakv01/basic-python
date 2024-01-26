# current_age = input("Enter the current age.\n")
# age_probabaly_leave = input("Enter the age you probabaly Leave.\n")
# year_left = int(age_probabaly_leave) - int(current_age)
# no_of_weeks = year_left * 365 / 7
# print(f"No of weeks you have - {int(no_of_weeks)}")

# ===========================================================
# Learning on data types
# Here you will calculate the share amount of your in a tip
total_bil = float(input("Enter the total bill amount.\n"))
percentage_of_tip = int(input("Enter the percentage of tip you like to give in you total bill amount 10, 12 or 14\n"))
no_people = int(input("No of people you would like share\n"))

your_share = "{:.2f}".format(((total_bil * percentage_of_tip)/100) / no_people, 2)
print(f"You share in the tip contribuation is {your_share}")
