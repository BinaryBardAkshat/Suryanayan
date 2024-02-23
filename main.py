import os
import cv2
import numpy as np
from nanogps import NanoGPS
from sklearn.externals import joblib  # Use joblib for model persistence
from telegram import Bot
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables from .env file
load_dotenv()

# Initialize Nano GPS module
gps = NanoGPS()

# Load trained model
model = joblib.load('trained_model.pkl')  

# Initialize Telegram Bot
bot = Bot(token=os.getenv("TELEGRAM_BOT_TOKEN"))

# Function to capture image from camera
def capture_image():
    
    return captured_image

# Function to detect issue using the trained model
def detect_issue(image):
 
    flattened_image = image.reshape(1, -1)


    issue = model.predict(flattened_image)[0]
    return issue

# Function to send data to Telegram bot
def send_data_to_telegram_bot(issue, coordinates):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message = f"Issue detected: {issue}\nCoordinates: {coordinates}\nTimestamp: {timestamp}"
    bot.send_message(chat_id=os.getenv("TELEGRAM_CHAT_ID"), text=message)

# Main function
def main():
    while True:
        # Capture image from camera
        image = capture_image()

        # Get GPS coordinates
        latitude, longitude = gps.get_latitude_longitude()

        # Detect issue using the trained model
        issue = detect_issue(image)

        # Send data to Telegram 
        send_data_to_telegram_bot(issue, (latitude, longitude))

      
        time.sleep(100)

# Run the main function
if __name__ == "__main__":
    main()

