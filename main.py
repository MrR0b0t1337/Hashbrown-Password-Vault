import customtkinter as ctk
# from screens import main_menu
from screens import login_screen
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
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)
        self.attributes("-fullscreen", True)
        #The above code creates the app window, sets it to fullscreen.
        #But maybe I don't need to do this if the firs thing I want the user
        #to see is the login screen? I suppose it could be a little screen with
        #an "Enter" button or something?

        # self.navigation = NavigationFrame(self, controller=self)
        # self.navigation.place(relx=0, rely=0, relwidth=1, relheight=0.125)
        # self.navigation._corner_radius=0
        #Commented out because I'm thinking that there's no real
        #reason for a navigation bar here, as the user will have to see the login
        #screen before they reach the main menu. There is nowhere for the user to
        #navigate TO before they log in.

        self.navigation1 = NavigationFrame(self, controller=self)
        self.navigation1.grid(row=0, column=0, sticky="s", ipadx=1920, ipady=350)
        # self.navigation2 = NavigationFrame(self, controller=self)
        # self.navigation2.grid(row=1, column=0, sticky="nesw")
        # self.navigation3 = NavigationFrame(self, controller=self)
        # self.navigation3.grid(row=2, column=0, sticky="nesw")



class NavigationFrame(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.configure(fg_color="#3851A4")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

if __name__ == "__main__":
    app = App()
    app.mainloop()


# TODO: Figure out how to implement different fonts, ideally on a project-wide level
# TODO: Figure out how to implement graphics/gradients, ideally on a project-wide level