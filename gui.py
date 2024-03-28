import tkinter as tk
from tkinter import ttk
import subprocess

victim_input = ""

def switch_window():
    global victim_input
    victim_input = victim_entry.get()
    if victim_input:
        first_window.withdraw()
        second_window.deiconify()
        victim_label.config(text="Victim: " + victim_input)

def perform_command():
    vals = ["LinPeas Enumeration", "Linux Exploit Suggester", "Port Status Check","HTTP enumeration","Packet Filter Detection","Load Balancer Output","Running Service Exploits","Host Open Ports Detection","XSS Forgery Detection Output","SQL Injection Detection","Anonymous FTP Login Detection"]
    args = []
    string = ''
    for option, var in option_vars.items():
        if var.get():
            args.append(option)
    for arg in args:
        string += str(vals.index(arg)) + ' '
    subprocess.run(['sudo','python3','pmaker.py',victim_input,string]).stdout

# First Window
first_window = tk.Tk()
first_window.title("Vulnerability Scanner")
first_window.geometry("400x400")


placeholder_image = tk.PhotoImage(file="temp/img.png")  
image_label = tk.Label(first_window, image=placeholder_image)
image_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

victim_label = tk.Label(first_window, text="Victim")
victim_label.grid(row=1, column=0, sticky="e", padx=5, pady=5)

victim_entry = tk.Entry(first_window)
victim_entry.grid(row=1, column=1, sticky="w", padx=5, pady=5)

submit_button = tk.Button(first_window, text="Submit", command=switch_window)
submit_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

# Second Window
second_window = tk.Toplevel(first_window)
second_window.title("Vulnerability Scanner")
second_window.geometry("400x400")
second_window.withdraw()  # Hide the window initially

option_vars = {}

option_list = ["LinPeas Enumeration", "Linux Exploit Suggester", "Port Status Check","HTTP enumeration","Packet Filter Detection","Load Balancer Output","Running Service Exploits","Host Open Ports Detection","XSS Forgery Detection Output","SQL Injection Detection","Anonymous FTP Login Detection"]

for i, option in enumerate(option_list):
    option_var = tk.BooleanVar(value=False)
    option_checkbutton = ttk.Checkbutton(second_window, text=option, variable=option_var)
    option_vars[option] = option_var
    option_checkbutton.grid(row=i, column=0, sticky="w", padx=5, pady=5)

perform_button = tk.Button(second_window, text="Perform Command", command=perform_command)
perform_button.grid(row=len(option_list), column=0, columnspan=2, padx=5, pady=5)

first_window.mainloop()
