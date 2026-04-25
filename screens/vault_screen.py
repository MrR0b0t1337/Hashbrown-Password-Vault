import customtkinter as ctk

class VaultScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#003FAA")
        self.controller = controller

        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(2, weight=1)


        ctk.CTkButton(
        self,
        text="Back to Main Menu",
        width=400, height=60,
        font=("Helvetica", 20, "bold"),
        command=lambda: self.controller.show_screen("MainMenu")
        ).grid(row=3, column=1, pady=(0, 12))