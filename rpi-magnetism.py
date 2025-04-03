import time
import pandas as pd
from Adafruit_ADS1x15 import ADS1115
import RPi.GPIO as GPIO

# Setup
adc = ADS1115()
lcd_columns = 16  # Number of columns on LCD
lcd_rows = 2  # Number of rows on LCD


# You would need to add code here to initialize your LCD, for example:
# lcd = some_lcd_library.LCD()

# Function to read magnetism data from the Hall sensor
def read_magnetism():
    # Read a single value from the first channel (A0)
    value = adc.read_adc(0, gain=1)  # Use the appropriate channel
    return value


# Initialize a pandas DataFrame to store data
data = pd.DataFrame(columns=["Timestamp", "Magnetism"])


# Function to update the LCD display and store data
def update_display_and_save():
    magnetism_value = read_magnetism()

    # Display on LCD
    # lcd.clear()  # Clear the screen
    # lcd.message("Magnetism: {}".format(magnetism_value))
    print(f"Magnetism: {magnetism_value}")  # Print to console for now

    # Get current timestamp
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

    # Append data to DataFrame
    data.loc[len(data)] = [timestamp, magnetism_value]

    # Store data in CSV
    data.to_csv('magnetism_data.csv', index=False)


# Main loop
try:
    while True:
        update_display_and_save()
        time.sleep(1)  # Adjust the sleep time as necessary for your needs
except KeyboardInterrupt:
    print("Program terminated.")