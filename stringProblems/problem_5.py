# Python | Map function and Lambda expression in Python to replace characters
"""
Input : str = 'ratul'
        c1 = t, c2 = h 
Output : rahul
"""
def replaceChars (sring, c1, c2):
    newChars = map(lambda x: x if (x != c1 and x != c2) else c1 if (x == c2) else c2, sring)
    print (''.join(newChars))
    
replaceChars("ratul", "t", "h")

