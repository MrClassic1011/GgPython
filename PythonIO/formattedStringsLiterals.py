"""Syntax: { }.format(value)

Parameters: 

    value : Can be an integer, floating point numeric constant, string, characters or even variables.

Returntype: Returns a formatted string with the value passed as parameter in the placeholder position. """

# String Format() in Python
name = "Pravin"
age = 30
message = "Hi, my name is {0} and I am {1} years old. {1} is my favorite number.".format(name, age)
print(message)

# String format() with multiple placeholders
print("This is {} {} {} {}".format("one", "five", "three", "four"))

# Formatters with Positional and Keyword Arguments
print("{name} is a very smart person. In university exams he secured {0}th rank and cleared all exams with {1}."
      .format("10", "distinction", name="Pravin",))

# Type Specifying In Python
# To limit the precision
print("My average of this {0} was {1:.2f}%"
      .format("semester", 78.234876))
 
# For no decimal places
print("My average of this {0} was {1:.0f}%"
      .format("semester", 78.234876))
 
# Convert an integer to its binary or
# with other different converted bases.
print("The {0} of 100 is {1:b}"
      .format("binary", 100))

"""
    Syntax : String {field_name:conversion} Example.format(value)
    Errors and Exceptions : 
    ValueError : Error occurs during type conversion in this method.
    
    Another useful Type Specifying 

    %u unsigned decimal integer
    %o octal integer
    f - floating-point display
    b - binary number
    o - octal number
    %x - hexadecimal with lowercase letters after 9
    %X- hexadecimal with uppercase letters after 9
    e - exponent notation

"""
#Type Specifying Errors
"""
# When explicitly converted floating-point
# values to decimal with base-10 by 'd'
# type conversion we encounter Value-Error.
print("The temperature today is {0:d} degrees outside !"
      .format(35.567))
 
# Instead write this to avoid value-errors
''' print("The temperature today is {0:.0f} degrees outside !"
                                            .format(35.567))'''
"""
# Padding Substitutions or Generating Spaces
# Q. Printing square to forth power for the given range of numbers

def unorganized (a, b):
    for i in range(a, b):
        print(i, i**2, i**3, i**4)
        
def organized (a, b):
    for i in range(a, b):
        # Using formatters to give 6
        print("{:6d} {:6d} {:6d} {:6d}".format(i, i**2, i**3, i**4))

n1 = int(input("Enter lower range: "))
n2 = int(input("Enter upper range: "))

print("------Before Using Formatters-------")
 
# Calling function without formatters
unorganized(n1, n2)

print("------After Using Formatters-------")
 
# Calling function with formatters
organized(n1, n2)

# Using a dictionary for string formatting
introduction = 'My name is {first_name} {middle_name} {last_name} aka the {aka}.'
full_name = {
    'first_name' : 'Rutuja',
    'middle_name' : 'Pravin',
    'last_name' : 'Maratha',
    'aka' : 'Mrs. Classic'
}

# Notice the use of "**" operator to unpack the values.
print(introduction.format(**full_name))

# Python format() with list
# Python code to truncate float
# values to 2 decimal digits.
   
# List initialization
Input = [100.7689454, 17.232999, 60.98867, 300.83748789]

# Using format
Output = ['{:.2f}'.format(elema) for elema in Input]

# Print output
print(Output)  