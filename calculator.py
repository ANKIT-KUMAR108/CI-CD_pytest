from multiprocessing.sharedctypes import Value


def sum(num1,num2):
    if type(num1) not in [int,float]:
        raise ValueError("numbers must be either int or float")
    if(type(num2) not in [int, float] ):
        raise ValueError("numbers must be either ")
    return num1 + num2

def subtract(num1,num2):
    return num1 - num2

def multiply(num1,num2):
    return num1 * num2

def divide(num1,num2):
    if num2==0:
        raise ValueError("cannot divide by zero")
    return num1 // num2


