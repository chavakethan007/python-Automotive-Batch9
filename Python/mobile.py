# Defining a class named mobile
class mobile:

    # Constructor method to initialize object data
    def __init__(self, brand, model_type, price):
        self.brand = brand            # Stores the brand name of the mobile
        self.model_type = model_type  # Stores the model type of the mobile
        self.price = price            # Stores the price of the mobile

    # Method to return the brand information
    def show_brand(self):
        return f"{self.brand} brand"  # Returns brand as a formatted string
    
    # Method to return the model information
    def show_model_type(self):
        return f"{self.model_type} model"  # Returns model type as a formatted string
    
    # Method to return the price information
    def show_price(self):
        return f"{self.price} Rupees"  # Returns price with currency

# Creating an object (instance) of the mobile class
mobile1 = mobile('Apple', 'Iphone15', 80000)
mobile2 = mobile('Samsung', 'Galaxy S23', 75000)

# Printing the mobile details using object attributes
print(f"The {mobile1.brand} brand of {mobile1.model_type} costs {mobile1.price} Rupees")
print(f"The {mobile2.brand} brand of {mobile2.model_type} costs {mobile2.price} Rupees")
