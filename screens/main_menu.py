import customtkinter as ctk

class MainMenu(ctk.CTkFrame):
    def __init__(self, parent, controller):
            super().__init__(parent, fg_color="#142F9B")
            self.controller=controller

            self.grid_rowconfigure(0, weight=1)
            self.grid_rowconfigure(6, weight=1)

            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(2, weight=1)

            ctk.CTkLabel(
                  self,
                  text="What would you like to do?",
                  font=("Helvetica", 50, "bold"),
            ).grid(row=1, column=1, pady=(0,10))

            ctk.CTkLabel(
                  self,
                  text="Choose an option",
                  font=("Helvetica", 25, "bold"),
                ).grid(row=2, column=1, pady=(0, 12))
            
            browse_vault_btn = ctk.CTkButton(
                  self,
                  text="Browse Vault",
                  width=400, height=60,
                  font=("Helvetica", 20, "bold"),
                  command=lambda: controller.show_screen("VaultScreen")
            )
            browse_vault_btn.grid(row=3, column=1, pady=(0, 12))

            gen_pw_btn = ctk.CTkButton(
                  self,
                  text="Generate Password",
                  width=400, height=60,
                  font=("Helvetica", 20, "bold"),
                  command=lambda: controller.show_screen("PWGenerator")
            )
            gen_pw_btn.grid(row=4, column=1, pady=(0, 12))

            settings_btn = ctk.CTkButton(
                  self,
                  text="Settings",
                  width=400, height=60,
                  font=("Helvetica", 20, "bold"),
                  command=lambda: controller.show_screen("SettingsScreen")
            )
            settings_btn.grid(row=5, column=1, pady=(0, 12))

            ctk.CTkButton(
                  self,
                  text="Log Out",
                  width=400, height=60,
                  font=("Helvetica", 20, "bold"),
                  fg_color="transparent",
                  border_width=1,
                  command=lambda: controller.logout()
            ).grid(row=6, column=1, pady=(0, 12))
            