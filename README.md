**Task**: _Password Generator Program_

**Objective**:
Implement a password generator program using basic object-oriented programming principles in Python.

**Instructions**:

1. Create a Python class called `PasswordGenerator` that will generate random passwords based on certain criteria.

2. The PasswordGenerator class should have the following attributes:

* `length`: an integer representing the length of the password (default: 8)
* `include_uppercase`: a boolean indicating whether to include uppercase letters in the password (default: True)
* `include_lowercase`: a boolean indicating whether to include lowercase letters in the password (default: True)
* `include_digits`: a boolean indicating whether to include digits in the password (default: True)
* `include_special_chars`: a boolean indicating whether to include special characters in the password (default: True)

3. Implement the following_ methods in the PasswordGenerator class:
  * `__init__`(self): Initializes the attributes of the class.
  * `generate_password(self`): 
Generates and returns a random password based on the specified criteria. The password should be a string of characters randomly chosen from the available character sets (uppercase letters, lowercase letters, digits, and special characters).

4. Write a separate Python script (outside the class) that utilizes the PasswordGenerator class.
* Create an instance of the PasswordGenerator class.
* Prompt the user to input the desired password length and criteria (whether to include uppercase letters, lowercase letters, digits, and special characters).
* Use the instance of the class to generate a password based on the user's input.
* Display the generated password to the user.

5. Test your program with different inputs and ensure it generates passwords that satisfy the user's criteria.

** Submission Guidelines**:
* Submit the Python script file containing the implementation of the PasswordGenerator class and the separate script that utilizes the class.
* Include comments in your code to explain the purpose and functionality of each section.
* Add any additional features or enhancements to the program if you desire, as long as the basic requirements are met.

** Note **: You may use any built-in Python libraries or functions related to random number generation or string manipulation to complete this assignment.