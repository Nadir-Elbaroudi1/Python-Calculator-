
from art import logo 

def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2

def multiply(n1,n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operation = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
def math_calc(): 
  print(logo)
  calculator = True
  n1 = float(input("What is your first number? "))
  for symbol in operation:
    print(symbol)
    
  while calculator:
    operation_symbol = input("Please pick an operation: ")
    n2 = float(input("What is your next number? "))
    calc_Function = operation[operation_symbol] #extracts the respective function 
    answer = calc_Function(n1,n2)
    print(f"{n1} {operation_symbol} {n2} = {answer}")
    again = input(f"Would you like to continue using {answer}? Please type 'yes' to contine or 'no' to start with a new number\n")
    if again == "yes" :
      n1 = answer
    else: 
      calculator = False
      math_calc()
      
math_calc()
  
    
  
  