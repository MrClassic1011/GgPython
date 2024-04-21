# Taking multiple inputs from user in Python

# -------- 1.Using split() method -----------------
# input().split(separator, maxsplit)

# taking two inputs at a time
x, y = input("Input two numbers:").split()
print("Yout first number is {0} and second number is {1}".format(x, y))

# taking multiple inputs at a time 
# and type casting using list() function
x = list(map(int, input("Enter multiple values: ").split()))
print("List of students:", x)

# -------- 2.Using map() with split() -----------------
# variable1, variable2, ... = map(datatype, input().split())

#Example with integers
a, b, c = map(int, input("Enter three numbers seperated by space").split())
print(a+b+c)

#Example with floats:
x, y = map(float, input("Enter two floats separated by a space: ").split())
print("Product:", x * y)

#Example with strings:
name, age = input("Enter your name and age separated by a space: ").split()
print("Hello,", name + "! You are", age, "years old.")

#-------- 3. Using List comprehension-----------------
# taking two input at a time
x, y = [int(x) for x in input("Enter two numbers seperated by spaces ").split()]
print("First number is ", x)
print("Second number is ", y)

# taking multiple inputs at a time 
x = [int(x) for x in input("Enter multiple values: ").split()]
print("Number of list is: ", x) 