import tkinter as tk
from picamera import PiCamera
from PIL import Image, ImageTk
import time

# Initialize camera
camera = PiCamera()
camera.resolution = (640, 480)  # Set camera resolution

# Create main window
window = tk.Tk()
window.title("Camera Feed with Button")

# Create label for displaying the camera feed
camera_label = tk.Label(window)
camera_label.pack()

# Function to update the camera feed in the GUI
def update_camera_feed():
    # Capture image from the camera
    camera.capture('/home/pi/temp_image.jpg')  # Save the image temporarily
    
    # Open the captured image
    img = Image.open('/home/pi/temp_image.jpg')
    img = img.resize((640, 480))  # Resize the image to fit the window
    img_tk = ImageTk.PhotoImage(img)

    # Update the label with the new image
    camera_label.img_tk = img_tk
    camera_label.configure(image=img_tk)

    # Call update_camera_feed again after 100ms to continuously update the feed
    window.after(100, update_camera_feed)

# Function to start the camera feed when the button is clicked
def start_camera():
    update_camera_feed()

# Create a button that starts the camera feed
button = tk.Button(window, text="Start Camera", command=start_camera)
button.pack()

# Run the GUI loop
window.mainloop()
