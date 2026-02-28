# import time
# import schedule
# from plyer import notification

# def remind_to_drink_water():
#     notification.notify(
#         title='Drink Water Reminder',
#         message="It's time to drink water!",
#         app_name='Water Reminder',
#         app_icon="C:\\Users\\Deepak\\OneDrive\\Desktop\\Python\\PROJECTS\\project_11\\jal_pi_lijeye.ico",
#         timeout=10  # duration in seconds
#     )

# # Schedule the reminder every hour
# schedule.every(10).seconds.do(remind_to_drink_water)

# print("Water reminder started. You will get a reminder every hour.")

# while True:
#     schedule.run_pending()
#     time.sleep(1)

# import time
# import schedule
# from win10toast_click import ToastNotifier

# # Function to show the notification
# def remind_to_drink_water():
#     toaster = ToastNotifier()
#     toaster.show_toast(
#         "Water Reminder",
#         "It's time to drink water!",
#         icon_path="C://Users//Deepak//OneDrive//Desktop//Python//PROJECTS//project_11//pure-water-icon-isolated-png.ico",  # Path to your custom icon file, e.g., 'icon.ico'
#         duration=10,
#         threaded=True
#     )
#     while toaster.notification_active():
#         time.sleep(0.1)

# # Schedule the reminder every minute for testing
# schedule.every(10).seconds.do(remind_to_drink_water)  # Adjust to .hour for the final version

# print("Water reminder started. You will get a reminder every 10 seconds for testing.")

# # Run the schedule in an infinite loop
# while True:
#     schedule.run_pending()
#     time.sleep(1)

# import time
# import schedule
# import tkinter as tk
# from PIL import Image, ImageTk

# def remind_to_drink_water():
#     root = tk.Tk()
#     root.title("Drink Water Reminder")

#     # Load image
#     image_path = "C:\\Users\\Deepak\\OneDrive\\Desktop\\Python\\PROJECTS\\project_11\\jal_pi_lijeye.png"
#     image = Image.open(image_path)
#     image = image.resize((300, 300), Image.LANCZOS)
#     photo = ImageTk.PhotoImage(image)

#     # Create a Label with image
#     label = tk.Label(root, image=photo)
#     label.image = photo
#     label.pack()

#     # Create a Label with text
#     text_label = tk.Label(root, text="Jal Pii Lijeye..Thak Gaye Honge Aap!", font=("Arial", 16))
#     text_label.pack()

#     # Auto-close after 10 seconds
#     root.after(10000, root.destroy)

#     # Run the tkinter loop
#     root.mainloop()

# # Schedule the reminder every 10 seconds for testing purposes
# schedule.every(10).seconds.do(remind_to_drink_water)

# print("Water reminder started. You will get a reminder every 10 seconds.")

# while True:
#     schedule.run_pending()
#     time.sleep(1)

import time
import schedule
import tkinter as tk
from PIL import Image, ImageTk
import keyboard
import atexit
running_reminder=True

def remind_to_drink_water():
    root = tk.Tk()
    root.title("Drink Water Reminder")
    # Remove window decorations (title bar, close button, etc.)
    root.overrideredirect(1)
    # Get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # Window width and height
    window_width = 350
    window_height = 350
    # Calculate position to place window at bottom right corner
    x = screen_width - window_width - 10  # 10 pixels from the right edge
    y = screen_height - window_height - 50  # 50 pixels from the bottom edge
    # Set window geometry
    root.geometry(f'{window_width}x{window_height}+{x}+{y}')
    # Load image
    image_path = "C:\\Users\\Deepak\\OneDrive\\Desktop\\Python\\PROJECTS\\project_11\\jal_pi_lijeye.png"
    image = Image.open(image_path)
    image = image.resize((300, 300), Image.LANCZOS)
    photo = ImageTk.PhotoImage(image)
    # Create a Label with image
    label = tk.Label(root, image=photo)
    label.image = photo
    label.pack()
    # Create a Label with text
    text_label = tk.Label(root, text="Jal Pii Lijeye Thak Gye Honge Aap", font=("Arial", 16))
    text_label.pack()
    # Auto-close after 10 seconds
    root.after(10000, root.destroy)
    # Run the tkinter loop
    root.mainloop()

def stop_pressing_key(e):
    global running_reminder
    running_reminder=False
    print("Reminders will start on the next logging")

# Schedule the reminder every 10 seconds for testing purposes
schedule.every().hour.do(remind_to_drink_water)
print("Water reminder started. You will get a reminder every hour.")
keyboard.on_press_key("F12",stop_pressing_key)

def on_exit():
    global running_reminder
    running_reminder=True
atexit.register(on_exit)

while True:
    if running_reminder:
        schedule.run_pending()
    time.sleep(1)
