import art

# add two numbers
def add(n1, n2):
    return n1 + n2
# subtract two numbers
def subtract(n1,n2):
    return n1 - n2
# multiply two numbers
def multiply(n1,n2):
    return n1 * n2
#divide two numbers
def divide(n1,n2):
    return n1 / n2

operations = {
      "+":add,
      "-":subtract,
      "*":multiply,
      "/":divide,
  }

def calculator():
    print(art.logo)
    should_continue = True

    num1 = int(input("What's the first number?: "))

    while should_continue:

        for key in operations:
            print(key)
        operation_symbol = input("Pick an operation: ")
        num2 = int(input("What's the next number?: "))
        result = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {result}")

        choice = input(f"Type 'y' to continue calculating with {result},"
                           f" or type 'n' to start a new calculation: ")

        if choice == 'y':
            num1 = result
            should_continue = True

        else:
            should_continue = False
            print("\n" * 20)
            calculator()


calculator()

