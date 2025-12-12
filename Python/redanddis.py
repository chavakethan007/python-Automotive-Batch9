filename = input("Enter the filename: ")
try:
    with open("example.txt", 'r') as file:
        content = file.read()
        print("\nFile contents:\n")
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
