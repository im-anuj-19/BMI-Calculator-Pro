import tkinter as tk
from tkinter import ttk, messagebox

from bmi import calculate_bmi, get_bmi_category
from validation import validate_inputs

class BMICalculator:

    def __init__(self, root):
        self.root = root
        self.root.title("BMI Calculator Pro v1.0")
        self.root.geometry("520x600")
        self.root.resizable(False, False)
        self.root.configure(bg="#EAF4FC")

        self.create_widgets()

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="BMI Calculator Pro",
            font=("Segoe UI", 22, "bold"),
            bg="#EAF4FC",
            fg="#0F4C81"
        )
        title.pack(pady=15)

        frame = tk.Frame(
            self.root,
            bg="white",
            bd=2,
            relief="ridge"
        )
        frame.pack(padx=20, pady=10, fill="both", expand=True)

        # Weight
        tk.Label(
            frame,
            text="Weight",
            font=("Segoe UI", 11, "bold"),
            bg="white"
        ).pack(pady=(20, 5))

        weight_frame = tk.Frame(frame, bg="white")
        weight_frame.pack()

        self.weight_entry = ttk.Entry(weight_frame, width=18)
        self.weight_entry.pack(side="left", padx=5)

        self.weight_unit = ttk.Combobox(
            weight_frame,
            values=["kg", "lbs"],
            width=8,
            state="readonly"
        )
        self.weight_unit.current(0)
        self.weight_unit.pack(side="left")

        # Height
        tk.Label(
            frame,
            text="Height",
            font=("Segoe UI", 11, "bold"),
            bg="white"
        ).pack(pady=(20, 5))

        height_frame = tk.Frame(frame, bg="white")
        height_frame.pack()

        self.height_entry = ttk.Entry(height_frame, width=18)
        self.height_entry.pack(side="left", padx=5)

        self.height_unit = ttk.Combobox(
            height_frame,
            values=["m", "cm", "ft"],
            width=8,
            state="readonly"
        )
        self.height_unit.current(0)
        self.height_unit.pack(side="left")

        ttk.Button(
            frame,
            text="Calculate BMI",
            command=self.calculate
        ).pack(pady=20)

        ttk.Button(
            frame,
            text="Reset",
            command=self.reset
        ).pack()

        ttk.Separator(frame).pack(fill="x", pady=20)

        self.result_label = tk.Label(
            frame,
            text="BMI : --",
            font=("Segoe UI", 18, "bold"),
            bg="white"
        )
        self.result_label.pack()

        self.category_label = tk.Label(
            frame,
            text="Category : --",
            font=("Segoe UI", 14),
            bg="white"
        )
        self.category_label.pack(pady=5)

        self.advice_label = tk.Label(
            frame,
            text="Enter your details to calculate BMI.",
            font=("Segoe UI", 11),
            bg="white",
            fg="gray",
            wraplength=420,
            justify="center"
        )
        self.advice_label.pack(pady=15)

        self.range_label = tk.Label(
            frame,
            text="Healthy Weight Range : --",
            font=("Segoe UI", 11, "bold"),
            bg="white",
            fg="#0F4C81"
        )
        self.range_label.pack()

        tk.Label(
            self.root,
            text="Developed using Python & Tkinter",
            bg="#EAF4FC",
            fg="gray"
        ).pack(pady=10)

    def calculate(self):

        try:
            weight = float(self.weight_entry.get())
            height = float(self.height_entry.get())

        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter valid numeric values."
            )
            return

        if self.weight_unit.get() == "lbs":
            weight *= 0.453592

        if self.height_unit.get() == "cm":
            height /= 100

        elif self.height_unit.get() == "ft":
            height *= 0.3048

        valid, msg = validate_inputs(weight, height)

        if not valid:
            messagebox.showerror("Error", msg)
            return

        bmi = calculate_bmi(weight, height)

        category, advice = get_bmi_category(bmi)

        self.result_label.config(text=f"BMI : {bmi}")

        self.category_label.config(text=f"Category : {category}")

        self.advice_label.config(text=advice)

        lower = round(18.5 * height * height, 1)
        upper = round(24.9 * height * height, 1)

        self.range_label.config(
            text=f"Healthy Weight Range : {lower} kg - {upper} kg"
        )

        colors = {
            "Underweight": "#3498DB",
            "Normal": "#27AE60",
            "Overweight": "#F39C12",
            "Obese": "#E74C3C"
        }

        self.result_label.config(
            fg=colors.get(category, "black")
        )

    def reset(self):

        self.weight_entry.delete(0, tk.END)
        self.height_entry.delete(0, tk.END)

        self.weight_unit.current(0)
        self.height_unit.current(0)

        self.result_label.config(
            text="BMI : --",
            fg="black"
        )

        self.category_label.config(
            text="Category : --"
        )

        self.advice_label.config(
            text="Enter your details to calculate BMI."
        )

        self.range_label.config(
            text="Healthy Weight Range : --"
        )


if __name__ == "__main__":
    root = tk.Tk()
    BMICalculator(root)
    root.mainloop()