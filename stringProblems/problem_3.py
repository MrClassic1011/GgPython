# Python | Count and display vowels in a string

def Check_Vow(string, vowels):
    final = [each for each in string if each in vowels]
    print(len(final))
    print(final)
    

string = "Pravin is learning very fast"
vowels = "AaEeIiOoUu"
Check_Vow(string, vowels)

# Counting vowels: Dictionary Way

def Check_Vow1(string, vowels):
    count = {}.fromkeys(vowels, 0)
    
    for character in string:
        if character in vowels:
            count[character] += 1
            print(character, count[character])
    return count

print(Check_Vow1(string, vowels))

# Counting vowels: recursive function way
