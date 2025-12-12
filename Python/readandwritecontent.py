def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print(f"Content written to {filename} successfully.")

def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        print(f"Content of {filename}:")
        print(content)
    except FileNotFoundError:
        print(f"Error: {filename} not found.")

filename = input("Enter the filename: ")
content_to_write = input("Enter content to write to the file: ")

write_file(filename, content_to_write)
read_file(filename)