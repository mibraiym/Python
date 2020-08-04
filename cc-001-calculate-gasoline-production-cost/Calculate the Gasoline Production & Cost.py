'''Problem Statement
Write a program that will prompt the user for inputting a floating point number that stands for gallons of gasoline. 
You will re-print that value along with other information about gasoline and gasoline usage:
    Amount of liters
    Amount of barrels of oil required to make this amount of gasoline
    Price in US dollars
Here are some approximate conversion values:
    1 gallon is equivalent to 3.7854 liters
    1 barrel of oil approximately produces 19.5 gallons of gas
    God knows what the cost should be, but let’s assume it $0.75/liter
'''

gallons_int = input('Enter a number which stands for gallons of gasoline: ')

gallons_fl = float(gallons_int)
liters = gallons_fl * 3.7854
barrels = gallons_fl / 19.5
cost= liters * 0.75

print(f"{gallons_fl} gallon(s) = {liters} liter(s).")
print(f"{barrels} barrel(s) of oil required to produce {gallons_fl} gallon(s) of gas.")
print(f"It will cost ${cost} dollar(s).")


