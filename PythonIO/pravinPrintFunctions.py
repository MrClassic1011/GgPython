"""
tripple quatations are used for multiline comments.
Syntax for printfunction
Syntax : print(value(s), sep= ‘ ‘, end = ‘\n’, file=file, flush=flush)

Parameters: 

    value(s): Any value, and as many as you like. Will be converted to a string before printed
    sep=’separator’ : (Optional) Specify how to separate the objects, if there is more than one.Default :’ ‘
    end=’end’: (Optional) Specify what to print at the end.Default : ‘\n’
    file : (Optional) An object with a write method. Default :sys.stdout
    flush : (Optional) A Boolean, specifying if the output is flushed (True) or buffered (False). Default: False

Return Type: It returns output to the screen.
"""

name = "Pravin"
age = 30
print("Hello, my name is", name, "and I am", age, "years old", end="** ")
print("Pravin")

# Print concatenated strings
name= "Pravin"
name1= "Rutuja"
print(name+" "+name1)

# Output formating (string.format)==> string formating
a, b, = 10, 20
print('value of a is {} and value of b is {}'.format(a,b))

# Flush parameter in Python with print() function
#without flush example
import time
count_seconds = 3
for i in reversed (range(count_seconds+1)):
    if i > 0:
        print(i, end=">>>")
        time.sleep(1)
    else:
        print("Start")

#flush example: its applications are related when input or output is buffering and data is not in the chuncks       
count_seconds_f = 3
for j in reversed (range(count_seconds_f+1)):
    if j > 0:
        print(j, end=">>>", flush= True)
        time.sleep(1)
    else:
        print("start")
        
# Python “sep” parameter in print()

a=10
b=20
c=30

print(a, b, c, sep='-')

#File Argument in Python print() 
"""
import io

# declare a dummy file
dummy_file = io.StringIO()

# add message to the dummy file
print('Hello Geeks!!', file=dummy_file)

# get the value from dummy file
print(dummy_file.getvalue())

--------------------------------
print('Welcome to GeeksforGeeks Python world.!!', file=open('Testfile.txt', 'w'))

"""