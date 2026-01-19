import math

# -------------------------------
# Pure Pursuit Controller
# -------------------------------
def pure_pursuit(vehicle_x, vehicle_y, target_x, target_y):
    dx = target_x - vehicle_x
    dy = target_y - vehicle_y

    # Steering angle towards target point
    steering_angle = math.atan2(dy, dx)
    return steering_angle


# -------------------------------
# Stanley Controller
# -------------------------------
def stanley_controller(vehicle_y, vehicle_heading, path_heading, k):
    """
    Stanley Controller
    """
    heading_error = path_heading - vehicle_heading
    cross_track_error = vehicle_y

    steering_angle = heading_error + math.atan(k * cross_track_error)
    return steering_angle


# -------------------------------
# Helper function for default input
# -------------------------------
def get_input(prompt, default):
    user_input = input(f"{prompt} [default = {default}]: ")
    return float(user_input) if user_input.strip() != "" else default


# -------------------------------
# Main Function
# -------------------------------
def main():

    print("ENTER VEHICLE DETAILS")
    vehicle_x = get_input("Vehicle X position", 0.0)
    vehicle_y = get_input("Vehicle Y position (cross-track error)", 1.0)
    vehicle_heading = get_input("Vehicle heading (yaw in radians)", 0.0)

    print("\nENTER PATH DETAILS")
    path_heading = get_input("Path heading (radians)", 0.0)
    target_x = get_input("Target X position", 10.0)
    target_y = get_input("Target Y position", 5.0)

    print("\nENTER STANLEY CONTROLLER GAIN")
    k = get_input("Gain (k)", 0.5)

    # Controller outputs
    pp_angle = pure_pursuit(vehicle_x, vehicle_y, target_x, target_y)
    stanley_angle = stanley_controller(vehicle_y, vehicle_heading, path_heading, k)

    # Results
    print("\n--- OUTPUT ---")
    print("Pure Pursuit Steering Angle (radians):", pp_angle)
    print("Pure Pursuit Steering Angle (degrees):", math.degrees(pp_angle))

    print("\nStanley Steering Angle (radians):", stanley_angle)
    print("Stanley Steering Angle (degrees):", math.degrees(stanley_angle))


# -------------------------------
# Program Entry Point
# -------------------------------
if __name__ == "__main__":
    main()
