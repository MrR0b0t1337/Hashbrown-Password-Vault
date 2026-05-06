import customtkinter as ctk
from database.db import create_user
from utils import calculate_entropy, get_strength_label, validate_password

class CreateAccountScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#142F9B")
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(10, weight=1)

        ctk.CTkLabel(
            self,
            text="Create Account",
            font=("Helvetica", 80, "bold"),
        ).grid(row=0, column=1, pady=(0, 40))

        #Username
        ctk.CTkLabel(
            self,
            text="Username",
            font=("Helvetica", 26),
            width=560,
            anchor="w"
        ).grid(row=1, column=1, pady=(0, 6))

        self.username_entry = ctk.CTkEntry(
            self,
            width=560, height=70,
            placeholder_text="Choose a username",
            font=("Helvetica", 22)
        )
        self.username_entry.grid(row=2, column=1, pady=(0, 24))

        #Master Password
        ctk.CTkLabel(
            self,
            text="Master Password",
            font=("Helvetica", 26),
            width=560,
            anchor="w"
        ).grid(row=3, column=1, pady=(0, 6))

        pw_row = ctk.CTkFrame(self, fg_color="transparent")
        pw_row.grid(row=4, column=1, pady=(0, 6))

        self.password_entry = ctk.CTkEntry(
            pw_row,
            width=480, height=70,
            placeholder_text="Enter your desired master password",
            font=("Helvetica", 22),
            show="*"
        )
        self.password_entry.grid(row=0, column=0)

        self.pw_show_btn = ctk.CTkButton(
            pw_row,
            text="Show",
            width=80, height=70,
            font=("Helvetica", 16),
            fg_color="transparent",
            border_width=1,
            command=lambda: self._toggle_entry(self.password_entry, self.pw_show_btn)
        )
        self.pw_show_btn.grid(row=0, column=1, padx=(8, 0))

        self.strength_label = ctk.CTkLabel(
            self,
            text="",
            font=("Helvetica", 18),
            width=560,
            anchor="w"
        )
        self.strength_label.grid(row=5, column=1, pady=(0, 16))

        ctk.CTkLabel(
            self, text="Confirm Master Password",
            font=("Helvetica", 26),
            width=560,
            anchor="w"
        ).grid(row=6, column=1, pady=(0, 6))

        confirm_row = ctk.CTkFrame(self, fg_color="transparent")
        confirm_row.grid(row=7, column=1, pady=(0, 24))

        self.confirm_entry = ctk.CTkEntry(
            confirm_row,
            width=480, height=70,
            placeholder_text="Re-enter your master password",
            font=("Helvetica", 22),
            show="*"
        )
        self.confirm_entry.grid(row=0, column=0)

        self.confirm_show_btn = ctk.CTkButton(
            confirm_row,
            text="Show",
            width=80, height=70,
            font=("Helvetica", 16),
            fg_color="transparent",
            border_width=1,
            command=lambda: self._toggle_entry(self.confirm_entry, self.confirm_show_btn)
        )
        self.confirm_show_btn.grid(row=0, column=1, padx=(8, 0))

        self.error_label = ctk.CTkLabel(
            self,
            text="",
            text_color="#FF8800",
            font=("Helvetica", 20),
            width=560,
            wraplength=560,
            justify="left"
        )
        self.error_label.grid(row=8, column=1, pady=(0, 16))

        ctk.CTkButton(
            self,
            text="Create Account",
            width=560, height=60,
            font=("Helvetica", 20, "bold"),
            command=self._submit,
        ).grid(row=9, column=1, pady=(0, 16))

        ctk.CTkButton(
            self,
            text="<- Back to Login Screen",
            width=560, height=50,
            font=("Helvetica", 18),
            fg_color="transparent",
            border_width=1,
            command=lambda: controller.show_screen("LoginScreen")
            ).grid(row=10, column=1)
        
        self.password_entry.bind("<KeyRelease>", self._update_strength)


    def _toggle_entry(self, entry, btn):
        if entry.cget("show") == "*":
            entry.configure(show="")
            btn.configure(text="Hide")
        else:
            entry.configure(show="*")
            btn.configure(text="Show")

    def _update_strength(self, event=None):
        password=self.password_entry.get()

        if not password:
            self.strength_label.configure(text="", text_color="white")
            return
        
        entropy = calculate_entropy(password)
        label, color = get_strength_label(entropy)
        bits = round(entropy, 1)

        self.strength_label.configure(
            text=f"Strength: {label} ({bits} bits of entropy)",
            text_color=color
        )

    def _submit(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm = self.confirm_entry.get()

        if not username or not password or not confirm:
            self.error_label.configure(text="All fields are required.")
            return
        if len(username) < 3:
            self.error_label.configure(text="Username must be at least 3 characters in length")
            return
        
        errors = validate_password(password)
        if errors:
            self.error_label.configure(
                text="Password must contain:\n• " + "\n• ".join(errors)
            )
            return
        
        if password != confirm:
            self.error_label.configure(text="Passwords do not match.")
            return
        
        result = create_user(username, password)

        if not result["success"]:
            self.error_label.configure(text=result["error"])
            return
        
        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        self.confirm_entry.delete(0, "end")
        self.strength_label.configure(text="")
        self.error_label.configure(text="")

        self.controller.show_screen("LoginScreen")