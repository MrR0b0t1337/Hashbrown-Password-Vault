import customtkinter as ctk

class pw_generator_screen(ctk.CTkFrame):
    def __init__(self, parent, controller):
            super().__init__(parent, fg_color="#000000")
            self.controller=controller

            self.grid_rowconfigure(0, weight=1)
            self.grid_rowconfigure(5, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(5, weight=1)

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