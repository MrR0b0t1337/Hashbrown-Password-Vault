# import customtkinter

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

# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()

#         self.title("my app")
#         screen_width = self.winfo_screenwidth()
#         screen_height = self.winfo_screenheight()
#         self.geometry(f"{screen_width}x{screen_height}+0+0")
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure((0, 1), weight=1)

#         values = ["value 1", "value 2", "value 3", "value 4", "value 5", "value 6"]
#         self.scrollable_checkbox_frame = MyScrollableCheckboxFrame(self, title="Values", values=values)
#         self.scrollable_checkbox_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nsew")

#         # self.checkbox_frame_1 = MyCheckboxFrame(self, "Values", values=["value 1", "value 2", "value 3"])
#         # self.checkbox_frame_1.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nsew")

#         # self.checkbox_frame_2 = MyCheckboxFrame(self, "Options", values=["option 1", "option 2", "option 3"])
#         # self.checkbox_frame_2.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")

#         # self.radiobutton_frame = MyRadioButtonFrame(self, "Options", values=["option 1", "option 2"])
#         # self.radiobutton_frame.grid(row=0, column=1, padx=(0, 10), pady=(10, 0), sticky="nsew")

#         self.button = customtkinter.CTkButton(self, text="my button", command=self.button_callback)
#         self.button.grid(row=3, column=0, padx=10, pady=10, sticky="ew", columnspan=2)

        

#     def button_callback(self):
#         print("checkbox_frame_1:", self.checkbox_frame_1.get())
#         print("radiobutton_frame:", self.radiobutton_frame.get())

# class MyScrollableCheckboxFrame(customtkinter.CTkScrollableFrame):
#     def __init__(self, master, title, values):
#         super().__init__(master, label_text=title)
#         self.grid_columnconfigure(0, weight=1)
#         self.values = values
#         self.checkboxes = []

#         for i, value in enumerate(self.values):
#             checkbox = customtkinter.CTkCheckBox(self, text=value)
#             checkbox.grid(row=i, column=0, padx=10, pady=(10, 0), sticky="w")
#             self.checkboxes.append(checkbox)

#     def get(self):
#         checked_checkboxes = []
#         for checkbox in self.checkboxes:
#             if checkbox.get() == 1:
#                 checked_checkboxes.append(checkbox.cget("text"))
#         return checked_checkboxes

# class MyRadioButtonFrame(customtkinter.CTkFrame):
#     def __init__(self, master, title, values):
#         super().__init__(master)
#         self.grid_columnconfigure(0, weight=1)
#         self.title = title
#         self.values = values
#         self.radiobuttons = []
#         self.variable = customtkinter.StringVar(value="")

#         self.title = customtkinter.CTkLabel(self, text=self.title, fg_color="gray30", corner_radius=6)
#         self.title.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="ew")

#         for i, value in enumerate(self.values):
#             radiobutton = customtkinter.CTkRadioButton(self, text=value, value=value, variable=self.variable)
#             radiobutton.grid(row=i+1, column=0, padx=10, pady=(10, 0), sticky="w")
#             self.radiobuttons.append(radiobutton)

#     def get(self):
#         return self.variable.get()
    
#     def set(self, value):
#         self.variable.set(value)



# app = App()
# app.mainloop()

#######################################################
# import customtkinter

# customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

# app = customtkinter.CTk()
# app.geometry("400x780")
# app.title("CustomTkinter simple_example.py")


# def button_callback():
#     print("Button click", combobox_1.get())


# def slider_callback(value):
#     progressbar_1.set(value)


# frame_1 = customtkinter.CTkFrame(master=app)
# frame_1.pack(pady=20, padx=60, fill="both", expand=True)

# label_1 = customtkinter.CTkLabel(master=frame_1, justify=customtkinter.LEFT)
# label_1.pack(pady=10, padx=10)

# progressbar_1 = customtkinter.CTkProgressBar(master=frame_1)
# progressbar_1.pack(pady=10, padx=10)

# button_1 = customtkinter.CTkButton(master=frame_1, command=button_callback)
# button_1.pack(pady=10, padx=10)

# slider_1 = customtkinter.CTkSlider(master=frame_1, command=slider_callback, from_=0, to=1)
# slider_1.pack(pady=10, padx=10)
# slider_1.set(0.5)

# entry_1 = customtkinter.CTkEntry(master=frame_1, placeholder_text="CTkEntry")
# entry_1.pack(pady=10, padx=10)

# optionmenu_1 = customtkinter.CTkOptionMenu(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
# optionmenu_1.pack(pady=10, padx=10)
# optionmenu_1.set("CTkOptionMenu")

# combobox_1 = customtkinter.CTkComboBox(frame_1, values=["Option 1", "Option 2", "Option 42 long long long..."])
# combobox_1.pack(pady=10, padx=10)
# combobox_1.set("CTkComboBox")

# checkbox_1 = customtkinter.CTkCheckBox(master=frame_1)
# checkbox_1.pack(pady=10, padx=10)

# radiobutton_var = customtkinter.IntVar(value=1)

# radiobutton_1 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=1)
# radiobutton_1.pack(pady=10, padx=10)

# radiobutton_2 = customtkinter.CTkRadioButton(master=frame_1, variable=radiobutton_var, value=2)
# radiobutton_2.pack(pady=10, padx=10)

# switch_1 = customtkinter.CTkSwitch(master=frame_1)
# # switch_1.pack(pady=10, padx=10)

# # text_1 = customtkinter.CTkTextbox(master=frame_1, width=200, height=70)
# # text_1.pack(pady=10, padx=10)
# # text_1.insert("0.0", "CTkTextbox\n\n\n\n")

# # segmented_button_1 = customtkinter.CTkSegmentedButton(master=frame_1, values=["CTkSegmentedButton", "Value 2"])
# # segmented_button_1.pack(pady=10, padx=10)

# # tabview_1 = customtkinter.CTkTabview(master=frame_1, width=300)
# # tabview_1.pack(pady=10, padx=10)
# # tabview_1.add("CTkTabview")
# # tabview_1.add("Tab 2")

# # app.mainloop()
# ##################################################################
# import tkinter
# import tkinter.messagebox
# import customtkinter

# customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
# customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


# class App(customtkinter.CTk):
#     def __init__(self):
#         super().__init__()

#         # configure window
#         self.title("CustomTkinter complex_example.py")
#         self.geometry(f"{1100}x{580}")

#         # configure grid layout (4x4)
#         self.grid_columnconfigure(1, weight=1)
#         self.grid_columnconfigure((2, 3), weight=0)
#         self.grid_rowconfigure((0, 1, 2), weight=1)

#         # create sidebar frame with widgets
#         self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
#         self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
#         self.sidebar_frame.grid_rowconfigure(4, weight=1)
#         self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="CustomTkinter", font=customtkinter.CTkFont(size=20, weight="bold"))
#         self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
#         self.sidebar_button_1 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
#         self.sidebar_button_1.grid(row=1, column=0, padx=20, pady=10)
#         self.sidebar_button_2 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
#         self.sidebar_button_2.grid(row=2, column=0, padx=20, pady=10)
#         self.sidebar_button_3 = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
#         self.sidebar_button_3.grid(row=3, column=0, padx=20, pady=10)
#         self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
#         self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
#         self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
#                                                                        command=self.change_appearance_mode_event)
#         self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))
#         self.scaling_label = customtkinter.CTkLabel(self.sidebar_frame, text="UI Scaling:", anchor="w")
#         self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
#         self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["80%", "90%", "100%", "110%", "120%"],
#                                                                command=self.change_scaling_event)
#         self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

#         # create main entry and button
#         self.entry = customtkinter.CTkEntry(self, placeholder_text="CTkEntry")
#         self.entry.grid(row=3, column=1, columnspan=2, padx=(20, 0), pady=(20, 20), sticky="nsew")

#         self.main_button_1 = customtkinter.CTkButton(master=self, fg_color="transparent", border_width=2, text_color=("gray10", "#DCE4EE"))
#         self.main_button_1.grid(row=3, column=3, padx=(20, 20), pady=(20, 20), sticky="nsew")

#         # create textbox
#         self.textbox = customtkinter.CTkTextbox(self, width=250)
#         self.textbox.grid(row=0, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")

#         # create tabview
#         self.tabview = customtkinter.CTkTabview(self, width=250)
#         self.tabview.grid(row=0, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
#         self.tabview.add("CTkTabview")
#         self.tabview.add("Tab 2")
#         self.tabview.add("Tab 3")
#         self.tabview.tab("CTkTabview").grid_columnconfigure(0, weight=1)  # configure grid of individual tabs
#         self.tabview.tab("Tab 2").grid_columnconfigure(0, weight=1)

#         self.optionmenu_1 = customtkinter.CTkOptionMenu(self.tabview.tab("CTkTabview"), dynamic_resizing=False,
#                                                         values=["Value 1", "Value 2", "Value Long Long Long"])
#         self.optionmenu_1.grid(row=0, column=0, padx=20, pady=(20, 10))
#         self.combobox_1 = customtkinter.CTkComboBox(self.tabview.tab("CTkTabview"),
#                                                     values=["Value 1", "Value 2", "Value Long....."])
#         self.combobox_1.grid(row=1, column=0, padx=20, pady=(10, 10))
#         self.string_input_button = customtkinter.CTkButton(self.tabview.tab("CTkTabview"), text="Open CTkInputDialog",
#                                                            command=self.open_input_dialog_event)
#         self.string_input_button.grid(row=2, column=0, padx=20, pady=(10, 10))
#         self.label_tab_2 = customtkinter.CTkLabel(self.tabview.tab("Tab 2"), text="CTkLabel on Tab 2")
#         self.label_tab_2.grid(row=0, column=0, padx=20, pady=20)

#         # create radiobutton frame
#         self.radiobutton_frame = customtkinter.CTkFrame(self)
#         self.radiobutton_frame.grid(row=0, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
#         self.radio_var = tkinter.IntVar(value=0)
#         self.label_radio_group = customtkinter.CTkLabel(master=self.radiobutton_frame, text="CTkRadioButton Group:")
#         self.label_radio_group.grid(row=0, column=2, columnspan=1, padx=10, pady=10, sticky="")
#         self.radio_button_1 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=0)
#         self.radio_button_1.grid(row=1, column=2, pady=10, padx=20, sticky="n")
#         self.radio_button_2 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=1)
#         self.radio_button_2.grid(row=2, column=2, pady=10, padx=20, sticky="n")
#         self.radio_button_3 = customtkinter.CTkRadioButton(master=self.radiobutton_frame, variable=self.radio_var, value=2)
#         self.radio_button_3.grid(row=3, column=2, pady=10, padx=20, sticky="n")

#         # create slider and progressbar frame
#         self.slider_progressbar_frame = customtkinter.CTkFrame(self, fg_color="transparent")
#         self.slider_progressbar_frame.grid(row=1, column=1, padx=(20, 0), pady=(20, 0), sticky="nsew")
#         self.slider_progressbar_frame.grid_columnconfigure(0, weight=1)
#         self.slider_progressbar_frame.grid_rowconfigure(4, weight=1)
#         self.seg_button_1 = customtkinter.CTkSegmentedButton(self.slider_progressbar_frame)
#         self.seg_button_1.grid(row=0, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
#         self.progressbar_1 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
#         self.progressbar_1.grid(row=1, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
#         self.progressbar_2 = customtkinter.CTkProgressBar(self.slider_progressbar_frame)
#         self.progressbar_2.grid(row=2, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
#         self.slider_1 = customtkinter.CTkSlider(self.slider_progressbar_frame, from_=0, to=1, number_of_steps=4)
#         self.slider_1.grid(row=3, column=0, padx=(20, 10), pady=(10, 10), sticky="ew")
#         self.slider_2 = customtkinter.CTkSlider(self.slider_progressbar_frame, orientation="vertical")
#         self.slider_2.grid(row=0, column=1, rowspan=5, padx=(10, 10), pady=(10, 10), sticky="ns")
#         self.progressbar_3 = customtkinter.CTkProgressBar(self.slider_progressbar_frame, orientation="vertical")
#         self.progressbar_3.grid(row=0, column=2, rowspan=5, padx=(10, 20), pady=(10, 10), sticky="ns")

#         # create scrollable frame
#         self.scrollable_frame = customtkinter.CTkScrollableFrame(self, label_text="CTkScrollableFrame")
#         self.scrollable_frame.grid(row=1, column=2, padx=(20, 0), pady=(20, 0), sticky="nsew")
#         self.scrollable_frame.grid_columnconfigure(0, weight=1)
#         self.scrollable_frame_switches = []
#         for i in range(100):
#             switch = customtkinter.CTkSwitch(master=self.scrollable_frame, text=f"CTkSwitch {i}")
#             switch.grid(row=i, column=0, padx=10, pady=(0, 20))
#             self.scrollable_frame_switches.append(switch)

#         # create checkbox and switch frame
#         self.checkbox_slider_frame = customtkinter.CTkFrame(self)
#         self.checkbox_slider_frame.grid(row=1, column=3, padx=(20, 20), pady=(20, 0), sticky="nsew")
#         self.checkbox_1 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
#         self.checkbox_1.grid(row=1, column=0, pady=(20, 0), padx=20, sticky="n")
#         self.checkbox_2 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
#         self.checkbox_2.grid(row=2, column=0, pady=(20, 0), padx=20, sticky="n")
#         self.checkbox_3 = customtkinter.CTkCheckBox(master=self.checkbox_slider_frame)
#         self.checkbox_3.grid(row=3, column=0, pady=20, padx=20, sticky="n")

#         # set default values
#         self.sidebar_button_3.configure(state="disabled", text="Disabled CTkButton")
#         self.checkbox_3.configure(state="disabled")
#         self.checkbox_1.select()
#         self.scrollable_frame_switches[0].select()
#         self.scrollable_frame_switches[4].select()
#         self.radio_button_3.configure(state="disabled")
#         self.appearance_mode_optionemenu.set("Dark")
#         self.scaling_optionemenu.set("100%")
#         self.optionmenu_1.set("CTkOptionmenu")
#         self.combobox_1.set("CTkComboBox")
#         self.slider_1.configure(command=self.progressbar_2.set)
#         self.slider_2.configure(command=self.progressbar_3.set)
#         self.progressbar_1.configure(mode="indeterminnate")
#         self.progressbar_1.start()
#         self.textbox.insert("0.0", "CTkTextbox\n\n" + "Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua.\n\n" * 20)
#         self.seg_button_1.configure(values=["CTkSegmentedButton", "Value 2", "Value 3"])
#         self.seg_button_1.set("Value 2")

#     def open_input_dialog_event(self):
#         dialog = customtkinter.CTkInputDialog(text="Type in a number:", title="CTkInputDialog")
#         print("CTkInputDialog:", dialog.get_input())

#     def change_appearance_mode_event(self, new_appearance_mode: str):
#         customtkinter.set_appearance_mode(new_appearance_mode)

#     def change_scaling_event(self, new_scaling: str):
#         new_scaling_float = int(new_scaling.replace("%", "")) / 100
#         customtkinter.set_widget_scaling(new_scaling_float)

#     def sidebar_button_event(self):
#         print("sidebar_button click")


# if __name__ == "__main__":
#     app = App()
#     app.mainloop()