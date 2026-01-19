"""
Cruise Control Speed Alert System
---------------------------------
This program continuously monitors vehicle speed
and generates an alert when the speed crosses
the predefined safety limit.
"""

import time

MAX_SPEED_LIMIT = 70  # Speed limit in km/h
# System Initialization
print("Speed Limit Set to:", MAX_SPEED_LIMIT, "km/h")
print("Type 'exit' to turn OFF the system\n")

# Main Monitoring Loop
while True:
    user_input = input("Enter current vehicle speed (km/h): ")

    # Check for ignition OFF condition
    if user_input.lower() == "exit":
        print("\nSystem Stopped Successfully (Ignition OFF)")
        break

    try:
        # Convert user input to float
        current_speed = float(user_input)
        # Speed Evaluation Logic
        if current_speed > MAX_SPEED_LIMIT:
            print("ALERT: Overspeed Detected! Reduce Speed Immediately.")
        else:
            print("Speed is within the safe operating range.")

    except ValueError:
        # Handles invalid inputs like characters or symbols
        print("nvalid input! Please enter a numeric speed value.")

    # Delay to simulate real-time sensor refresh
    time.sleep(0.5)
