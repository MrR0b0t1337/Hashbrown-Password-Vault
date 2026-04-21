import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class LoginScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#000000")
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)

        ctk.CTkLabel(
            self,
            text="Hashbrown Password Vault",
            font=("Helvetica", 50, "bold")
        ).grid(row=1, column=1, pady=(0, 40))

        ctk.CTkLabel(self,
                     text="Username",
                     font=("Helvetica", 20)).grid(
                         row=2, column=1, sticky="w", padx=4
                     )
        
        self.username_entry = ctk.CTkEntry(
            self,
            width=350, height=50,
            desc_text="Enter your username",
            font=("Helvetica", 14)
        ).grid(row=5, column=1, pady=(0, 8))

        self.password_entry = ctk.CTkEntry(
            self,
            width=350, height=50,
            desc_text="Enter your master password",
            font=("Helvetica", 14)
        ).grid(row=5, column=1, pady=(0, 8))

        ctk.CTkButton(
            self,
            text="Unlock Vault",
            width=350, height=50,
            font=("Helvetica", 20, "bold"),
        )
        
    # def attempt_login(self):
    #     username = self.username_entry.get()
    #     password = self.password_entry.get()

