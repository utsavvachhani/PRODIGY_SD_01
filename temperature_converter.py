import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def celsius_to_kelvin(c):
    return c + 273.15

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def fahrenheit_to_kelvin(f):
    return fahrenheit_to_celsius(f) + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def kelvin_to_fahrenheit(k):
    return celsius_to_fahrenheit(kelvin_to_celsius(k))

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PRODIGY INFOTECH - Temperature Converter")

        # Title label
        self.title_label = ttk.Label(root, text="Temperature Converter", font=("Helvetica", 16, "bold"))
        self.title_label.grid(column=0, row=0, columnspan=3, padx=10, pady=10)

        # Temperature input
        self.temp_label = ttk.Label(root, text="Enter Temperature:")
        self.temp_label.grid(column=0, row=1, padx=10, pady=10)

        self.temp_entry = ttk.Entry(root)
        self.temp_entry.grid(column=1, row=1, padx=10, pady=10)

        # Unit selection
        self.unit_var = tk.StringVar()

        self.celsius_radio = ttk.Radiobutton(root, text="Celsius", variable=self.unit_var, value="C")
        self.celsius_radio.grid(column=0, row=2, padx=10, pady=5)

        self.fahrenheit_radio = ttk.Radiobutton(root, text="Fahrenheit", variable=self.unit_var, value="F")
        self.fahrenheit_radio.grid(column=1, row=2, padx=10, pady=5)

        self.kelvin_radio = ttk.Radiobutton(root, text="Kelvin", variable=self.unit_var, value="K")
        self.kelvin_radio.grid(column=2, row=2, padx=10, pady=5)

        # Convert button
        self.convert_button = ttk.Button(root, text="Convert", command=self.convert_temperature)
        self.convert_button.grid(column=0, row=3, columnspan=3, padx=10, pady=10)

        # Result labels
        self.result_label_c = ttk.Label(root, text="")
        self.result_label_c.grid(column=0, row=4, columnspan=3, padx=10, pady=5)

        self.result_label_f = ttk.Label(root, text="")
        self.result_label_f.grid(column=0, row=5, columnspan=3, padx=10, pady=5)

        self.result_label_k = ttk.Label(root, text="")
        self.result_label_k.grid(column=0, row=6, columnspan=3, padx=10, pady=5)

    def convert_temperature(self):
        try:
            temp = float(self.temp_entry.get())
            unit = self.unit_var.get()

            if unit == "C":
                temp_f = celsius_to_fahrenheit(temp)
                temp_k = celsius_to_kelvin(temp)
                self.result_label_c.config(text=f"{temp} °C")
                self.result_label_f.config(text=f"{temp_f:.2f} °F")
                self.result_label_k.config(text=f"{temp_k:.2f} K")
            elif unit == "F":
                temp_c = fahrenheit_to_celsius(temp)
                temp_k = fahrenheit_to_kelvin(temp)
                self.result_label_c.config(text=f"{temp_c:.2f} °C")
                self.result_label_f.config(text=f"{temp} °F")
                self.result_label_k.config(text=f"{temp_k:.2f} K")
            elif unit == "K":
                temp_c = kelvin_to_celsius(temp)
                temp_f = kelvin_to_fahrenheit(temp)
                self.result_label_c.config(text=f"{temp_c:.2f} °C")
                self.result_label_f.config(text=f"{temp_f:.2f} °F")
                self.result_label_k.config(text=f"{temp} K")
            else:
                self.result_label_c.config(text="Select a unit")
                self.result_label_f.config(text="")
                self.result_label_k.config(text="")
        except ValueError:
            self.result_label_c.config(text="Invalid input")
            self.result_label_f.config(text="")
            self.result_label_k.config(text="")

if __name__ == "__main__":
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
