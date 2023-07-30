import string
import random

class PasswordGenerator():

    def __init__(
        self,
        length = 4,
        include_uppercase = True,
        include_lowercase = True,
        include_digits = True,
        include_special_chars = True
    ):
        self.length = length;
        self.include_uppercase = include_uppercase;
        self.include_lowercase = include_lowercase;
        self.include_digits = include_digits;
        self.include_special_chars = include_special_chars;
    
    def generate_password(self):
        password_array = [];
        chars = '';
        if self.include_uppercase:
            chars = chars + string.ascii_uppercase;
            password_array.append(random.choice(string.ascii_uppercase));
        if self.include_lowercase:
            chars = chars + string.ascii_lowercase;
            password_array.append(random.choice(string.ascii_lowercase));
        if self.include_digits:
            chars = chars + string.digits;
            password_array.append(random.choice(string.digits));
        if self.include_special_chars:
            chars = chars + string.punctuation;
            password_array.append(random.choice(string.punctuation));

        if len(chars) > 0:
            # add random characters
            for _ in range(self.length - len(password_array)):
                password_array.append(random.choice(chars))

            # randomize order of characters
            random.shuffle(password_array);
            return ''.join(password_array);
        else:
            return '';

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

# get password length from user
def input_password_length():
    return input("Please enter the desired password length: ");

# get password configurations from user
def input_password_configurations():
    include_uppercase = bool(input("Do you want to include uppercase characters? type y/n? ") == 'y');
    include_lowercase = bool(input("Do you want to include lowercase characters? type y/n? ") == 'y');
    include_digits = bool(input("Do you want to include digits? type y/n? ") == 'y');
    include_special_chars = bool(input("Do you want to include special characters? type y/n? ") == 'y');

    if include_uppercase or include_lowercase or include_digits or include_special_chars:
        return [
            include_uppercase,
            include_lowercase,
            include_digits,
            include_special_chars
        ];
    else:
        print("You did not choose any type of password characters! Please choose at least one of the types!");
        return input_password_configurations();

def init():
    print("Welcome to the Linux User Password Generator!");
    # get password length from user
    password_length = is_value_in_limit(input_password_length);

    # get password configurations from user
    config = input_password_configurations();

    # create new instance of PasswordGenerator class
    password_generator_inst = PasswordGenerator(
        password_length,
        config[0],
        config[1],
        config[2],
        config[3]
    );
    # create password
    print(password_generator_inst.generate_password());

init();