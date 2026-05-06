import customtkinter as ctk
from database.db import authenticate_user, open_vault, derive_vault_key

class LoginScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#142F9B")
        self.controller = controller

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=0)
        self.grid_columnconfigure(2, weight=1)

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(8, weight=1)

        #Title Button
        ctk.CTkLabel(
            self,
            text="Hashbrown\n Password Vault",
            font=("Helvetica", 100, "bold"),
            bg_color="transparent", fg_color="#142F9B",
            corner_radius=0
        ).grid(row=0, column=1, pady=(0, 60))
        
        #Username Label
        ctk.CTkLabel(self,
                     text="Username",
                     font=("Helvetica", 26),
                     bg_color="transparent", fg_color="#142F9B",
                     corner_radius=0,
                     width=560,
                     anchor="w"
        ).grid(row=1, column=1, pady=(0, 6))

        #Username Entry Box
        self.username_entry = ctk.CTkEntry(
            self,
            width=560, height=70,
            placeholder_text="Enter your username",
            font=("Helvetica", 22)
        )
        self.username_entry.grid(row=2, column=1, pady=(0, 30))

        #Master Password Label
        ctk.CTkLabel(self,
                     text="Master Password",
                     font=("Helvetica", 26),
                     width=560,
                     anchor="w",
                     fg_color="transparent", bg_color="#142F9B",
                     corner_radius=0
        ).grid(row=3, column=1, pady=(0, 6))

        pw_row = ctk.CTkFrame(self, fg_color="transparent", bg_color="transparent")
        pw_row.grid(row=4, column=1, pady=(0, 30))
        pw_row.grid_columnconfigure(0, weight=1)

        #Master Password Entry Box
        self.password_entry = ctk.CTkEntry(
            pw_row,
            width=480, height=70,
            placeholder_text="Enter your master password",
            font=("Helvetica", 22),
            show="*"
        )
        self.password_entry.grid(row=0, column=0)

        self.show_pw_btn = ctk.CTkButton(
            pw_row,
            text="Show",
            width=80, height=70,
            font=("Helvetica", 16),
            border_width=1,
            command=self._toggle_password
        )
        self.show_pw_btn.grid(row=0, column=1, padx=(8, 0))

        #Unlock Vault Button
        ctk.CTkButton(
            self,
            text="Unlock Vault",
            width=560, height=60,
            font=("Helvetica", 20, "bold"),
            command=self.attempt_login
        ).grid(row=5, column=1, pady=(0, 16))

        ctk.CTkButton(
            self,
            text="New user? Create an account.",
            width=560, height=40,
            font=("Helvetica", 18),
            fg_color="transparent",
            bg_color="transparent",
            hover_color="#004FCC",
            text_color="#AACCFF",
            command=lambda: controller.show_screen("CreateAccountScreen"),
        ).grid(row=6, column=1, pady=(0, 8))

        #Error Label, blank by default
        self.error_label = ctk.CTkLabel(
            self,
            text="",
            text_color="#FF8800",
            font=("Helvetica", 30),
            bg_color="transparent", fg_color="transparent"
        )
        self.error_label.grid(row=7, column=1)

        self.password_entry.bind("<Return>", lambda _: self.attempt_login())
        self.username_entry.bind("<Return>", lambda _: self.attempt_login())
        
    def attempt_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            self.error_label.configure(text="Please enter your username and password")
            return
        
        result = authenticate_user(username, password)

        if not result["success"]:
            self.error_label.configure(text=result["error"])
            return
        
        hex_key = result["enc_key_salt"]
        encryption_key = derive_vault_key(password, hex_key)
        vault_conn = open_vault(username, password, hex_key)

        self.controller.current_user = username
        self.controller.vault_conn = vault_conn
        self.controller.encryption_key = encryption_key

        self.username_entry.delete(0, "end")
        self.password_entry.delete(0, "end")
        self.error_label.configure(text="")

        self.controller.start_lock_timer()

        self.controller.show_screen("MainMenu")
    
    def _toggle_password(self):
        if self.password_entry.cget("show") == "*":
            self.password_entry.configure(show="")
            self.show_pw_btn.configure(text="Hide")
        else:
            self.password_entry.configure(show="*")
            self.show_pw_btn.configure(text="Show")

