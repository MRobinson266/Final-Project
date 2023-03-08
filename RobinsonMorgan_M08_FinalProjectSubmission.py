"""
Author:  Morgan Robinson
Date written: 03/08/23
Assignment:   Module 8 Final Project Submission
"""

from tkinter import *
import tkinter as tk
from tkinter.ttk import *

import random
        
def roll_dice():
    dice_type_input = float(dice_type_entry.get())
    num_dice_input = int(dice_num_entry.get())
    end = 0
    roll_dice.total = 0

    while end < num_dice_input:
    # Roll d4
        if dice_type_input == 4:
            roll = random.randint(1, 4)
            roll_dice.total += roll
            end += 1
    # Roll d6
        elif dice_type_input == 6:
            roll = random.randint(1, 6)
            roll_dice.total += roll
            end += 1
    # Roll d8
        elif dice_type_input == 8:
            roll = random.randint(1, 8)
            roll_dice.total += roll
            end += 1
    # Roll d10
        elif dice_type_input == 10:
            roll = random.randint(1, 10)
            roll_dice.total += roll
            end += 1
    # Roll d12
        elif dice_type_input == 12:
            roll = random.randint(1, 12)
            roll_dice.total += roll
            end += 1
    # Roll d20
        elif dice_type_input == 20:
            roll = random.randint(1, 20)
            roll_dice.total += roll
            end += 1
    # Error Incorrect Input
        else:
            roll_dice.total = "Please enter a valid dice type."
    
    dice_roll_label.config(text= roll_dice.total)

# function to open a new window on a button click
def modifierWindow():
    # Toplevel object which will be treated as a new window
    newWindow = tk.Toplevel()
     # sets the title of the Toplevel widget
    newWindow.title("Add Modifier")
     # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # Create label to display instructions
    modifier_label = tk.Label(newWindow, text="What is your modifier?")
    modifier_label.pack()

    # Create an entry widget for the user to enter the temperature in Celsius
    modifierWindow.modifier_entry = tk.Entry(newWindow)
    modifierWindow.modifier_entry.pack()
    
    # Create a button to trigger adding the modifier
    modifier_button = tk.Button(newWindow, text="Add Modifier to Roll", command=add_modifier)
    modifier_button.pack()
    # Create an exitbutton
    exit_button = tk.Button(newWindow, text ="exit", command = newWindow.quit)
    exit_button.pack()

    # Create a label to display the result
    modifierWindow.result_label = tk.Label(newWindow, text="")
    modifierWindow.result_label.pack()

def add_modifier():
    modifier = float(modifierWindow.modifier_entry.get())
    outcome = modifier + roll_dice.total

    modifierWindow.result_label.config(text= outcome)

# Create App Windows
# creates master object
master = tk.Tk()
master.title("DnD Dice Roller")
# sets the geometry of main root window
master.geometry("350x200")

# Create labels and entry to choose type and number of dice
dice_type_label = tk.Label(master, text="How many sides do you want? (4, 6, 8, 10, 12, 20)")
dice_type_label.pack()
dice_type_entry = tk.Entry(master)
dice_type_entry.pack()

dice_num_label = tk.Label(master, text="How many dice do you want rolled?")
dice_num_label.pack()
dice_num_entry = tk.Entry(master)
dice_num_entry.pack()

# Create a button to trigger a roll
roll_button = tk.Button(master, text="Roll", command=roll_dice)
roll_button.pack()
# Create a button to trigger a reroll
reroll_button = tk.Button(master, text="Reroll?", command=roll_dice)
reroll_button.pack()
# a button widget which will open the modifier window on button click
add_modifier_button = tk.Button(master, text ="Add Modifier?", command = modifierWindow)
add_modifier_button.pack()
# Create an exit button
exit_button = tk.Button(master, text ="exit", command = master.quit)
exit_button.pack()

# Create a label to display the result
dice_roll_label = tk.Label(master, text="")
dice_roll_label.pack()

# mainloop, runs infinitely
master.mainloop()

dice_type_input = float(dice_type_entry.get())
num_dice_input = int(dice_num_entry.get())
