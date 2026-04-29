import customtkinter as ctk

class SettingsScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
            super().__init__(parent, fg_color="#003FAA")
            self.controller=controller

            self.grid_rowconfigure(0, weight=1)
            self.grid_rowconfigure(5, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(5, weight=1)

            ctk.CTkLabel(
                  self,
                  text="Settings",
                  font=("Helvetica", 50, "bold"),
            ).grid(row=1, column=1, pady=(0, 5))

            ctk.CTkLabel(
                  self,
                  text="Change settings (i.e. time until timeout, change master password,etc.s)",
                  font=("Helvetica", 20),
                  text_color="gray"
            ).grid(row=2, column=1, pady=(0,20))

            ctk.CTkButton(
            self,
            text="← Main Menu",
            width=160, height=40,
            font=("Helvetica", 14),
            fg_color="transparent",
            border_width=1,
            command=lambda: self.controller.show_screen("MainMenu")
            ).place(x=20, rely=1.0, y=-20, anchor="sw")