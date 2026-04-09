import customtkinter as ctk

ctk.set_appearance_mode("dark")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hashbrown Password Vault")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)
        #self.attributes("-fullscreen", True)
        #First need to create a way to exit the app.

        label = ctk.CTkLabel(self, text="Welcome to Hashbrown Password Vault!", font=ctk.CTkFont(size=24, weight="bold"))
        label.grid(row=0, column=0, columnspan=2, pady=20)  

class Frame(ctk.CTkFrame):
    def __init__(self, parent, title):
        super().__init__(parent)


if __name__ == "__main__":
    app = App()
    app.mainloop()
#Good operating practice when it comes to Python; ensures that the code is 
#only executed when the script is run directly, and not when it is imported as a module in another script.

# TODO: Figure out how to implement different fonts, ideally on a project-wide level
# TODO: Figure out how to implement graphics/gradients, ideally on a project-wide level