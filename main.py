# Importing Necessary Modules
from tkinter import *
import sounddevice as sd

from microphone import microphone_control
from func import startMeetAHK, startDiscordAHK, startTeamsAHK, startZoomAHK


duration = 100000  # seconds

# Create Object
root = Tk()
root.title('MicroPy')
root.geometry("800x500")

option = input("Hello There......What would you like to choose \n 1. Google Meet 2. Microsoft Teams 3. Discord 4. Zoom")

if option == 1:
  startMeetAHK()
elif option == 2:
  startTeamsAHK()
elif option == 3:
  startDiscordAHK()
elif option == 4:
  startZoomAHK()
else:
  print("Sorry Invalid Option!")
  

# Keep track of the button state on/off
is_on = False

# Create Label
my_label = Label(root,
                 text="MicroPy Is turned Off!",
                 fg="grey",
                 font=("Helvetica", 20))

my_label.pack(pady=20)

# Defining our switch function


def switch():
    global is_on

    # Determining if switch is on or off
    if is_on:
        on_button.config(image=off)
        my_label.config(text="MicroPy is turned Off",
                        fg="grey")

        is_on = False

    else:

        on_button.config(image=on)
        my_label.config(text="MicroPy is turned On", fg="black")

        is_on = True


# Defining the Images
on = PhotoImage(file="assets/on.png")
off = PhotoImage(file="assets/off.png")


# Create A Button
on_button = Button(root, image=off, bd=0,
                   command=switch)
on_button.pack(pady=50)

# Execute Tkinter
root.mainloop()
