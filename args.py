# * called the packing operating
# *args you can add as many non key arguments in the function
# ** Double packing  operator
# **kwargs is used to add multiple keyword arguments

def happy(*args):
    print(f"{args}")

print(happy(1,2,3,4,5))

def sad(**kwargs):
    print(f"The keywords arguments are{kwargs}")

sad(happy="Happy Now")

