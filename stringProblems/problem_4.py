# Python | Python program to check the validity of a Password

"""In this program, we will be taking a password as a combination of alphanumeric characters along with special characters, and checking whether the password is valid or not with the help of a few conditions.

Primary conditions for password validation:

    Minimum 8 characters.
    The alphabet must be between [a-z]
    At least one alphabet should be of Upper Case [A-Z]
    At least 1 number or digit between [0-9].
    At least 1 character from [ _ or @ or $ ].
"""

import re
password = input("Enter your password")

flag = 0

while True:
    if len(password) <= 8:
        flag = -1
        break
    
    elif not re.search ("[a-z]", password):
        flag= -1
        break
    
    elif not re.search ("[A-Z]", password):
        flag= -1
        break
    
    elif not re.search ("[0-9]", password):
        flag= -1
        break
    
    elif not re.search ("[_@$]", password):
        flag= -1
        break
    
    elif re.search ("\\s" , password):
        flag= -1
        break
    
    else:
        flag= 0
        print("It's a valid password")
        break
    
if flag == -1:
    print("Not a Valid Password ")