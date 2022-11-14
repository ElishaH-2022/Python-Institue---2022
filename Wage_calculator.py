#Calculate wage based on desired salary

import time

name = input("Hello, what is your name? " )
print(name + ", This program will calculate what your hourly rate will be based on how much you want to earn annually \n ")

time.sleep(2)

salary = input(name + ", How much do you want to get paid annually? ")
#40_hour_week * 52weeks = 2080 

salary = salary.replace(",", "")
salary = float(salary)

hourly_wage = salary / 2080

hourly_wage = round(hourly_wage, 2)

print("Your hourly rate will be £" + str(hourly_wage) + " per hour ")