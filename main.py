import customtkinter as ctk
from screens.main_menu import MainMenu
from screens.login_screen import LoginScreen
from screens.pw_generator import PWGenerator
from screens.vault_screen import VaultScreen
from screens.settings_screen import SettingsScreen

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
        # self.geometry("1920x750")
        

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.screens = {}
        for ScreenClass in (LoginScreen, MainMenu, PWGenerator, VaultScreen, SettingsScreen):
            screen = ScreenClass(parent=container, controller=self)
            self.screens[ScreenClass.__name__] = screen
            screen.grid(row=0, column=0, sticky="nsew")


        self.show_screen("LoginScreen")
        
    def show_screen(self, name: str):
        self.screens[name].tkraise()

        
if __name__ == "__main__":
    app = App()
    app.mainloop()

# TODO: Figure out how to implement graphics/gradients, ideally on a project-wide level
