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
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()   
        self.geometry(f"{screen_width}x{screen_height}+0+0")
        self.attributes("-fullscreen", True)
        
        self.current_user = None
        self.vault_conn = None
        self.encryption_key = None

        #Default timeout (in milliseconds), equivalent to 5 minutes.
        #Set to 'None' to disable auto-lock entirely.
        self.lock_after_ms = 5 * 60 * 1000

        #Holds the pending after() call ID so we can
        #cancel and restart it on every activity event.
        self._lock_timer_id = None

        self.bind_all("<Motion>", self._reset_lock_timer)
        self.bind_all("<KeyPress>", self._reset_lock_timer)
        
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

    #Clear session, stop lock timer, return to Login Screen
    def logout(self):
        self._stop_lock_timer()

        if self.vault_conn:
            self.vault_conn.close()
        
        self.current_user = None
        self.vault_conn = None
        self.encryption_key = None

        self.show_screen("LoginScreen")

    #Cleanly stop timer, close vault, destroy window
    def _on_closing(self):
        self._stop_lock_timer()

        if self.vault_conn:
            self.vault_conn.close()
        self.destroy()
    
    #Called by LoginScreen after a successful login.
    #Kicks off the inactivity countdown for the first time.
    def start_lock_timer(self):
        self._reset_lock_timer()

    #Cancel the existing timer and start a fresh one.
    #Fires automatically on every mouse movement or key press
    #via bind_all() above. Does nothing if no user is logged in,
    #so the timer never runs on the login or create account screens.
    def _reset_lock_timer(self, event=None):
        if not self.current_user:
            return
        if self._lock_timer_id:
            self.after_cancel(self._lock_timer_id)
        if self.lock_after_ms is not None:
            self._lock_timer_id = self.after(
                self.lock_after_ms,
                self._auto_lock
            )

    #Cancel any pending lock timer
    def _stop_lock_timer(self):
        if self._lock_timer_id:
            self.after_cancel(self._lock_timer_id)
            self._lock_timer_id = None

    #Called when the inactivity timer fires. Logs the user out.
    def _auto_lock(self):
        if self.current_user:
            self.logout()

    #Called by SettingsScreen when the user picks a new timeout.
    #'None' to disable auto-lock entirely.
    def set_lock_timeout(self, minutes):
        if minutes is None:
            self.lock_after_ms = None
            self._stop_lock_timer()
        else:
            self.lock_after_ms = minutes * 60 * 1000
            self._reset_lock_timer()

        
if __name__ == "__main__":
    app = App()
    try:
        app.mainloop()
    except KeyboardInterrupt:
        app.destroy()

# TODO: Figure out how to implement graphics/gradients, ideally on a project-wide level
