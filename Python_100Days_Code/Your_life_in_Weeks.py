#Dont change the code below
age = int(input("What is your current age: "))

#Dont change the code above.
years_tl = 40 - age
months = int(years_tl * 12)
days = int(years_tl * 365)

message = f"You have {days} days, {months} months and {years_tl} years"
print(message)

