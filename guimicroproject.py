import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Conversion functions
def convert_length(value, from_unit, to_unit):
    conversions = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "miles": 1609.34,
        "yards": 0.9144,
        "feet": 0.3048,
        "inches": 0.0254,
        "nautical miles": 1852,
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return value if to_unit == "Celsius" else (value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15)
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else value if to_unit == "Fahrenheit" else (value - 32) * 5/9 + 273.15
    else:  # Kelvin
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32 if to_unit == "Fahrenheit" else value

def convert_weight(value, from_unit, to_unit):
    conversions = {
        "kilograms": 1,
        "grams": 0.001,
        "milligrams": 0.000001,
        "pounds": 0.453592,
        "ounces": 0.0283495,
        "stones": 6.35029,
    }
    return value * conversions[from_unit] / conversions[to_unit]

def convert_volume(value, from_unit, to_unit):
    conversions = {
        "liters": 1,
        "milliliters": 0.001,
        "cubic meters": 1000,
        "cubic centimeters": 0.001,
        "gallons": 3.78541,
        "quarts": 0.946353,
        "pints": 0.473176,
        "cups": 0.24,
    }
    return value * conversions[from_unit] / conversions[to_unit]

# Main conversion function
def perform_conversion():
    try:
        value = float(entry_value.get())
        from_unit = combo_from.get()
        to_unit = combo_to.get()
        category = combo_category.get()
        
        if category == "Length":
            result = convert_length(value, from_unit, to_unit)
        elif category == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        elif category == "Weight":
            result = convert_weight(value, from_unit, to_unit)
        elif category == "Volume":
            result = convert_volume(value, from_unit, to_unit)
        else:
            result = "Error: Unsupported category"
        
        label_result.config(text=f"Result: {result:.2f} {to_unit}")
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Update unit options based on selected category
def update_units(event=None):
    category = combo_category.get()
    units = []
    
    if category == "Length":
        units = ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches", "nautical miles"]
    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
    elif category == "Weight":
        units = ["kilograms", "grams", "milligrams", "pounds", "ounces", "stones"]
    elif category == "Volume":
        units = ["liters", "milliliters", "cubic meters", "cubic centimeters", "gallons", "quarts", "pints", "cups"]
    
    combo_from['values'] = units
    combo_to['values'] = units
    combo_from.current(0)
    combo_to.current(1)

# GUI setup
window = tk.Tk()
window.title("Enhanced Unit Converter")
window.geometry("500x500")
window.configure(bg="#f0f4fa")
window.resizable(False, False)

# UI Components with styling
style = ttk.Style()
style.configure("TLabel", font=("Arial", 10))
style.configure("TButton", font=("Arial", 10), background="#4CAF50", foreground="white")
style.configure("TCombobox", padding=5)

label_title = ttk.Label(window, text="Unit Converter", font=("Arial", 16, "bold"), background="#f0f4fa", foreground="#333")
label_title.pack(pady=10)

label_category = ttk.Label(window, text="Select Category:", background="#f0f4fa")
label_category.pack(pady=5)

combo_category = ttk.Combobox(window, values=["Length", "Temperature", "Weight", "Volume"], state="readonly", font=("Arial", 10))
combo_category.pack(pady=5)
combo_category.current(0)
combo_category.bind("<<ComboboxSelected>>", update_units)

label_value = ttk.Label(window, text="Enter Value:", background="#f0f4fa")
label_value.pack(pady=5)

entry_value = ttk.Entry(window, width=20, font=("Arial", 10))
entry_value.pack(pady=5)

label_from = ttk.Label(window, text="From Unit:", background="#f0f4fa")
label_from.pack(pady=5)

combo_from = ttk.Combobox(window, state="readonly", font=("Arial", 10))
combo_from.pack(pady=5)

label_to = ttk.Label(window, text="To Unit:", background="#f0f4fa")
label_to.pack(pady=5)

combo_to = ttk.Combobox(window, state="readonly", font=("Arial", 10))
combo_to.pack(pady=5)

button_convert = ttk.Button(window, text="Convert", command=perform_conversion)
button_convert.pack(pady=15)

label_result = ttk.Label(window, text="Result: ", font=("Arial", 12), background="#f0f4fa", foreground="#333")
label_result.pack(pady=10)

update_units()  # Initialize the unit options

# Run the application
window.mainloop()