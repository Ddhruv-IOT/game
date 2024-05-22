# import pyautogui
# import time
# import math

# # Set the radius of the circle
# radius = 100

# # Set the speed of movement
# speed = 0.1  # Adjust as needed

# # Calculate initial position
# center_x, center_y = pyautogui.position()
# angle = 0

# try:
#     while True:
#         # Calculate new position on the circle
#         x = center_x + radius * math.cos(angle)
#         y = center_y + radius * math.sin(angle)

#         # Move the cursor to the new position
#         pyautogui.moveTo(x, y, duration=speed)

#         # Increment angle
#         angle += 0.1

#         # Pause briefly to prevent overwhelming system
#         time.sleep(7)

# except KeyboardInterrupt:
#     print("\nScript terminated by user.")


import pyautogui
import time
import math
import threading

# Set the radius of the circle
radius = 100

# Set the speed of movement
speed = 0.1  # Adjust as needed

# Calculate initial position
center_x, center_y = pyautogui.position()
angle = 0

# Create a flag for controlling the thread
move_cursor = threading.Event()

def move_in_circle():
    global angle
    while True:
        if move_cursor.is_set():
            # Calculate new position on the circle
            x = center_x + radius * math.cos(angle)
            y = center_y + radius * math.sin(angle)

            # Move the cursor to the new position
            pyautogui.moveTo(x, y, duration=speed)

            # Increment angle
            angle += 0.1

            # Pause briefly to prevent overwhelming system
            time.sleep(0.1)
        else:
            time.sleep(0.1)  # Check the flag status periodically

# Start the movement thread
movement_thread = threading.Thread(target=move_in_circle)
movement_thread.daemon = True
movement_thread.start()

try:
    while True:
        user_input = input("Enter 'On' to start and 'Off' to stop the cursor movement: ").strip().lower()
        if user_input == "on":
            move_cursor.set()
        elif user_input == "off":
            move_cursor.clear()
        else:
            print("Invalid input. Please enter 'On' or 'Off'.")
except KeyboardInterrupt:
    print("\nScript terminated by user.")
