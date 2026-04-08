# import tkinter as tk

# # border_effects = {
# #     "flat": tk.FLAT,
# #     "sunken": tk.SUNKEN,
# #     "raised": tk.RAISED,
# #     "groove": tk.GROOVE,
# #     "ridge": tk.RIDGE
# # }

# # for relief_name, relief in border_effects.items():
# #     frame = tk.Frame(master=window, relief=relief, borderwidth=5)
# #     frame.pack(side=tk.LEFT)
# #     label = tk.Label(master=frame, text=relief_name)
# #     label.pack()

# window = tk.Tk()

# frame_a = tk.Frame()
# frame_b = tk.Frame()




# # greeting = tk.Label(text="Hello, TKinter")
# # #tk.Label(text="Hello, TKinter") is a widget that we have assigned to the variable 'greeting'
# # #So far, we have only created the widget. We have NOT added it to the window yet.
# # greeting.pack()
# # #The .pack() method adds the label widget to the window

# # label_a = tk.Label(master=frame_a, text="I'm inside of Frame A")
# # label_a.pack()

# # label_b = tk.Label(master=frame_b, text="I'm inside of Frame B")
# # label_b.pack()

# # frame_b.pack()
# # frame_a.pack()
# #These .pack() methods are order-sensitive, meaning that the order
# #in which they are interpreted will determine the order in which they are displayed


# # button = tk.Button(
# #     text="Click me!",
# #     width=25,
# #     height=5,
# #     bg="blue",
# #     fg="yellow",
# # )









# window.mainloop()
####################################
# import customtkinter as ctk

# class App(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.title("Frame Switching App")
#         self.geometry("400x300")

#         # 1. Create a container frame to hold all screens
#         self.container = ctk.CTkFrame(self)
#         self.container.pack(side="top", fill="both", expand=True)
#         self.container.grid_rowconfigure(0, weight=1)
#         self.container.grid_columnconfigure(0, weight=1)

#         self.frames = {}

#         # 2. Initialize and stack each page
#         for F in (StartPage, PageOne):
#             page_name = F.__name__
#             frame = F(parent=self.container, controller=self)
#             self.frames[page_name] = frame
#             # All frames go in the same grid cell (stacking)
#             frame.grid(row=0, column=0, sticky="nsew")

#         self.show_frame("StartPage")

#     def show_frame(self, page_name):
#         """Bring the specified frame to the top layer"""
#         frame = self.frames[page_name]
#         frame.tkraise()

# class StartPage(ctk.CTkFrame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         label = ctk.CTkLabel(self, text="Start Page", font=("Arial", 24))
#         label.pack(pady=40)

#         # Button to switch to PageOne
#         button = ctk.CTkButton(self, text="Go to Page One",
#                                command=lambda: controller.show_frame("PageOne"))
#         button.pack()

# class PageOne(ctk.CTkFrame):
#     def __init__(self, parent, controller):
#         super().__init__(parent)
#         label = ctk.CTkLabel(self, text="Page One", font=("Arial", 24))
#         label.pack(pady=40)

#         # Button to return to StartPage
#         button = ctk.CTkButton(self, text="Back to Home",
#                                command=lambda: controller.show_frame("StartPage"))
#         button.pack()

# if __name__ == "__main__":
#     app = App()
#     app.mainloop()
######################################################################
# Source - https://stackoverflow.com/a/74844868
# Posted by BUILDERCOIN
# Retrieved 2026-04-08, License - CC BY-SA 4.0

# import tkinter
# import customtkinter

# DARK_MODE = "dark"
# customtkinter.set_appearance_mode(DARK_MODE)
# customtkinter.set_default_color_theme("dark-blue")


# class App(customtkinter.CTk):

#     def __init__(self):
#         super().__init__()
        
#         self.title("Change Frames")
#         # remove title bar , page reducer and closing page !!!most have a quit button with app.destroy!!! (this app have a quit button so don't worry about that)
#         self.overrideredirect(True)
#         # make the app as big as the screen (no mater wich screen you use) 
#         self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        

#         # root!
#         self.main_container = customtkinter.CTkFrame(self, corner_radius=10)
#         self.main_container.pack(fill=tkinter.BOTH, expand=True, padx=10, pady=10)

#         # left side panel -> for frame selection
#         self.left_side_panel = customtkinter.CTkFrame(self.main_container, width=150, corner_radius=10)
#         self.left_side_panel.pack(side=tkinter.LEFT, fill=tkinter.Y, expand=False, padx=5, pady=5)
        
#         self.left_side_panel.grid_columnconfigure(0, weight=1)
#         self.left_side_panel.grid_rowconfigure((0, 1, 2, 3), weight=0)
#         self.left_side_panel.grid_rowconfigure((4, 5), weight=1)
        
        
#         # self.left_side_panel WIDGET
#         self.logo_label = customtkinter.CTkLabel(self.left_side_panel, text="Welcome! \n", font=customtkinter.CTkFont(size=20, weight="bold"))
#         self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        
#         self.scaling_label = customtkinter.CTkLabel(self.left_side_panel, text="UI Scaling:", anchor="w")
#         self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        
#         self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.left_side_panel, values=["80%", "90%", "100%", "110%", "120%"],
#                                                             command=self.change_scaling_event)
#         self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20), sticky = "s")
        
#         self.bt_Quit = customtkinter.CTkButton(self.left_side_panel, text="Quit", fg_color= '#EA0000', hover_color = '#B20000', command= self.close_window)
#         self.bt_Quit.grid(row=9, column=0, padx=20, pady=10)
        
#         # button to select correct frame IN self.left_side_panel WIDGET
#         self.bt_dashboard = customtkinter.CTkButton(self.left_side_panel, text="Dashboard", command=self.dash)
#         self.bt_dashboard.grid(row=1, column=0, padx=20, pady=10)

#         self.bt_statement = customtkinter.CTkButton(self.left_side_panel, text="Statement", command=self.statement)
#         self.bt_statement.grid(row=2, column=0, padx=20, pady=10)
        
#         self.bt_categories = customtkinter.CTkButton(self.left_side_panel, text="Manage Categories", command=self.categories)
#         self.bt_categories.grid(row=3, column=0, padx=20, pady=10)
        

#         # right side panel -> have self.right_dashboard inside it
#         self.right_side_panel = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
#         self.right_side_panel.pack(side=tkinter.LEFT, fill=tkinter.BOTH, expand=True, padx=5, pady=5)
        
        
#         self.right_dashboard = customtkinter.CTkFrame(self.main_container, corner_radius=10, fg_color="#000811")
#         self.right_dashboard.pack(in_=self.right_side_panel, side=tkinter.TOP, fill=tkinter.BOTH, expand=True, padx=0, pady=0)
    

#     #  self.right_dashboard   ----> dashboard widget  
#     def dash(self):
        
#         self.clear_frame()
#         self.bt_from_frame1 = customtkinter.CTkButton(self.right_dashboard, text="dash", command=lambda:print("test dash") )
#         self.bt_from_frame1.grid(row=0, column=0, padx=20, pady=(10, 0))
#         self.bt_from_frame2 = customtkinter.CTkButton(self.right_dashboard, text="dash 1", command=lambda:print("test dash 1" ) )
#         self.bt_from_frame2.grid(row=1, column=0, padx=20, pady=(10, 0))

#     #  self.right_dashboard   ----> statement widget
#     def statement(self):
#         self.clear_frame()
#         self.bt_from_frame3 = customtkinter.CTkButton(self.right_dashboard, text="statement", command=lambda:print("test statement") )
#         self.bt_from_frame3.grid(row=0, column=0, padx=20, pady=(10, 0))
        
#     #  self.right_dashboard   ----> categories widget
#     def categories(self):
#         self.clear_frame()
#         self.bt_from_frame4 = customtkinter.CTkButton(self.right_dashboard, text="categories", command=lambda:print("test cats") )
#         self.bt_from_frame4.grid(row=0, column=0, padx=20, pady=(10, 0))


#     # Change scaling of all widget 80% to 120%
#     def change_scaling_event(self, new_scaling: str):
#         new_scaling_float = int(new_scaling.replace("%", "")) / 100
#         customtkinter.set_widget_scaling(new_scaling_float)
        
        
#     # close the entire window    
#     def close_window(self): 
#             App.destroy(self)
            
            
#     # CLEAR ALL THE WIDGET FROM self.right_dashboard(frame) BEFORE loading the widget of the concerned page       
#     def clear_frame(self):
#         for widget in self.right_dashboard.winfo_children():
#             widget.destroy()


# a = App()
# a.mainloop()
###########################################################################
# import customtkinter as ctk

# class SettingsWindow(ctk.CTkToplevel):
#     def __init__(self, parent):
#         super().__init__(parent)
        
#         # Configure window
#         self.title("Settings")
#         self.geometry("500x400")
#         self.minsize(400, 300)
#         self.resizable(True, True)
        
#         # Set custom colors
#         self.configure(fg_color=("#f0f0f0", "#2b2b2b"))
        
#         # Make window modal
#         self.grab_set()
#         self.attributes("-topmost", True)
        
#         # Configure grid
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(1, weight=1)
        
#         # Title label
#         title = ctk.CTkLabel(
#             self,
#             text="Application Settings",
#             font=ctk.CTkFont(size=20, weight="bold")
#         )
#         title.grid(row=0, column=0, pady=20, padx=20, sticky="w")
        
#         # Settings frame
#         settings_frame = ctk.CTkFrame(self)
#         settings_frame.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))
        
#         # Add settings widgets here
#         appearance_label = ctk.CTkLabel(settings_frame, text="Appearance Mode:")
#         appearance_label.pack(pady=10, padx=20, anchor="w")
        
#         appearance_menu = ctk.CTkOptionMenu(
#             settings_frame,
#             values=["Light", "Dark", "System"],
#             command=self.change_appearance
#         )
#         appearance_menu.pack(pady=5, padx=20, anchor="w")
        
#         # Close button
#         close_button = ctk.CTkButton(
#             self,
#             text="Close",
#             command=self.destroy
#         )
#         close_button.grid(row=2, column=0, pady=(0, 20))
    
#     def change_appearance(self, mode):
#         ctk.set_appearance_mode(mode.lower())

# class MainApp(ctk.CTk):
#     def __init__(self):
#         super().__init__()
#         self.title("Main Application")
#         self.geometry("700x500")
        
#         button = ctk.CTkButton(
#             self,
#             text="Open Settings",
#             command=self.open_settings
#         )
#         button.pack(pady=20)
    
#     def open_settings(self):
#         settings = SettingsWindow(self)
#         settings.focus()

# if __name__ == "__main__":
#     app = MainApp()
#     app.mainloop()
    ##########################################################################
import tkinter


root = tkinter.Tk()
root.geometry("1920x1080")
root.title("main")

l = tkinter.Label(root, text = "This is root window")

top = tkinter.Toplevel()
top.geometry("1920x1080")
top.title("toplevel")
l2 = tkinter.Label(top, text = "This is toplevel window")

l.pack()
l2.pack()

top.mainloop()

#In theory, this should work for what I need. I would just need to make some sort of navigation system and
#maybe invoke the destroy() method or whatver so I don't have all these windows open simultaneously?

#It seems that instantiating Tk (root = tkinter.Tk()) not only creates the main or "master" window of the application,
#but also initializes the entire TKinter framework and starts up the Tcl intepreter under the hood.