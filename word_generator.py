"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
def main():
    import random

    VOWELS = "aeiou"
    CONSONANTS = "bcdfghjklmnpqrstvwxyz"
    WILDCARD = "#%*/"

    print("Enter the word format")
    print("*Only c and v is accepted\n(c for consonants, v for vowels)")
    word_format = str(input(">>>")).lower()
    word = ""
    valid = is_valid_format(word_format)
    while valid != True:
        print("Format entered is invalid\nPlease enter only c and v")
        word_format = str(input(">>>")).lower()
        valid = is_valid_format(word_format)
    for kind in word_format:
        if kind == "c":
            word += random.choice(CONSONANTS)
        else:
            word += random.choice(VOWELS)

    print(word)

def is_valid_format(word_format):
    for letter in word_format:
        if letter == "c" or letter == "v":
            valid = True
        else:
            valid = False
            return valid
    return valid
main()