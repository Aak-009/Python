# Question:
# Welcome to the roller coaster ride!
#
# Rules:
# 1. A person can ride only if their height is more than 120 cm.
# 2. Ticket prices:
#    - Under 12 years old: $5
#    - Age 12 to 18: $7
#    - Above 18: $12
# 3. If the person wants photos taken during the ride,
#    add an extra $3 to the bill.
#
# Write a program that:
# - checks if the person can ride
# - calculates the total bill
# - prints the final amount



print("welcome")
height = int(input("enter height in cm: "))

if height>=120:
    print("you can ride")

    age = int(input("enter age: "))
    want_photo = input("want photos(true/false )\n").lower()=="true"
        #
    #
    if age>18:
        if want_photo:
            print("you pay 15 $")
        else:
            print("pay 12")
    elif age<12:
        if want_photo:
            print("pay 8 dollar $")
        else:
            print("pay 5 dollar $")

    else:
        if want_photo:
            print("pay 10 $")  
        else:
            print("pay 7 $")

else:
    print("you cant")
