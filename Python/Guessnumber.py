fixednumber = 6 # Fixed number that the user has to guess
count = 0 # Variable to count how many attempts the user makes

while True: # Infinite loop to keep asking until the correct number is guessed
    number=int(input("Enter Your number: "))    # Take number input from the user
    count+=1     # Increase attempt count by 1
        # Check if the guessed number is correct
    if number==fixednumber: 
                # Print success message with number of attempts
        print(f'The Number matched with {fixednumber} , You Gussed it in {count} attempts')
        # Stop the loop because the correct number is guessed
        break
    else:
                # Message shown when the guess is wrong
        print("Your guess is wrong,please  try again!")