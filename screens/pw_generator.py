import customtkinter as ctk
import random
import string
from utils import calculate_entropy, get_strength_label

class PWGenerator(ctk.CTkFrame):
    def __init__(self, parent, controller):
            super().__init__(parent, fg_color="#003FAA")
            self.controller=controller

            self.grid_rowconfigure(0, weight=1)
            self.grid_rowconfigure(6, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(2, weight=1)

            #Title
            ctk.CTkLabel(
                  self,
                  text="Password Generator",
                  font=("Helvetica", 50, "bold"),
            ).grid(row=1, column=1, pady=(0, 5))

            ctk.CTkLabel(
                  self,
                  text="Create a strong, secure password with custom options",
                  font=("Helvetica", 20),
                  text_color="gray"
            ).grid(row=2, column=1, pady=(0,20))

            card = ctk.CTkFrame(self, fg_color="#002080", corner_radius=16)
            card.grid(row=3, column=1, padx=20, pady=(0, 20), sticky="ew")
            card.grid_columnconfigure(0 ,weight=1)

            output_row = ctk.CTkFrame(card, fg_color="transparent")
            output_row.grid(row=0, column=0, padx=24, pady=(20, 4), sticky="ew")
            output_row.grid_columnconfigure(0, weight=1)

            ctk.CTkLabel(
                  output_row,
                  text="Generated Password:",
                  font=("Helvetica", 14),
                  anchor="w"
            ).grid(row=0, column=0, sticky="w")

            self.pw_output = ctk.CTkEntry(
                  card,
                  width=560, height=50,
                  placeholder_text="Click 'Generate' to create a password",
                  font=("Helvetica", 16),
                  state="readonly"
            )
            self.pw_output.grid(row=1, column=0, padx=24, pady=(0, 4), sticky="ew")

            #Entropy Label
            self.entropy_label = ctk.CTkLabel(
                  card,
                  text="",
                  font=("Helvetica", 15),
                  anchor="w"
            )
            self.entropy_label.grid(row=2, column=0, padx=24, pady=(0, 16), sticky="w")

            #'Copy to Clipboard' Button
            self.copy_btn = ctk.CTkButton(
                  card,
                  text="Copy to Clipboard",
                  width=200, height=40,
                  font=("Helvetica", 14),
                  command=self._copy_to_clipboard
            )
            self.copy_btn.grid(row=3, column=0, padx=24, pady=(0, 16), sticky="w")

            #Password Length Slider
            length_row = ctk.CTkFrame(card, fg_color="transparent")
            length_row.grid(row=4, column=0, padx=24, sticky="ew")
            length_row.grid_columnconfigure(0, weight=1)

            ctk.CTkLabel(
                  length_row,
                  text="Password Length",
                  font=("Helvetica", 14)
            ).grid(row=0, column=0, sticky="w")

            self.length_label = ctk.CTkLabel(
                  length_row,
                  text="16",
                  font=("Helvetica", 14, "bold"),
                  width=30
            )
            self.length_label.grid(row=0, column=1)


            self.length_slider = ctk.CTkSlider(
                  card,
                  from_=4, to=32,
                  number_of_steps=28,
                  command=self._update_length_label
            )
            self.length_slider.set(16)
            self.length_slider.grid(row=5, column=0, padx=24, pady=(4, 4), sticky="ew")

            ctk.CTkLabel(card, text="4", font=("Helvetica", 11), text_color="gray").grid(row=6, column=0, padx=28, sticky="w")
            ctk.CTkLabel(card, text="32", font=("Helvetica", 11), text_color="gray").grid(row=6, column=0, padx=28, sticky="e")

            #Checkboxes
            ctk.CTkLabel(
                  card,
                  text="Include Character",
                  font=("Helvetica", 14, "bold"),
                  anchor="w"
            ).grid(row=7, column=0, padx=24, pady=(16, 6), sticky="w")

            self.use_upper = self._make_checkbox(card, row=8, label="Uppercase Letters (A-Z)", default=True)
            self.use_lower = self._make_checkbox(card, row=9, label="Lowercase Letters (a-z)", default=True)
            self.use_numbers = self._make_checkbox(card, row=10, label="Numbers (0-9)", default=True)
            self.use_symbols = self._make_checkbox(card, row=11, label="Symbols (!@#$%^&*)", default=True)

            ctk.CTkButton(
                  card,
                  text="Generate Password",
                  width=560, height=50,
                  font=("Helvetica", 16, "bold"),
                  command=self._generate
            ).grid(row=12, column=0, padx=24, pady=(20, 24))

            #Back Button
            ctk.CTkButton(
                  self,
                  text="Back to Main Menu",
                  width=400, height=50,
                  border_width=1,
                  font=("Helvetica", 18),
                  fg_color="transparent",
                  command=lambda: self.controller.show_screen("MainMenu")
            ).place(x=20, rely=1.0, y=-20, anchor="sw")

    def _make_checkbox(self, parent, row, label, default):
        var = ctk.BooleanVar(value=default)
        ctk.CTkCheckBox(
            parent,
            text=label,
            variable=var,
            font=("Helvetica", 14)
        ).grid(row=row, column=0, padx=32, pady=3, sticky="w")
        return var

    def _update_length_label(self, value):
        self.length_label.configure(text=str(int(value)))

    def _generate(self):
        length = int(self.length_slider.get())
        pool, forced = "", []

        if self.use_upper.get():
            pool += string.ascii_uppercase
            forced.append(random.choice(string.ascii_uppercase))

        if self.use_lower.get():
            pool += string.ascii_lowercase
            forced.append(random.choice(string.ascii_lowercase))

        if self.use_numbers.get():
            pool += string.digits
            forced.append(random.choice(string.digits))

        if self.use_symbols.get():
            pool += string.punctuation
            forced.append(random.choice(string.punctuation))

        if not pool:
            return

        remainder = [random.choice(pool) for _ in range(length - len(forced))]
        password = forced + remainder
        random.shuffle(password)
        result = "".join(password)

        # Write to output field
        self.pw_output.configure(state="normal")
        self.pw_output.delete(0, "end")
        self.pw_output.insert(0, result)
        self.pw_output.configure(state="readonly")

        # Show entropy of generated password
        entropy = calculate_entropy(result)
        label, color = get_strength_label(entropy)
        bits = round(entropy, 1)
        self.entropy_label.configure(
            text=f"Strength: {label} ({bits} bits of entropy)",
            text_color=color
        )

    def _copy_to_clipboard(self):
        password = self.pw_output.get()
        if not password:
            return

        self.clipboard_clear()
        self.clipboard_append(password)

        self.copy_btn.configure(text="Copied!", fg_color="#006600")
        self.after(2000, lambda: self.copy_btn.configure(
            text="Copy to Clipboard",
            fg_color="#1F6AA5"
        ))
