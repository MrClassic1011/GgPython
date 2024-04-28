# mkdir folder_name
# echo > stringPython.py

"""# Add 'string' directory back to the index
git add string/

# Commit the changes
git commit -m "Add 'string' directory to the parent repository"

# Push the changes to the remote repository
git push origin master
"""

print("use of title method".title())

# Python | Swap commas and dots in a String
# Python code to replace, with . and vice-versa

def Replacecd(str1):
    m = str1.maketrans
    final= str1.translate(m(',.','.,',' '))
    return final.replace(',', ", ")

# Driving Code
string = "14, 625, 498.002"
print(Replacecd(string))