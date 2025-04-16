

def happy():
    print("Hello")
    print("How are you")

happy()


def happyme(name,age):
    print(f"the name is {name}")
    print(f"the age is {age}")

happyme("Joe",22)

def invoice(name, amount,due_date):
    print(f"the username is {name}")
    print(f"the amount due is{amount: .2f}")
    print(f"The due date is {due_date}")

invoice("Ehsan", 25500, 12)