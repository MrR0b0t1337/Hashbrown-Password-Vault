import customtkinter as ctk

class LoginScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#003FAA")
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(7, weight=1)
        
        ctk.CTkLabel(
            self,
            text="Hashbrown\n Password Vault",
            font=("Helvetica", 100, "bold")
        ).grid(row=0, column=1, pady=(0, 60))

        ctk.CTkLabel(self,
                     text="Username",
                     font=("Helvetica", 26),
                     width=560,
                     anchor="w"
        ).grid(row=1, column=1, pady=(0, 6))

        self.username_entry = ctk.CTkEntry(
            self,
            width=560, height=70,
            placeholder_text="Enter your username",
            font=("Helvetica", 22)
        )
        self.username_entry.grid(row=2, column=1, pady=(0, 30))

        ctk.CTkLabel(self,
                     text="Master Password",
                     font=("Helvetica", 26),
                     width=560,
                     anchor="w"
        ).grid(row=3, column=1, pady=(0, 6))

        self.password_entry = ctk.CTkEntry(
            self,
            width=560, height=70,
            placeholder_text="Enter your master password",
            font=("Helvetica", 22),
            show="*"
        )
        self.password_entry.grid(row=4, column=1, pady=(0, 30))

        unlock_vault_btn = ctk.CTkButton(
            self,
            text="Unlock Vault",
            width=400, height=60,
            font=("Helvetica", 20, "bold"),
            command=self.attempt_login
        )
        unlock_vault_btn.grid(row=6, column=1)

        self.error_label = ctk.CTkLabel(
            self,
            text="",
            text_color="#FF8800",
            font=("Helvetica", 30)
        )
        self.error_label.grid(row=7, column=1, pady=(0, 12))

        self.password_entry.bind("<Return>", lambda _: self.attempt_login())
        self.username_entry.bind("<Return>", lambda _: self.attempt_login())
        
    def attempt_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "brady" and password == "password":
            self.error_label.configure(text="")
            self.controller.show_screen("MainMenu")
        else:
            self.error_label.configure(text="Invalid username or password. Please try again!")


    

