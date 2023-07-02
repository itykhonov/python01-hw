import string
import random

# check is the value is integer or recall the action from user
def is_integer(input):
    try:
        val = int(input())
        return val;
    except ValueError:
        print("Input is not an integer. Try one more time.");
        return is_integer(input);

# check is the value is integer and it is in the valid range or recall the action from user        
def is_value_in_limit(input):
    val = is_integer(input);

    if 4 <= val <= 12:
        return val;
    else:
        print("Value - " + str(val) + " is out from the range (4 - 12 symbols). Try one more time.");
        return is_value_in_limit(input);

# generate password with setted length
def passord_generator(size):
    chars = string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation;

    # password has at least one uppercase letter, one lowercase letter, one digit, one symbol
    password_array = [
     random.choice(string.ascii_uppercase),
     random.choice(string.ascii_lowercase),
     random.choice(string.digits),
     random.choice(string.punctuation),
    ];

    # add random characters if inputed length more than 4
    for _ in range(size - len(password_array)):
        password_array.append(random.choice(chars))

    # randomize order of characters
    random.shuffle(password_array);
    return ''.join(password_array);

# get password length from user
def input_password_length():
    return input("Please enter the desired password length: ")

def init():
    print("Welcome to the Linux User Password Generator!");
    password_length = is_value_in_limit(input_password_length);
    print(passord_generator(password_length));

init();