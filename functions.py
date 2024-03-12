"""
Description: Module 05 demonstration: Functions
Author: {student name}
Date: {current date}
Usage: To run individual functions, place a function 
call within the main guard.
"""

def greet() -> None:
    """
    Prints a greeting message to the console.
    Returns:
        None
    """

    print("Hello, world!")

#greet()
#greet()


def greet_name(name: str) -> None:
    """
    Prints a greeting which includes the value of the name argument.
    Args:
        name (str): The name of the person to greet.
    Returns:
        None
    """

    print(f"Hello {name}!")

#greet_name("Yizheng")
#greet_name("Conrad")
#greet_name("Kiranjeet")


#def greet_name_age(name, age):   # Does not meet PEP 8 standards
def greet_name_age(name: str, age: int) -> None:
    """
    Prints a greeting which includes 
    the values of the name and age arguments.
    Args:
        name (str): The name of the person to greet.
        age (int): The age of the person to greet.
    Returns:
        None
    """

    print(f"Hello {name}, you are {age} years old!")


#greet_name_age("Nathan", 30)




def math_operation(operand1: int, operand2: int, operation: str)-> float:
    """
    Returns the result of the specified operation based 
    on the two operands.
    Args:
        operand1 (int): The first operand.
        operand2 (int): The second operand.
        operation (str): The operation to perform.
    Returns:
        Float
    """

    if operation == "+":
        result = operand1 + operand2
    else:
        result = operand1 - operand2

    return result

result = math_operation(1, 3, "+")
#print(result)


def math_operation(operand1: int, operand2: int, operation: str = "+")-> float:
    """
    Returns the result of the specified operation based 
    on the two operands.

    Args:
        operand1 (int): The first operand.
        operand2 (int): The second operand.
        operation (str): The operation to perform.
    Returns:
        Float
    """

    if operation == "+":
        result = operand1 + operand2
    elif operation == "-":
        result = operand1 - operand2
    else:
        raise ValueError("Invalid operation.")   
    
    return result

try:
    result = math_operation(5, 5)
except ValueError as e:
    print(e)

print(result)


# printing functions documentation
    
#print(math_operation.__doc__) # __ dunder --> double underscore
#print(print.__doc__)
#print(len.__doc__)