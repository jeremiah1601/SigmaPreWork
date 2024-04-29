user_input = input("please enter a list of numbers separated by ','\n")
user_list = user_input.split(",")

biggest = -99999
smallest = 99999

for item in user_list: 
    number = int(item)
    if biggest - number <= 0:
        biggest = number
    if smallest - number >= 0:
        smallest = number
print(f"the smallest number is {smallest} and the largest is {largest}\n")