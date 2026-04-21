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

        #Here is where I instantiate all screens at once and "stack" them
        #in the same frame. None of these screens are made yet, though.
        # self.screens = {}
        # for ScreenClass in (LoginScreen, MainMenu, VaultScreen, PasswordGeneratorScreen, SettingsScreen):
        #     screen = ScreenClass(parent=container, controller=self)
        #     self.screens[ScreenClass.__name__] = screen
        #     screen.grid(row=0, column=0, sticky="nsew")

        

        

        




if __name__ == "__main__":
    app = App()
    app.mainloop()

# TODO: Figure out how to implement graphics/gradients, ideally on a project-wide level
# TODO: Figure out how to force the login screen to be the first screent he user sees
