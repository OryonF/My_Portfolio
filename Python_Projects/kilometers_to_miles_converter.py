################################################################################

# Program Name: Kilometres to miles converter

# Author Name: Oryon J. Facey

# Date: 29 November 2024

# Description: Displaying kilometres to miles

###############################################################################

#imports

import sys

from tkinter import *

#from tkinter.ttk import *

#functions

def converter(_event = None):

    try:

        current_speed_measurement = radvar.get()

        speed_then = float(speed_text_entry.get())

        if float(speed_text_entry.get()) > 0:

            if current_speed_measurement == "kilometres":

                speed_now = speed_then / 1.609344

                convert_output.configure(text = f"Your speed in kilometres converted is {speed_now:.2f} miles")

            else:

                speed_now = speed_then * 1.609344

                convert_output.configure(text = f"Your speed in miles converted is {speed_now:.2f} kilometres")
        else:
            convert_output.configure(text="ERROR: input must be greater than zero")
    except:

            convert_output.configure(text = "ERROR: input must be numeric")

def close_it (_event = None):

    sys.exit()

def reset_it (_event = None):

    speed_text_entry.delete(0, END)

    convert_output.configure(text = "")

    radvar.set("kilometres")

#Declarations, widgets and sizing

window = Tk()

window.geometry("700x500")

window.title("kilometres to miles")

radvar = StringVar()

radvar.set("kilometres")

measurement_of_speed = Label(window, text = "Choose you measurement of speed:")

kilometres = Radiobutton(window, text = "kilometres", value = "kilometres", variable = radvar)

miles = Radiobutton(window, text = "miles", value = "miles", variable = radvar)

speed = Label(window, text = "Speed:")

converted_value = Label(window, text = "converted value:")

speed_text_entry = Entry(window, width = 50)

destination_text_entry = Entry(window, width = 50)

convert_output = Label(window, bd = 2, relief = SUNKEN, width= 63)

convert = Button(window, text = "convert", command = converter, width = 15)

reset = Button(window, text = "Reset", command = reset_it, width = 15)

close = Button(window, text = "Close", command = close_it, width = 15)

# Location of widgets

measurement_of_speed.grid(row = 0, column = 0, padx= 10, pady= 10, sticky = E)

kilometres.grid(row = 0, column = 1)

miles.grid(row = 0, column = 2)

speed.grid(row = 1, column = 0, padx= 10, pady= 10, sticky = E)

converted_value.grid(row = 2, column = 0, padx= 10, pady= 10, sticky = E)

speed_text_entry.grid(row = 1, column = 1, padx= 10, pady= 10, sticky = W)

convert_output.grid(row = 2, column = 1, padx= 10, pady= 10, sticky = W, columnspan = 2)

convert.grid(row = 3, column = 0, padx= 10, pady= 10, sticky = E)

reset.grid(row= 3, column = 2, padx= 10, pady= 10, sticky = E)

close.grid(row = 4, column = 2, padx= 10, pady= 10, sticky = E)

window.mainloop()