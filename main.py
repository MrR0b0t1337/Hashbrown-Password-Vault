import customtkinter as ctk
from screens.main_menu import MainMenu
from screens.login_screen import LoginScreen
from screens.pw_generator import PWGenerator
from screens.vault_screen import VaultScreen
from screens.settings_screen import SettingsScreen
from screens.create_account_screen import CreateAccountScreen
from database.db import init_users_db

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        init_users_db()

        self.title("Hashbrown Password Vault")
        # screen_width = self.winfo_screenwidth()
        # screen_height = self.winfo_screenheight()   
        # self.geometry(f"{screen_width}x{screen_height}+0+0")
        # self.attributes("-fullscreen", True)
        self.geometry("960x540")

        self.current_user = None
        self.vault_conn = None
        self.encryption_key = None
        

        container = ctk.CTkFrame(self, fg_color="transparent")
        container.pack(fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.screens = {}
        for ScreenClass in (LoginScreen, CreateAccountScreen, MainMenu, PWGenerator, VaultScreen, SettingsScreen):
            screen = ScreenClass(parent=container, controller=self)
            self.screens[ScreenClass.__name__] = screen
            screen.grid(row=0, column=0, sticky="nsew")


        self.show_screen("LoginScreen")
        self.update_idletasks()
        self.protocol("WM_DELETE_WINDOW", self._on_closing)
        
    def show_screen(self, name: str):
        self.screens[name].tkraise()

    def logout(self):
        if self.vault_conn:
            self.vault_conn.close()
        
        self.current_user = None
        self.vault_conn = None
        self.encryption_key = None

        self.show_screen("LoginScreen")

    def _on_closing(self):
        if self.vault_conn:
            self.vault_conn.close()
        self.destroy()
        
if __name__ == "__main__":
    app = App()
    try:
        app.mainloop()
    except KeyboardInterrupt:
        app.destroy()

# TODO: Figure out how to implement graphics/gradients, ideally on a project-wide level
