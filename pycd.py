import pyautogui
import time
import math

# Set the radius of the circle
radius = 100

# Set the speed of movement
speed = 0.1  # Adjust as needed

# Calculate initial position
center_x, center_y = pyautogui.position()
angle = 0

try:
    while True:
        # Calculate new position on the circle
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)

        # Move the cursor to the new position
        pyautogui.moveTo(x, y, duration=speed)

        # Increment angle
        angle += 0.1

        # Pause briefly to prevent overwhelming system
        time.sleep(7)

except KeyboardInterrupt:
    print("\nScript terminated by user.")
