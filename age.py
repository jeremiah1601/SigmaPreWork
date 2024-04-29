import datetime
"""
calculates the year difference rounded down between the given date and the current date

we will accomplish this by turning each date into days
calculate their differences
integer division by 365 to calculate years
"""


user_date = input('please enter a given date in the "DD-MM-YYYY" format\n')
format_user_date = user_date.split("-")
user_day = int(format_user_date[0])
user_month = int(format_user_date[1])
user_year = int(format_user_date[2])

delta = abs(datetime.date(user_year, user_month, user_day) - datetime.date.today())

age = delta.days // 365

print(f"the difference is {age}\n")