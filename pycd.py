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


# import pyautogui
# import time
# import math
# import threading

# # Set the radius of the circle
# radius = 100

# # Set the speed of movement
# speed = 0.1  # Adjust as needed

# # Calculate initial position
# center_x, center_y = pyautogui.position()
# angle = 0

# # Create a flag for controlling the thread
# move_cursor = threading.Event()

# def move_in_circle():
#     global angle
#     while True:
#         if move_cursor.is_set():
#             # Calculate new position on the circle
#             x = center_x + radius * math.cos(angle)
#             y = center_y + radius * math.sin(angle)

#             # Move the cursor to the new position
#             pyautogui.moveTo(x, y, duration=speed)

#             # Increment angle
#             angle += 0.1

#             # Pause briefly to prevent overwhelming system
#             time.sleep(0.1)
#         else:
#             time.sleep(0.1)  # Check the flag status periodically

# # Start the movement thread
# movement_thread = threading.Thread(target=move_in_circle)
# movement_thread.daemon = True
# movement_thread.start()

# try:
#     while True:
#         user_input = input("Enter 'On' to start and 'Off' to stop the cursor movement: ").strip().lower()
#         if user_input == "on":
#             move_cursor.set()
#         elif user_input == "off":
#             move_cursor.clear()
#         else:
#             print("Invalid input. Please enter 'On' or 'Off'.")
# except KeyboardInterrupt:
#     print("\nScript terminated by user.")


# import pyautogui
# import time
# import math
# import threading
# from pynput import mouse, keyboard

# # Set the radius of the circle
# radius = 100

# # Set the speed of movement
# speed = 0.1  # Adjust as needed

# # Calculate initial position
# center_x, center_y = pyautogui.position()
# angle = 0

# # Create a flag for controlling the thread
# move_cursor = threading.Event()

# # Variable to track the last active time
# last_active_time = time.time()

# # Inactivity timeout in seconds (2 minutes)
# INACTIVITY_TIMEOUT = 2

# def move_in_circle():
#     global angle
#     while True:
#         if move_cursor.is_set():
#             # Calculate new position on the circle
#             x = center_x + radius * math.cos(angle)
#             y = center_y + radius * math.sin(angle)

#             # Move the cursor to the new position
#             pyautogui.moveTo(x, y, duration=speed)

#             # Increment angle
#             angle += 0.1

#             # Pause briefly to prevent overwhelming system
#             time.sleep(0.1)
#         else:
#             time.sleep(0.1)  # Check the flag status periodically

# def check_inactivity():
#     global last_active_time
#     while True:
#         current_time = time.time()
#         if (current_time - last_active_time) > INACTIVITY_TIMEOUT:
#             move_cursor.set()
#         else:
#             move_cursor.clear()
#         time.sleep(1)

# def on_activity(x, y):
#     global last_active_time
#     last_active_time = time.time()

# # Start the movement thread
# movement_thread = threading.Thread(target=move_in_circle)
# movement_thread.daemon = True
# movement_thread.start()

# # Start the inactivity checking thread
# inactivity_thread = threading.Thread(target=check_inactivity)
# inactivity_thread.daemon = True
# inactivity_thread.start()

# # Listen to mouse and keyboard events to detect activity
# mouse_listener = mouse.Listener(on_move=on_activity)
# keyboard_listener = keyboard.Listener(on_press=lambda key: on_activity(None, None))

# mouse_listener.start()
# keyboard_listener.start()

# try:
#     mouse_listener.join()
#     keyboard_listener.join()
# except KeyboardInterrupt:
#     print("\nScript terminated by user.")


import pyautogui
import time
import math
import threading
from pynput import mouse, keyboard

# Set the radius of the circle
radius = 1

# Set the speed of movement
speed = 0.1  # Adjust as needed

# Calculate initial position
center_x, center_y = pyautogui.position()
angle = 0

# Create flags for controlling the threads
move_cursor = threading.Event()
check_inactivity_flag = threading.Event()

# Variable to track the last active time
last_active_time = time.time()

# Inactivity timeout in seconds (2 minutes)
INACTIVITY_TIMEOUT = 2

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

def check_inactivity():
    global last_active_time
    while True:
        if check_inactivity_flag.is_set():
            current_time = time.time()
            if (current_time - last_active_time) > INACTIVITY_TIMEOUT:
                move_cursor.set()
            else:
                move_cursor.clear()
        else:
            move_cursor.clear()  # Ensure cursor movement is stopped if checking is disabled
        time.sleep(1)

def on_activity(x, y):
    global last_active_time
    last_active_time = time.time()

# Start the movement thread
movement_thread = threading.Thread(target=move_in_circle)
movement_thread.daemon = True
movement_thread.start()

# Start the inactivity checking thread
inactivity_thread = threading.Thread(target=check_inactivity)
inactivity_thread.daemon = True
inactivity_thread.start()

# Listen to mouse and keyboard events to detect activity
mouse_listener = mouse.Listener(on_move=on_activity)
keyboard_listener = keyboard.Listener(on_press=lambda key: on_activity(None, None))

mouse_listener.start()
keyboard_listener.start()

try:
    while True:
        user_input = input("Enter 'On' to start sensing inactivity and 'Off' to stop: ").strip().lower()
        if user_input == "on":
            check_inactivity_flag.set()
            print("Inactivity sensing enabled.")
        elif user_input == "off":
            check_inactivity_flag.clear()
            print("Inactivity sensing disabled.")
        else:
            print("Invalid input. Please enter 'On' or 'Off'.")
except KeyboardInterrupt:
    print("\nScript terminated by user.")
