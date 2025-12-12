def count_vowels(string):
    vowels="aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count +=1
    return count

string_input=input("Enter String: ")
vowel_count=count_vowels(string_input)
print("The number of Vowels in a string: ", vowel_count)

