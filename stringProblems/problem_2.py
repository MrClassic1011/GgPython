# cd stringProblems

"""String to List Conversion in Python

Below are the methods that we will cover in this article:

    Using list()
    Using list comprehension 
    Using split() method
    Using string slicing
    Using re.findall() method
    Using enumerate function 
    Using JSON
    Using ast.literal
"""
# Using list()

p = "Pravin Rutuja"
print(p)
print("Using List():", list(p))

# Using list comprehension
print("List comprehension: ", [i for i in p])

# Python Convert String to List using split() method
# Input: Pravin-Rutuja;  Output: ["Pravin", "Rutuja"]
def Covert(str1):
    return list(str1.split("-"))
p= "Rutuja-Pravin"
print(Covert(p))



