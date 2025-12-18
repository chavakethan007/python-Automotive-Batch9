import sys
# I Opened a text file in write mode
file = open("kethan.txt", "w")
# Redirect standard output to the file
sys.stdout=file
# print statement now go into output.txt
print("My name is kethan,I complete my graduation in 2025,Now undergoing training in wipro.")
# Close the file
file.close()
