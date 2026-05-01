import customtkinter as ctk
from database.db import change_master_password, derive_vault_key
from utils import calculate_entropy, get_strength_label, validate_password

class SettingsScreen(ctk.CTkFrame):
    def __init__(self, parent, controller):
            super().__init__(parent, fg_color="#003FAA")
            self.controller=controller

            self.grid_rowconfigure(0, weight=1)
            self.grid_rowconfigure(20, weight=1)
            self.grid_columnconfigure(0, weight=1)
            self.grid_columnconfigure(1, weight=0)
            self.grid_columnconfigure(2, weight=1)

            ctk.CTkLabel(
                  self,
                  text="Settings",
                  font=("Helvetica", 60, "bold"),
            ).grid(row=1, column=1, pady=(0, 30))

            ctk.CTkLabel(
                  self,
                  text="Auto-Lock Timeout",
                  font=("Helvetica", 24, "bold"),
                  anchor="w",
                  width=600
            ).grid(row=2, column=1, sticky="w", pady=(0, 6))

            ctk.CTkLabel(
                  self,
                  text="Automatically lock the vault after a period of inactivity.",
                  font=("Helvetica", 15),
                  text_color="gray",
                  anchor="w",
                  width=600
            ).grid(row=3, column=1, sticky="w", pady=(0, 12))

            timeout_frame = ctk.CTkFrame(self, fg_color="transparent")
            timeout_frame.grid(row=4, column=1, sticky="w", pady=(0, 8))

            timeout_options = [
                  ("5 Minutes", 5),
                  ("10 Minutes", 10),
                  ("15 Minutes", 15),
                  ("30 Minutes", 30),
                  ("Never", None)
            ]

            self.timeout_buttons = {}
            for label, minutes in timeout_options:
                  btn = ctk.CTkButton(
                        timeout_frame,
                        text=label,
                        width=110, height=38,
                        font=("Helvetica", 14),
                        fg_color="transparent",
                        border_width=1,
                        command=lambda m=minutes, l=label: self._set_timeout(m, l)
                  )
                  btn.pack(side="left", padx=(0, 8))
                  self.timeout_buttons[label] = btn
            
            self.timeout_status = ctk.CTkLabel(
                  self,
                  text="Current timeout: 5 Minutes",
                  font=("Helvetica", 14),
                  text_color="gray",
                  anchor="w",
                  width=600
            )
            self.timeout_status.grid(row=5, column=1, sticky="w", pady=(0, 30))

            self._highlight_timeout_btn("5 Minutes")

            ctk.CTkFrame(
                  self,
                  height=2, width=600,
                  fg_color="#FFFFFF"
            ).grid(row=6, column=1, sticky="ew", pady=(0, 30))

            ctk.CTkLabel(
                  self,
                  text="Change Master Password",
                  font=("Helvetica", 24, "bold"),
                  anchor="w",
                  width=600
            ).grid(row=7, column=1, sticky="w", pady=(0, 16))

            ctk.CTkLabel(
                  self,
                  text="Current Password",
                  font=("Helvetica", 16),
                  anchor="w",
                  width=600
            ).grid(row=8, column=1, sticky="w", pady=(0, 6))

            self.current_pw_entry = ctk.CTkEntry(
                  self,
                  width=600, height=50,
                  placeholder_text="Enter your current master password",
                  font=("Helvetica", 15),
                  show="*"
            )
            self.current_pw_entry.grid(row=9, column=1, pady=(0, 16))

            ctk.CTkLabel(
                  self,
                  text="New Password",
                  font=("Helvetica", 16),
                  anchor="w",
                  width=600
            ).grid(row=10, column=1, sticky="w", pady=(0, 4))

            self.new_pw_entry = ctk.CTkEntry(
                  self,
                  width=600, height=50,
                  placeholder_text="Enter your new master password",
                  font=("Helvetica", 15),
                  show="*"
            )
            self.new_pw_entry.grid(row=11, column=1, pady=(0, 6))

            self.strength_label = ctk.CTkLabel(
                  self,
                  text="",
                  font=("Helvetica", 14),
                  anchor="w",
                  width=600
            )
            self.strength_label.grid(row=12, column=1, sticky="w", pady=(0, 12))

            ctk.CTkLabel(
                  self,
                  text="Confirm New Password",
                  font=("Helvetica", 16),
                  anchor="w",
                  width=600
            ).grid(row=13, column=1, sticky="w", pady=(0, 4))

            self.confirm_pw_entry = ctk.CTkEntry(
                  self,
                  width=600, height=50,
                  placeholder_text="Re-enter your new master password",
                  font=("Helvetica", 15),
                  show="*"
            )
            self.confirm_pw_entry.grid(row=14, column=1, pady=(0, 12))

            self.pw_feedback_label = ctk.CTkLabel(
                  self,
                  text="",
                  font=("Helvetica", 14),
                  anchor="w",
                  width=600,
                  wraplength=600
            )
            self.pw_feedback_label.grid(row=15, column=1, sticky="w", pady=(0, 12))

            ctk.CTkButton(
                  self,
                  text="Change Password",
                  width=600, height=50,
                  font=("Helvetica", 16, "bold"),
                  command=self._change_password
            ).grid(row=16, column=1, pady=(0, 16))

            ctk.CTkButton(
            self,
            text="← Main Menu",
            width=160, height=40,
            font=("Helvetica", 14),
            fg_color="transparent",
            border_width=1,
            command=lambda: self.controller.show_screen("MainMenu")
            ).place(x=20, rely=1.0, y=-20, anchor="sw")

            self.new_pw_entry.bind("<KeyRelease>", self._update_strength)

    # Update the auto-lock timeout on App and highlight chosen button.
    def _set_timeout(self, minutes, label):
        self.controller.set_lock_timeout(minutes)
        self._highlight_timeout_btn(label)
        display = f"{minutes} minutes" if minutes is not None else "Never"
        self.timeout_status.configure(text=f"Current timeout: {display}")

    # Fill the selected button and reset all others to transparent.
    # Makes the row of buttons behave like a radio button group.
    def _highlight_timeout_btn(self, selected_label):
        for label, btn in self.timeout_buttons.items():
            if label == selected_label:
                btn.configure(fg_color="#1F6AA5", border_width=0)
            else:
                btn.configure(fg_color="transparent", border_width=1)

    # Update strength label as the user types a new password.
    def _update_strength(self, event=None):
        password = self.new_pw_entry.get()

        if not password:
            self.strength_label.configure(text="")
            return

        entropy = calculate_entropy(password)
        label, color = get_strength_label(entropy)
        bits = round(entropy, 1)

        self.strength_label.configure(
            text=f"Strength: {label} ({bits} bits of entropy)",
            text_color=color
        )

    def _change_password(self):
        current = self.current_pw_entry.get()
        new_pw = self.new_pw_entry.get()
        confirm = self.confirm_pw_entry.get()

        if not current or not new_pw or not confirm:
            self.pw_feedback_label.configure(
                text="All fields are required.",
                text_color="#FF8800"
            )
            return

        errors = validate_password(new_pw)
        if errors:
            self.pw_feedback_label.configure(
                text="New password must contain:\n• " + "\n• ".join(errors),
                text_color="#FF8800"
            )
            return

        if new_pw != confirm:
            self.pw_feedback_label.configure(
                text="New passwords do not match",
                text_color="#FF8800"
            )
            return

        result = change_master_password(
            self.controller.current_user,
            current,
            new_pw,
            self.controller.vault_conn
        )

        if not result["success"]:
            self.pw_feedback_label.configure(
                text=result["error"],
                text_color="#FF8800"
            )
            return

        # Update the live session key, vault remains usable immediately
        self.controller.encryption_key = derive_vault_key(
            new_pw,
            result["new_enc_key_salt"]
        )

        self.current_pw_entry.delete(0, "end")
        self.new_pw_entry.delete(0, "end")
        self.confirm_pw_entry.delete(0, "end")
        self.strength_label.configure(text="")

        self.pw_feedback_label.configure(
            text="Master password changed successfully!",
            text_color="#04FF00"
        )