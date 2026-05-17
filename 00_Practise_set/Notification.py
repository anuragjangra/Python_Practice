import time
from plyer import notification

while True:  # Send notification every 1 minute for 5 times
    notification.notify(
        title="Please Drink Water",
        message="It's important to stay hydrated! Remember to drink water regularly throughout the day.",
        timeout=10
    )
    time.sleep(10)  # Wait for 1 minute before sending the next notification
