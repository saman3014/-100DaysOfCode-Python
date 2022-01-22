#Calculator
from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def sub(n1, n2):
  return n1 - n2

#Multiply
def mul(n1, n2):
  return n1 * n2

#Divide
def div(n1, n2):
  return n1 / n2

#Dictionary

operations = {
  "+" : add,
  "-" : sub,
  "*" : mul,
  "/" : div
}

def Calculator():
  print(logo)
  num1 = float(input("What is the first number?\n"))
  for symbol in operations:
    print(symbol)
    
  should_continue = True
  
  while should_continue:
    operation_symbol = input("Pick an operation from the line above:\n")
    num2 = float(input("What is the second number?\n"))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    
    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation:\n") == "y":
      num1 = answer
    else:
      should_continue = False
      Calculator()

Calculator()
