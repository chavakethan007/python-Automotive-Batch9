import math

def pure_pursuit(vehicle_x, vehicle_y, target_x, target_y):
    dx = target_x - vehicle_x
    dy = target_y - vehicle_y

    # Steering angle towards target point
    steering_angle = math.atan2(dy, dx)
    return steering_angle

def stanley_controller(vehicle_y, vehicle_heading, path_heading, k):
    """
    Stanley Controller

    vehicle_y       : Lateral distance of vehicle from path center line
                      (This is the cross-track error)

    vehicle_heading : Current direction (yaw) of the vehicle in radians

    path_heading    : Desired direction of the road/path in radians

    k               : Control gain (decides how aggressively the vehicle corrects)
    """

    # Difference between the direction of the path and the direction the vehicle is currently facing.
    # If positive → vehicle is pointing away from the path direction
    # If zero → vehicle is perfectly aligned with the path
    heading_error = path_heading - vehicle_heading


    # Sideways distance between vehicle and path center line.
    # If positive → vehicle is above / left of the path
    # If negative → vehicle is below / right of the path
    cross_track_error = vehicle_y


    # Combines heading correction and lateral correction
    # atan() limits the correction to a smooth steering angle
    steering_angle = heading_error + math.atan(k * cross_track_error)

    return steering_angle

def main():

    print("ENTER VEHICLE DETAILS")
    vehicle_x = float(input("Vehicle X position: "))
    vehicle_y = float(input("Vehicle Y position (cross-track error): "))
    vehicle_heading = float(input("Vehicle heading (yaw in radians): "))

    print("\nENTER PATH DETAILS")
    path_heading = float(input("Path heading (radians): "))
    target_x = float(input("Target X position: "))
    target_y = float(input("Target Y position: "))

    print("\nENTER STANLEY CONTROLLER GAIN")
    k = float(input("Gain (k): "))

    pp_angle = pure_pursuit(vehicle_x, vehicle_y, target_x, target_y)

    stanley_angle = stanley_controller(vehicle_y, vehicle_heading, path_heading, k)

    print("\n--- OUTPUT ---")
    print("Pure Pursuit Steering Angle (radians):", pp_angle)
    print("Pure Pursuit Steering Angle (degrees):", math.degrees(pp_angle))

    print("\nStanley Steering Angle (radians):", stanley_angle)
    print("Stanley Steering Angle (degrees):", math.degrees(stanley_angle))


# Program entry point
if __name__ == "__main__":
    main()