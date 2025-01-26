#Body mass calculator.
#The bmi is a measure of some's weight into account ther height.
#If a tall person and short person both weight the same amount,
#the short person is usually more overweight.
print(
      "======== Welcome to the BMI Calculator ======== \n"
      "|    Type 1 - Proceed to mass calculation     |\n"
      "|    Type 0 - Exit                            |\n"
      "==============================================="
)
start = int(input("Enter with the painel number.\n"))

#function who does the bmi's calculation
def calculation ():    
        weight = float(input("Please, type the KG.\n"))
        height = float(input("Type the height(e.g 1.50)\n"))
        bmi = (weight/(height**2))
        print(f"BMI: {bmi}")
        return bmi

#function who brings the avarage of bmi, based in function calculation.
def mass(bmi):
    if bmi < 18.5:
        print(f"- Underweight -")
        return bmi
    elif bmi < 25:
        return print(f"- Normal weight -")
    elif bmi <= 30:
        return print(f"- Overweight -")
    else:
        return print(f"- Obese -")

#loop
while start == 1:#Put code to work
    bmi_result = calculation()
    mass(bmi_result)
if start == 0: #exit
    print("Exiting the BMI Calculator.")
elif start > 2: #Reinstarted if choose number above 1
    start = int(input("Choose another number(1 or 0).\n"))
else:#Reinstarted if the number is bellow than 0 or any other quantity
    start = int(input("Choose another number(1 or 0).\n"))