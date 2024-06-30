logo = """
 _____________________
|  _________________  |
| | kedharish->  0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print (logo)
def add (n1, n2):
  """This function adds two numbers"""
  return n1 + n2

#for Sub
def Sub (n1, n2):
  """This function subs two numbers"""
  return n1 - n2

#for multiply
def multiply (n1, n2):
  """This function multiply two numbers"""
  return n1 * n2

#for Divide
def divide (n1, n2):
  """This function divides two numbers"""
  return n1 / n2

aggregate = {
  "+": add,
  "-": Sub,
  "*": multiply,
  "/": divide,
}

number_1 = float(input("Enter the first number: "))
for symbol in aggregate:
  print(symbol)

continue_calc = True
while continue_calc:
  User_aggregate = input("Enter the operation you want to perform: ")
  Number_2 = (float(input("Enter the second number: ")))
  calc = aggregate[User_aggregate]
  answer_1 = calc(number_1, Number_2)

  print(f"{number_1} {User_aggregate} {Number_2} = {answer_1}")

  #continue
  still_continue = input("Would you like to continue (Y/N): ").lower()
  if still_continue == "y":
    continue_calc = True
    number_1 = answer_1
  elif still_continue == "n":
    continue_calc = False
    print ("thanks you for using ME !!")
    print(f"\n The Final answer is = {answer_1}")