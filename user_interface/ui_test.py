import customtkinter

# def button_callback():
#     print("Button pressed!")
# # Defining what the button press action does, 
# # which in this case prints "Button pressed!" to the console

# app = customtkinter.CTk()
# # Creating an instance of the CTk class, which is the main application window for our custom tkinter app
# app.title("my app")
# # Setting the title of the application window to "my app"
# app.geometry("400x150")
# # Setting the size of the application window to 400 pixels in width and 150 pixels in height
# app.grid_columnconfigure((0,1), weight=1)
# app.grid_rowconfigure(0, weight=1)

# mybutton = customtkinter.CTkButton(app, text="my button", command=button_callback)
# # Creating a button widget using the CTkButton class.
# # The button is a child of the main application window (app), 
# # has the text "my button", and is linked to the button_callback function 
# # that will be called when the button is pressed.
# mybutton.grid(row=0, column=0, padx=20, pady=20, sticky="ew", columnspan=2)
# # Placing the button within the window's grid
# # and designating its position and properties.
# # The "sticky" parameter makes the button expand horizontally to fill 
# # the available space in its grid cell.

# # Note that the sticky parameter is set to "ew", which means "east-west",
# # not "ew" like gross.

# checkbox_1 = customtkinter.CTkCheckBox(app, text="checkbox 1")
# checkbox_1.grid(row=1, column=0, padx=20, pady=(0, 20), sticky="w")
# checkbox_2 = customtkinter.CTkCheckBox(app, text="checkbox 2")
# checkbox_2.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="w")
# # Pady is set to (0, 20) to add padding only below the checkboxes, not above.

# app.mainloop()

# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("my app")
#         self.geometry("400x150")
#         self.grid_columnconfigure(0, weight=1)
#         self.grid_rowconfigure(0, weight=1)

#         self.checkbox_frame = customtkinter.CTkFrame(self)
#         self.checkbox_frame.grid(row=0, padx=10, pady=(10, 0), sticky="nsw")

#         self.checkbox_1 = customtkinter.CTkCheckBox(self.checkbox_frame, text="checkbox 1")
#         self.checkbox_1.grid(row=0, column =0, padx=10, pady=(10, 0), sticky="w")

#         self.checkbox_2 = customtkinter.CTkCheckBox(self.checkbox_frame, text="checkbox 2")
#         self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

#         self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
#         self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

#     def button_callback(self):
#         print("Button pressed!")

# app = App()
# app.mainloop()

#########################################################

# class MyCheckboxFrame(customtkinter.CTkFrame):
#     def __init__(self, master, title, values):
#         super().__init__(master)
#         self.grid_columnconfigure(0, weight=1)
#         self.values = values
#         self.title = title
#         self.checkboxes = []

#         self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
#         self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

#         for i, value in enumerate(self.values):
#             checkbox = customtkinter.CTkCheckBox(self, text=value)
#             checkbox.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
#             self.checkboxes.append(checkbox)


        # self.checkbox_1 = customtkinter.CTkCheckBox(self, text="checkbox 1")
        # self.checkbox_1.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")

        # self.checkbox_2 = customtkinter.CTkCheckBox(self, text="checkbox 2")
        # self.checkbox_2.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")

        # self.checkbox_3 = customtkinter.CTkCheckBox(self, text="checkbox 3")
        # self.checkbox_3.grid(row=2, column=0, padx=10, pady=(10, 0), sticky="w")
    
    # def get(self):
    #     checked_checkboxes = []
    #     if self.checkbox_1.get() == 1:
    #         checked_checkboxes.append(self.checkbox_1.cget("text"))
    #     if self.checkbox_2.get() == 1:
    #         checked_checkboxes.append(self.checkbox_2.cget("text"))
    #     if self.checkbox_3.get() == 1:
    #         checked_checkboxes.append(self.checkbox_3.cget("text"))
    #     return checked_checkboxes

    # def get(self):
    #     checked_checkboxes = []
    #     for checkbox in self.checkboxes:
    #         if checkbox.get() == 1:
    #             checked_checkboxes.append(checkbox.cget("text"))
    #     return checked_checkboxes

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("my app")
        self.geometry("400x220")
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
        self.scrollable_checkbox_frame = MyScrollableCheckboxFrame(self, title="Values", values=values)
        self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

        # self.checkbox_frame_1 = MyCheckboxFrame(self, "Values", values=["value 1", "value 2", "value 3"])
        # self.checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew")

        # self.checkbox_frame_2 = MyCheckboxFrame(self, "Options", values=["option 1", "option 2", "option 3"])
        # self.checkbox_frame_2.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")

        # self.radiobutton_frame = MyRadioButtonFrame(self, "Options", values=["option 1", "option 2"])
        # self.radiobutton_frame.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")

        self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
        self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        

    def button_callback(self):
        print("checkbox_frame_1:", self.checkbox_frame_1.get())
        print("radiobutton_frame:", self.radiobutton_frame.get())

class MyScrollableCheckboxFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, title, values):
        super().__init__(master, label_text=title)
        self.grid_columnconfigure(0, weight=1)
        self.values = values
        self.checkboxes = []

        for i, value in enumerate(self.values):
            checkbox = customtkinter.CTkCheckBox(self, text=value)
            checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
            self.checkboxes.append(checkbox)

    def get(self):
        checked_checkboxes = []
        for checkbox in self.checkboxes:
            if checkbox.get() == 1:
                checked_checkboxes.append(checkbox.cget("text"))
        return checked_checkboxes

class MyRadioButtonFrame(customtkinter.CTkFrame):
    def __init__(self, master, title, values):
        super().__init__(master)
        self.grid_columnconfigure(0, weight=1)
        self.title = title
        self.values = values
        self.radiobuttons = []
        self.variable = customtkinter.StringVar(value="")

        self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
        self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

        for i, value in enumerate(self.values):
            radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
            radiobutton.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
            self.radiobuttons.append(radiobutton)

    def get(self):
        return self.variable.get()
    
    def set(self, value):
        self.variable.set(value)



app = App()
app.mainloop()

#######################################################