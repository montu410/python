import tkinter as tk
from time import strftime


def update_clock() -> None:
    """Refresh the displayed time once per second."""
    time_label.config(text=strftime("%H:%M:%S"))
    root.after(1000, update_clock)


root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x120")
root.resizable(False, False)

time_label = tk.Label(
    root,
    font=("Arial", 40, "bold"),
    background="#1e1e1e",
    foreground="#00ff99",
)
time_label.pack(expand=True, fill="both")

update_clock()
root.mainloop()