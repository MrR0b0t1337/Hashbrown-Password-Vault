import customtkinter as ctk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

class LoginScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#003FAA")
        self.controller = controller

        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(5, weight=1)
        self.grid_rowconfigure(7, weight=1)
        
        ctk.CTkLabel(
            self,
            text="Hashbrown Password Vault",
            font=("Helvetica", 60, "bold")
        ).grid(row=1, column=0, columnspan=2)

        ctk.CTkLabel(self,
                     text="Username:",
                     font=("Helvetica", 20)
                     ).grid(row=3, column=0, sticky="e")
        
        self.username_entry = ctk.CTkEntry(
            self,
            height=50,
            placeholder_text="Enter your username",
            font=("Helvetica", 14)
        )
        
        self.username_entry.grid(row=3, column=1, sticky="ew")

        ctk.CTkLabel(self,
                     text="Master Password:",
                     font=("Helvetica", 20)).grid(row=4, column=0, sticky="e")

        self.password_entry = ctk.CTkEntry(
            self,
            height=50,
            placeholder_text="Enter your master password",
            font=("Helvetica", 14)
        )
        
        self.password_entry.grid(row=4, column=1, sticky="ew")

        unlock_vault_btn = ctk.CTkButton(
            self,
            text="Unlock Vault",
            height=50,
            font=("Helvetica", 20, "bold"),
        )
        
        unlock_vault_btn.grid(row=6, column=0, columnspan=2)
        
    # def attempt_login(self):
    #     username = self.username_entry.get()
    #     password = self.password_entry.get()

