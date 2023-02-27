"""
Author:  Morgan Robinson
Date written: 02/27/23
Assignment:   Module 6 Project Introduction and Project Status Report II
"""

from tkinter import *
from tkinter.ttk import *

import random

def main(dice_type_entry, dice_num_entry):
    dice_type_input = float(dice_type_entry.get())
    num_dice_input = float(dice_num_entry.get())
    # Roll the dice
    roll_results = roll_dice(num_dice_input)
        
def roll_dice(num_dice_input, dice_type_input):
    roll_results = []
    # Roll d4
    if dice_type_input = "d4" or "D4":
        for _ in range(num_dice_input):
            roll = random.randint(1, 4)
            roll_results.append(roll)
        return roll_results
    # Roll d6
    if dice_type_input = "d6" or "D6":
        for _ in range(num_dice_input):
            roll = random.randint(1, 6)
            roll_results.append(roll)
        return roll_results
    # Roll d8
    if dice_type_input = "d8" or "D8":
        for _ in range(num_dice_input):
            roll = random.randint(1, 8)
            roll_results.append(roll)
        return roll_results
    # Roll d10
    if dice_type_input = "d10" or "D10":
        for _ in range(num_dice_input):
            roll = random.randint(1, 10)
            roll_results.append(roll)
        return roll_results
    # Roll d12
    if dice_type_input = "d12" or "D12":
        for _ in range(num_dice_input):
            roll = random.randint(1, 12)
            roll_results.append(roll)
        return roll_results
    # Roll d20
    if dice_type_input = "d20" or "D20":
        for _ in range(num_dice_input):
            roll = random.randint(1, 20)
            roll_results.append(roll)
        return roll_results


# Create App Windows
def master()
    # creates master object
    master = Tk()
    # sets the geometry of main root window
    master.geometry("200x200")

    # Create labels to choose type and number of dice
    dice_type_label = Label(master, text="What type of dice do you want? (D4, D6, D8, D10, D12, D20)")
    dice_type_label.pack()
    dice_num_label = Label(master, text="How many dice do you want rolled? (1-10)")
    dice_num_label.pack()

    # Create entry widgets for the user to enter type and number
    dice_type_entry = Entry(master)
    dice_type_label.pack()
    dice_num_entry = Entry(master)
    dice_num_label.pack()

    # Create a button to trigger a roll
    roll_button = Button(master, text="Roll", command=roll_dice)
    roll_button.pack()
    # Create a button to trigger a reroll
    reroll_button = Button(master, text="Reroll?", command=roll_dice)
    reroll_button.pack()
    # a button widget which will open the modifier window on button click
    add_modifier_button = Button(master, text ="Add Modifier?", command = modifierWindow)
    add_modifier_button.pack()
    # Create an exit button
    exit_button = Button(master, text ="exit", command = exit)
    exit_button.pack()

    # Create a label to display the result
    dice_roll_label = Label(master, text="")
    dice_roll_label.pack()

 
 
# function to open a new window on a button click
def modifierWindow():
    # Toplevel object which will be treated as a new window
    newWindow = Toplevel()
     # sets the title of the Toplevel widget
    newWindow.title("Add Modifier")
     # sets the geometry of toplevel
    newWindow.geometry("200x200")
 
    # Create label to display instructions
    modifier_label = Label(newWindow, text="What is your modifier?")
    modifier_label.pack()

    # Create an entry widget for the user to enter the temperature in Celsius
    modifier_entry = Entry(newWindow)
    modifier_entry.pack()
    
    # Create a button to trigger adding the modifier
    modifier_button = Button(newWindow, text="Add Modifier to Roll", command=add_modifier)
    modifier_button.pack()
    # Create an exitbutton
    exit_button = Button(newWindow, text ="exit", command = exit)
    exit_button.pack()

    # Create a label to display the result
    result_label = Label(newWindow, text="")
    result_label.pack()
 
 
# mainloop, runs infinitely
mainloop()


