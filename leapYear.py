###########################################################
# This script calculates if a year is a leap year or not 
###########################################################

#get the year to check
year = int(input("Which year do you want to check? "))

#check if the year is a leap year or not
if ( year % 4 == 0 ):

    if year % 100 == 0:

        if year % 400 == 0:
            print(f"{year} is a Leap year")

        else:
            print(f"{year} is not a Leap year")
    else:
        print(f"{year} is a Leap year")

else:
    print(f"{year} is not a Leap year")