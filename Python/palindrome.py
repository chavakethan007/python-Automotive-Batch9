text = input("Enter a string: ")
reversed_text = text[::-1]
if text == reversed_text:
    print("It is a palindrome.")
else:
    print("It is not a palindrome.")
