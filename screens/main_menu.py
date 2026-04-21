import customtkinter as ctk

class main_menu(ctk.CTkFrame):
    def __init__(self, parent, controller):
            super().__init__(parent, fg_color="#000000")
            self.controller=controller

            self.grid_rowconfigure(0, weight=1)
            self.grid_rowconfigure(3, weight=1)
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
                ).grid(row=1, colum=1, pady=(0, 12))
            
            