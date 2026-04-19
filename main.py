import customtkinter as ctk
# from screens import main_menu
# from screens import login_screen
# from screens import pw_generator

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Hashbrown Password Vault")
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()   
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        self.attributes("-fullscreen", True)

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.columnconfigure(0, weight=1)
        #Container to hold each frame and swap them out when necessary
        #Ditching the navigation frame. Makes more sense just to
        #have a 'back' button that sends the user back to the
        #main menu.


if __name__ == "__main__":
    app = App()
    app.mainloop()

# TODO: Figure out how to implement graphics/gradients, ideally on a project-wide level