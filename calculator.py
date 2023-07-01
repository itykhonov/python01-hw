# check is the value is integer or recall the action from user
def is_integer(input):
    try:
        val = int(input())
        return val;
    except ValueError:
        print("Input is not an integer. Try one more time.");
        return is_integer(input);

# check is the value is integer and it is in the valid range or recall the action from user        
def is_operation_valid(input):
    val = is_integer(input);

    if 1 <= val <= 4:
        return val;
    else:
        print("Operation - " + str(val) + " is out from the range from 1 to 4. Try one more time.");
        return is_operation_valid(input);

def addition(a, b):
    return a + b;
   
def subtraction(a, b):
    return a - b;
   
def multiplication(a, b):
    return a * b;

def division(a, b):
    return a / b;

# calculate the result
def calc(operation, value1, value2):
    if operation == 1:
        return "The result of addition is: " + str(addition(value1, value2));
    elif operation == 2:
        return "The result of subtraction is: " + str(subtraction(value1, value2));
    elif operation == 3:
        return "The result of multiplication is: " + str(multiplication(value1, value2));
    elif operation == 4:
        if value2 != 0:
            return "The result of division is: " + str(division(value1, value2));
        else:
            return "Error! Can't divide by zero!";

# enter first number
def first_step():
    return input("Please enter the first integer: ");

# enter second number   
def second_step():
    return input("Please enter the second integer: ");

# enter operator from the range
def third_step():
    print("Please select an operation:");
    print("1. Addition");
    print("2. Subtraction");
    print("3. Multiplication");
    print("4. Division");

    return input("Enter your choice (1-4): ");

# init calculator
def init():
    print("Welcome to the Calculator Program!");

    number_1 = is_integer(first_step);
    number_2 = is_integer(second_step);
    operation = is_operation_valid(third_step);
    result = calc(operation, number_1, number_2);

    print(result);
    
init();