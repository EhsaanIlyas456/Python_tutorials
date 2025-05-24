class Cuisine:
    def __init__(self, name, foods):
        self.name = name
        self.foods = foods

class Food:
    def __init__(self, foodname, price):
        self.name = foodname
        self.price = price

def isitemvalid(menu, checkfood):
    for cuisine in menu:
        for food in cuisine.foods:
            if food.name == checkfood:
                return True
    return False


def finditemprice(menu, item):
    for cuisine in menu:
        for food in cuisine.foods:
            if food.name == item:
                return food.price


def make_item_non_case_sensitive(item):
    item = item.lower()
    item = item[0].upper() + item[1:]
    return item


def printmenu(menu):
    for cuisine in menu:
        print(f"{cuisine.name}: ")
        for food in cuisine.foods:
            print(f"{food.name} {food.price}Rs")
        print("\n")


def orderitem(menu):
    while True:
        item = input("Choose item to order: ")
        item = make_item_non_case_sensitive(item)
        if isitemvalid(menu, item):
            return item
        print("Item is invalid. Please choose item from the shown menu.")


def getamountofitem():
    while True:
        try:
            amount = int(input("Choose amount of item to order: "))
            if amount <= 0:
                raise ValueError("Number must be above 0")
            return amount
        except ValueError:
            print("Amount is invalid. Please enter amount as a positive integer.")


def additemtocart(menu, item, amountofitem, totalcost, ordereditems):
    ordereditems.append(f"{item} x{amountofitem}")
    totalcost += (finditemprice(menu, item) * amountOfItem)
    print(f"{item} has been added to cart")
    return totalcost


def askcontinueorder():
    while True:
        continueOrder = input("Do you want to order anything else(yes/no): ")
        if continueOrder == "yes" or continueOrder == "no":
            return continueOrder
        print("Invalid. Please enter 'yes' or 'no'.")


americanCuisine = Cuisine("American", [Food("Burger", 500), Food("Hotdog", 200)])
pakistaniCuisine = Cuisine("Pakistani", [Food("Nihari", 700), Food("Biryani", 800)])
italianCuisine = Cuisine("Italian", [Food("Pizza", 1000), Food("Pasta", 300)])

menu = [americanCuisine, pakistaniCuisine, italianCuisine]
totalCost = 0
orderedItems = []

print("Menu: \n")
printmenu(menu)

continueOrder = "yes"

while continueOrder == "yes":
    item = orderitem(menu)
    amountOfItem = getamountofitem()
    totalCost = additemtocart(menu, item, amountOfItem, totalCost, orderedItems)
    continueOrder = askcontinueorder()

print("You ordered: ")
for x in orderedItems:
    print(x)
print(f"Your total amount payable is {totalCost} Rs")
print("Thank you!")