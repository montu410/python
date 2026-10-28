
import time
from datetime import datetime
import tkinter as tk
from tkinter import messagebox
import threading

try:
    import winsound
except ImportError:
    winsound = None


def ring_alarm():
    """Play an alarm sound."""
    if winsound:
        while alarm_active[0]:
            winsound.Beep(1000, 700)
            time.sleep(0.3)
    else:
        # Fallback for systems without winsound
        print("\a", end="", flush=True)
        while alarm_active[0]:
            time.sleep(1)


def set_alarm():
    try:
        hour = int(hour_entry.get())
        minute = int(minute_entry.get())
        second = int(second_entry.get())

        if not (0 <= hour <= 23 and
                0 <= minute <= 59 and
                0 <= second <= 59):
            raise ValueError

        alarm_time = f"{hour:02d}:{minute:02d}:{second:02d}"
        status_label.config(text=f"Alarm set for {alarm_time}")
        check_alarm(alarm_time)

    except ValueError:
        messagebox.showerror(
            "Invalid Time",
            "Enter a valid hour (0-23), minute (0-59), "
            "and second (0-59)."
        )


def check_alarm(alarm_time):
    current_time = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=f"Current Time: {current_time}")

    if current_time == alarm_time:
        status_label.config(text="ALARM RINGING!")
        alarm_active[0] = True
        threading.Thread(
            target=ring_alarm, daemon=True
        ).start()
        messagebox.showinfo("Alarm", "Your alarm is ringing!")
        alarm_active[0] = False
        status_label.config(text="Alarm stopped")
        return

    root.after(200, check_alarm, alarm_time)


def update_clock():
    current_time = datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=f"Current Time: {current_time}")
    root.after(200, update_clock)


def stop_alarm():
    alarm_active[0] = False
    status_label.config(text="Alarm stopped")


root = tk.Tk()
root.title("Python Alarm Clock")
root.geometry("350x300")
root.resizable(False, False)

alarm_active = [False]

tk.Label(
    root, text="ALARM CLOCK",
    font=("Arial", 20, "bold")
).pack(pady=10)

clock_label = tk.Label(
    root, text="", font=("Arial", 14)
)
clock_label.pack(pady=5)

tk.Label(
    root, text="Set alarm (24-hour format)"
).pack(pady=5)

input_frame = tk.Frame(root)
input_frame.pack()

hour_entry = tk.Entry(input_frame, width=5, justify="center")
hour_entry.insert(0, "07")
hour_entry.pack(side="left", padx=3)

tk.Label(input_frame, text=":").pack(side="left")

minute_entry = tk.Entry(input_frame, width=5, justify="center")
minute_entry.insert(0, "00")
minute_entry.pack(side="left", padx=3)

tk.Label(input_frame, text=":").pack(side="left")

second_entry = tk.Entry(input_frame, width=5, justify="center")
second_entry.insert(0, "00")
second_entry.pack(side="left", padx=3)

tk.Button(
    root, text="Set Alarm",
    command=set_alarm
).pack(pady=10)

tk.Button(
    root, text="Stop Alarm",
    command=stop_alarm
).pack(pady=3)

status_label = tk.Label(root, text="No alarm set")
status_label.pack(pady=5)

update_clock()
root.mainloop()
