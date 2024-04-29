user_input = input("please enter a list of numbers separated by ','\n")
user_list = user_input.split(",")

"""
under the assumption of a non empty list and a limited range of list values
we will find the largest and the smallest items of the list

method:
if bigggest - number is less than zero, number must be bigger than our current biggest
is smaller than the current number we are looking at

conversely, if smallest - number is more than zero, our current smallest number is 
larger than this number we are currently on

we end the algorithm once we have looked at every item 
"""

biggest = -99999
smallest = 99999

for item in user_list: 
    number = int(item)
    if biggest - number <= 0:
        biggest = number
    if smallest - number >= 0:
        smallest = number
print(f"the smallest number is {smallest} and the largest is {biggest}\n")