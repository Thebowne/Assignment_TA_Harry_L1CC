import math
no1 = input("Enter the first number: ")

while no1 == "":
    no1 = input("Enter the first number: ")

print("Operators"
      "\n1. Addition"
      "\n2. Subtract"
      "\n3. Multiplication"
      "\n4. Division"
      "\n5. Power"
      "\n6. Root")

operator = str(input("Enter the operator (1/2/3/4/5/6): "))

x = float(no1)
if operator == "6":
    print("The answer is : " + str(math.sqrt(x)))
    exit()

no2 = input("Enter the second number: ")
while no2 == "":
    no2 = input("Enter the second number: ")

num1 = float(x)
num2 = float(no2)

ans = 0

if operator == "1" or operator == "+":
    ans = num1 + num2

elif operator == "2" or operator == "-":
    ans = num1 - num2

elif operator == "3" or operator == "*":
    ans = num1 * num2

elif operator == "4" or operator == "/":
    ans = num1 / num2

elif operator == "5" or operator == "^":
    ans = num1 ** num2

else:
    print("lmao")

print("The answer is : " + str(ans))
