#Common GUI functions for Pop-Ups and Widgets in Tkinter, Fast and Easy to Use

#Import GUI modules for GUI elements
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

def show_error(title, error_message):
    """Show a GUI error message."""

    box = Tk() #Create Tkinter Window Object
    box.withdraw() #Hide Tkinter Window Object
    messagebox.showerror(title, error_message) #Show pop up
    box.destroy()

def show_warning(title, warning_message):
    """Shows a GUI warning message."""
    
    box = Tk()
    box.withdraw()
    messagebox.showwarning(title, warning_message)
    box.destroy()

def show_info(title, info_message):
    """Shows info to the user in a alert window."""

    box = Tk()
    box.withdraw()
    messagebox.showinfo(title, info_message)
    box.destroy()

def ok_or_cancel(title, question):
    """Pops up a GUI alert window that asks the user to aprove or cancel a process.

    It returns True if user clicks OK, it returns False if user clicks cancel."""

    box = Tk()
    box.withdraw()
    box.destroy()

    #Return user's answer (True/False)
    return messagebox.askokcancel(title,question)

def yes_or_no(title,question):
    """Pops up a GUI alert window that asks a yes or no question to the user.

    It returns True if user clicks yes, it returns False if user clicks no."""

    box = Tk()
    box.withdraw()
    box.destroy()

    #Return user's answer (True/False)
    return messagebox.askyesno(title,question)


def try_or_not(title,question):
    """Pops up a GUI alert window that asks user to retry something.

    It returns True if user clicks Retry, it returns False if user clicks Cancel.

    It has a warning symbol, so use only for those purposes."""

    box = Tk()
    box.withdraw()
    box.destroy()

    #Return user's answer
    return messagebox.askretrycancel(title, question)


#Tell the user what this module is about and that it should not be run directly

if __name__ == "__main__":
    show_warning("Import Warning",
                 "This module contains short hand functions for Tkinter GUI pop-ups." \
                 + "\n\nThis module IS NOT MEANT TO BE RUN DIRECTLY." \
                 + "\nPlease, IMPORT IT IN ANOTHER FILE.")
