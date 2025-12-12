char = input("Enter a character: ")
if len(char) != 1 or not char.isalpha():
    print("Please enter a single character.")
else:
    vowels = "aeiouAEIOU"
    if char in vowels:
        print(char, "is a vowel.")
    else:
        print(char, "is a consonant.")
