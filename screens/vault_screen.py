import customtkinter as ctk
from database.db import(
    get_all_credentials,
    get_credential,
    add_credential,
    update_credential,
    delete_credential
)

class VaultScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent, fg_color="#003FAA")
        self.controller = controller
        self.selected_id = None

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)

########### Left Panel ##################
        left = ctk.CTkFrame(self, fg_color="#003FAA", width=600, corner_radius=0)
        left.grid(row=0, column=0, sticky="nesw")
        left.grid_propagate(False)
        left.grid_rowconfigure(2, weight=1)
        left.grid_columnconfigure(0, weight=1)

        ctk.CTkLabel(
            left,
            text="Logins",
            font=("Helvetica", 28, "bold"),
            anchor="w",
        ).grid(row=0, column=0, padx=20, pady=(20, 8), sticky="w")
        #Add button sits in the top-right corner of the left panel
        ctk.CTkButton(
            left,
            text="Add +",
            width=90, height=34,
            font=("Helvetica", 14, "bold"),
            command=self._show_form
        ).place(relx=1.0, x=-20, y=20, anchor="ne")

        #Search bar filters the list in real time as the user types
        self.search_var = ctk.StringVar()
        self.search_var.trace_add("write", self._refresh_list)
        
        ctk.CTkEntry(
            left,
            placeholder_text="Search logins...",
            width=460, height=44,
            textvariable=self.search_var
        ).grid(row=1, column=0, padx=20, pady=(0, 10))

        #Scrollable login list
        self.login_list = ctk.CTkScrollableFrame(left, fg_color="transparent")
        self.login_list.grid(row=2, column=0, sticky="nesw", padx=8)

        #Right Panel

        #This frame holds:
        #-self.detail_panel, which shows the credential details/placeholder
        #-self.form_panel, which shows the add/edit form
        #We swap between them using tkraise(), same pattern as rest of the screens

        self.right = ctk.CTkFrame(self, fg_color="#003FAA", corner_radius=0)
        self.right.grid(row=0, column=1, sticky="nesw")
        self.right.grid_rowconfigure(0, weight=1)
        self.right.grid_columnconfigure(0, weight=1)

        self.detail_panel = ctk.CTkFrame(self.right, fg_color="#003FAA")
        self.detail_panel.grid(row=0, column=0, sticky="nesw", padx=40, pady=40)
        self.detail_panel.grid_columnconfigure(0, weight=1)

        self.form_panel = ctk.CTkFrame(self.right, fg_color="#003FAA")
        self.form_panel.grid(row=0, column=0, sticky="nesw", padx=40, pady=40)
        self.form_panel.grid_columnconfigure(0, weight=1)

        #Start with the detail panel (placeholder) on top
        self._show_placeholder()
        self.detail_panel.tkraise()

        ctk.CTkButton(
            self,
            text="← Main Menu",
            width=160, height=40,
            font=("Helvetica", 14),
            fg_color="transparent",
            border_width=1,
            command=lambda: self.controller.show_screen("MainMenu")
        ).place(x=20, rely=1.0, y=-20, anchor="sw")

        #TkRaise Override

    def tkraise(self, *args, **kwargs):
        super().tkraise(*args, **kwargs)
        self.selected_id = None
        self._refresh_list()
        self._show_placeholder()
        self.detail_panel.tkraise()

    def _refresh_list(self, *args):
        for widget in self.login_list.winfo_children():
            widget.destroy()

        rows = get_all_credentials(self.controller.vault_conn)

        query = self.search_var.get().lower()
        
        if query:
            rows = [
                r for r in rows
                if query in r["service_name"].lower()
                or query in (r["login_username"] or "").lower()
            ]

        if not rows:
            ctk.CTkLabel(
                self.login_list,
                text="No entries found.",
                text_color="gray",
                font=("Helvetica", 13)
            ).pack(pady=20)
            return
        
        for row in rows:
            self._make_login_row(row)

    def _make_login_row(self, entry: dict):
        is_selected = self.selected_id == entry["credential_id"]
        bg_color = "#3a3a5e" if is_selected else "#2a2a3e"

        row = ctk.CTkFrame(self.login_list, fg_color=bg_color, corner_radius=10)
        row.pack(fill="x", padx=4, pady=4)

        name_lbl = ctk.CTkLabel(
            row,
            text=entry["service_name"],
            font=("Helvetica", 20, "bold"),
            anchor="w"
        )
        name_lbl.grid(row=0, column=0, padx=14, pady=(16, 0), sticky="w")

        user_lbl = ctk.CTkLabel(
            row,
            text=entry["login_username"] or "-",
            font=("Helvetica", 14),
            text_color="gray",
            anchor="w"

        )
        user_lbl.grid(row=1, column=0, padx=14, pady=(4, 16), sticky="w")

        #Bind click on every widget in the row.

        for widget in (row, name_lbl, user_lbl):
            widget.bind(
                "<Button-1>",
                lambda _, e=entry: self._on_row_click(e["credential_id"])
            )
            widget.configure(cursor="hand2")

    
    def _show_placeholder(self):
        for widget in self.detail_panel.winfo_children():
            widget.destroy()

        ctk.CTkLabel(
            self.detail_panel,
            text="Select a login to view details",
            font=("Helvetica", 18, "bold"),
            text_color="gray"
        ).place(relx=0.5, rely=0.5, anchor="center")

    def _on_row_click(self, credential_id: int):
        self.selected_id = credential_id
        self._refresh_list()

        entry = get_credential(
            self.controller.vault_conn,
            credential_id,
            self.controller.encryption_key
        )
        if entry:
            self._show_detail(entry)

    def _show_detail(self, entry: dict):
        for widget in self.detail_panel.winfo_children():
            widget.destroy()

        #Service name as title
        ctk.CTkLabel(
            self.detail_panel,
            text=entry["service_name"],
            font=("Helvetica", 34, "bold"),
            anchor="w"
        ).pack(anchor="w", pady=(0, 24))

        #Username/email field
        self._make_detail_field("Username/Email", entry["login_username"] or "-")

        #Password field (hidden by default with show/hide toggle)
        self._make_secret_field("Password", entry["password"])

        #Timestamps
        ctk.CTkLabel(
            self.detail_panel,
            text=f"Created:     {entry['created_at'][:19].replace('T', ' ')}",
            font=("Helvetica", 16),
            text_color="white",
            anchor="w"
        ).pack(anchor="w", pady=(16, 0))

        ctk.CTkLabel(
            self.detail_panel,
            text=f"Last modified:   {entry['updated_at'][:19].replace('T', ' ')}",
            font=("Helvetica", 16),
            text_color="white",
            anchor="w"
        ).pack(anchor="w", pady=(2, 16))

        #Edit/Delete buttons
        btn_row = ctk.CTkFrame(self.detail_panel, fg_color="transparent")
        btn_row.pack(anchor="w")

        ctk.CTkButton(
            btn_row,
            text="Edit",
            width=130, height=44,
            font=("Helvetica", 16, "bold"),
            command=lambda: self._show_form(entry)
        ).pack(side="left", padx=(0, 8))

        ctk.CTkButton(
            btn_row,
            text="Delete",
            width=130, height=44,
            font=("Helvetica", 16, "bold"),
            fg_color="#8B0000",
            hover_color="#660000",
            command=lambda: self._confirm_delete(entry)
        ).pack(side="left")

        self.detail_panel.tkraise()

    def _make_detail_field(self, label: str, value: str):
        frame = ctk.CTkFrame(self.detail_panel, fg_color="#002080", corner_radius=10)
        frame.pack(fill="x", pady=4)

        ctk.CTkLabel(
            frame,
            text=label,
            font=("Helvetica", 16),
            text_color="gray",
            anchor="w",
            width=140
        ).grid(row=0, column=0, padx=(16, 8), pady=12, sticky="w")

        ctk.CTkLabel(
            frame,
            text=value,
            font=("Helvetica", 18),
            anchor="w"
        ).grid(row=0, column=1, sticky="w")

    def _make_secret_field(self, label: str, value: str):
        frame = ctk.CTkFrame(self.detail_panel, fg_color="#002080", corner_radius=10)
        frame.pack(fill="x", pady=4)
        frame.grid_columnconfigure(1, weight=1)

        ctk.CTkLabel(
            frame,
            text=label,
            font=("Helvetica", 16),
            text_color="gray",
            anchor="w",
            width=140
        ).grid(row=0, column=0, padx=(16, 8), pady=12, sticky="w")

        value_lbl = ctk.CTkLabel(
            frame,
            text="*" * len(value),
            font=("Helvetica", 18),
            anchor="w"
        )
        value_lbl.grid(row=0, column=1, sticky="w")

        visible = ctk.BooleanVar(value=False)

        def toggle():
            if visible.get():
                value_lbl.configure(text="*" * len(value))
                visible.set(False)
                toggle_btn.configure(text="Show")
            else:
                value_lbl.configure(text=value)
                visible.set(True)
                toggle_btn.configure(text="Hide")

        toggle_btn = ctk.CTkButton(
            frame,
            text="Show",
            width=70, height=34,
            font=("Helvetica", 14),
            fg_color="transparent",
            border_width=1,
            command=toggle
        )
        toggle_btn.grid(row=0, column=2, padx=4)

        copy_btn = ctk.CTkButton(
            frame,
            text="Copy",
            width=70, height=34,
            font=("Helvetica", 14),
            command=lambda: self._copy_and_flash(value, copy_btn)
        )
        copy_btn.grid(row=0, column=3, padx=(0, 12))

    def _copy_and_flash(self, text: str, btn: ctk.CTkButton):
        self.clipboard_clear()
        self.clipboard_append(text)
        btn.configure(text="Copied!", fg_color="#006600")
        self.after(2000, lambda: btn.configure(text="Copy", fg_color="#1F6AA5"))

#### Right Panel Add/Edit Form ######### Need to change the looks a little

    def _show_form(self, entry: dict = None):
        for widget in self.form_panel.winfo_children():
            widget.destroy()

        is_edit = entry is not None
        title = "Edit Login" if is_edit else "Add Login"

        ctk.CTkLabel(
            self.form_panel,
            text=title,
            font=("Helvetica", 26, "bold"),
            anchor="w"
        ).pack(anchor="w", pady=(0, 20))

        #Service Name
        ctk.CTkLabel(
            self.form_panel,
            text="Service Name *",
            font=("Helvetica", 20),
            anchor="w"
        ).pack(anchor="w")

        name_entry = ctk.CTkEntry(self.form_panel, height=54, font=("Helvetica", 18))
        if is_edit:
            name_entry.insert(0, entry["service_name"])
        name_entry.pack(fill="x", pady=(4, 14))

        #Username/email
        ctk.CTkLabel(
            self.form_panel,
            text="Username/Email",
            font=("Helvetica", 20),
            anchor="w"
        ).pack(anchor="w")

        username_entry = ctk.CTkEntry(self.form_panel, height=54, font=("Helvetica", 18))
        if is_edit:
            username_entry.insert(0,entry["login_username"] or "")
        username_entry.pack(fill="x", pady=(4, 14))

        #Password with show/hide toggle
        ctk.CTkLabel(
            self.form_panel,
            text="Password",
            font=("Helvetica", 20),
            anchor="w"
        ).pack(anchor="w")

        pw_row = ctk.CTkFrame(self.form_panel, fg_color="transparent")
        pw_row.pack(fill="x", pady=(4, 14))
        pw_row.grid_columnconfigure(0, weight=1)

        pw_entry = ctk.CTkEntry(pw_row, height=54, font=("Helvetica", 18), show="*")
        if is_edit:
            pw_entry.insert(0, entry["password"])
        pw_entry.grid(row=0, column=0, sticky="ew")

        show_var = ctk.BooleanVar(value=False)

        def toggle_pw():
            if show_var.get():
                pw_entry.configure(show="*")
                show_var.set(False)
                pw_toggle.configure(text="Show")
            else:
                pw_entry.configure(show="")
                show_var.set(True)
                pw_toggle.configure(text="Hide")

        pw_toggle = ctk.CTkButton(
            pw_row,
            text="Show",
            width=64, height=42,
            font=("Helvetica", 13),
            fg_color="transparent",
            border_width=1,
            command=toggle_pw
        )
        pw_toggle.grid(row=0, column=1, padx=(8, 0))

        #Error Label
        error_label = ctk.CTkLabel(
            self.form_panel,
            text="",
            text_color="#FF5555",
            font=("Helvetica", 13)
        )
        error_label.pack(anchor="w", pady=(0, 8))

        #Save/Cancel Buttons
        def _save():
            service = name_entry.get().strip()
            username = username_entry.get().strip()
            password = pw_entry.get()

            if not service:
                error_label.configure(text="Service name is required.")
                return
            
            if is_edit:
                update_credential(
                    self.controller.vault_conn,
                    entry["credential_id"],
                    service,
                    username,
                    password,
                    self.controller.encryption_key
                )
                #Reload the updated entry and go back to detail view
                updated = get_credential(
                    self.controller.vault_conn,
                    entry["credential_id"],
                    self.controller.encryption_key
                )
                self.selected_id = entry["credential_id"]
                self._refresh_list()
                self._show_detail(updated)
            else:
                add_credential(
                    self.controller.vault_conn,
                    service,
                    username,
                    password,
                    self.controller.encryption_key
                )
                self._refresh_list()
                self._show_placeholder()
                self.detail_panel.tkraise()
    
        def _cancel():
            if is_edit:
                self._show_detail(entry)
            else:
                self._show_placeholder()
            self.detail_panel.tkraise()

        btn_row = ctk.CTkFrame(self.form_panel, fg_color="transparent")
        btn_row.pack(fill="x", pady=(4, 0))

        ctk.CTkButton(
            btn_row,
            text="Save",
            height=44,
            font=("Helvetica", 15, "bold"),
            command=_save
        ).pack(side="left", expand=True, fill="x", padx=(0, 6))

        ctk.CTkButton(
            btn_row,
            text="Cancel",
            height=44,
            font=("Helvetica", 15),
            fg_color="transparent",
            border_width=1,
            command=_cancel
        ).pack(side="left", expand=True, fill="x", padx=(0, 6))

        self.form_panel.tkraise()


### Delete Confirmation Popup Window ###

#Working now but I would like to make sure it pops up in the middle of the screen

    def _confirm_delete(self, entry: dict):

        popup = ctk.CTkToplevel(self)
        popup.title("Confirm Delete")
        popup.resizable(False, False)
        popup.update()

        popup_width = 400
        popup_height = 180
        screen_width = popup.winfo_screenmmwidth()
        screen_height = popup.winfo_screenheight()
        x = (screen_width // 2) - (popup_width // 2)
        y = (screen_height // 2) - (popup_height // 2)
        popup.geometry(f"{popup_width}x{popup_height}+{x}+{y}")

        popup.grab_set()
        popup.focus_force()

        ctk.CTkLabel(
            popup,
            text=f"Delete \"{entry['service_name']}\"?",
            font=("Helvetica", 18, "bold"),
            text_color="gray"
        ).pack(pady=(0, 20))

        btn_row = ctk.CTkFrame(popup, fg_color="transparent")
        btn_row.pack()

        def confirm():
            delete_credential(
                self.controller.vault_conn,
                entry["credential_id"],
                entry["service_name"]
            )
            self.selected_id = None
            self._refresh_list()
            self._show_placeholder()
            self.detail_panel.tkraise()
            popup.destroy()

        ctk.CTkButton(
            btn_row,
            text="Yes, delete.",
            width=130, height=38,
            font=("Helvetica", 13),
            fg_color="#8B0000",
            hover_color="#660000",
            command=confirm
        ).pack(side="left", padx=(0, 8))

        ctk.CTkButton(
            btn_row,
            text="Cancel",
            width=130, height=38,
            font=("Helvetica", 13),
            fg_color="transparent",
            border_width=1,
            command=popup.destroy
        ).pack(side="left")