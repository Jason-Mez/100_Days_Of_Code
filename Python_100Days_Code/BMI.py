#Calculating someones Body Mass Index

#Dont change the code below
height = float(input("Enter your height in m: "))
weight = int(input("Enter you weight in kg: "))
#Dont change the code above

#Write you code below this line
BMI = weight / (height ** 2 )
print(f"Your BMI is {round(BMI,2)}")

#Always use the type function if you are unsure about what to do.
