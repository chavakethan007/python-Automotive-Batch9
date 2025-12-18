# Variables
name = "Chava Kethan"
age = 21
grade = 8.933

# Old style formatting (%)
print("Name: %s" % name)        # %s → string
print("Age: %d" % age)          # %d → integer
print("Grade: %f" % grade)      # %f → float (6 decimals)
print("Grade: %.2f" % grade)    # %.2f → 2 decimal places

# f-string (modern way)
item_cost = 12.36
item_count = 6
total_cost = item_cost * item_count

print(f"Your total is ${total_cost:.2f} for {item_count} items")

# Debugging style
bugs = "roaches"
count = 13
print(f"Debugging {bugs=} {count}")
