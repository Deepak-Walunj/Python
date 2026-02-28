import time
import schedule
from plyer import notification

def remind_to_drink_water():
    notification.notify(
        title='Drink Water Reminder',
        message="It's time to drink water!",
        app_name='Water Reminder',
        timeout=10  # duration in seconds
    )

# Schedule the reminder every hour
schedule.every(10).seconds.do(remind_to_drink_water)

print("Water reminder started. You will get a reminder every hour.")

while True:
    schedule.run_pending()
    time.sleep(1)