import tkinter as tk
from tkinter import ttk, messagebox
from ProfileJSONManager import ProfileManager, get_default_path_to_json

class ProfileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Profile Manager")

        self.main_menu_frame = tk.Frame(self.root, relief=tk.RAISED, borderwidth=2)
        self.main_menu_frame.pack(padx=20, pady=20)

        self.create_main_menu_buttons()

        self.current_frame = self.main_menu_frame  # Set main menu as current frame

    def create_main_menu_buttons(self):
        button_labels = [
            ("Choose default profile", self.show_choose_default_frame),
            ("Edit Profiles", self.show_edit_profiles_frame),
            ("Write profile", self.show_write_profile_frame),
            ("Run Minecraft", self.show_run_minecraft_frame),
            ("Manage Program Dependencies", self.show_manage_dependencies_frame),
            ("Exit Program", self.root.quit)  # Add exit button
        ]

        for label, command in button_labels:
            button = tk.Button(self.main_menu_frame, text=label, command=command)
            button.pack(fill=tk.X, padx=10, pady=5)

    def show_frame(self, frame_to_show):
        if hasattr(self, 'current_frame'):
            self.current_frame.pack_forget()

        self.current_frame = frame_to_show
        self.current_frame.pack(padx=20, pady=20)

    def create_basic_frame(self, title, return_to_menu_func):
        frame = tk.Frame(self.root, relief=tk.RAISED, borderwidth=2)

        label = tk.Label(frame, text=title)
        label.pack(side=tk.TOP)  # Pack label at the top of the frame

        exit_button = tk.Button(frame, text="Exit", command=return_to_menu_func)
        exit_button.pack(side=tk.BOTTOM)  # Pack exit button at the bottom of the frame

        return frame

    def show_choose_default_frame(self):
        choose_default_frame = self.create_basic_frame("Choose Default Profile", self.show_main_menu_frame)
        
        profiles = self.get_preset_profiles()  # Replace with your code to get preset profiles
        self.selected_profile = tk.StringVar(value=profiles[0] if profiles else "")

        profile_combobox = ttk.Combobox(choose_default_frame, textvariable=self.selected_profile, values=profiles)
        profile_combobox.pack()

        set_default_button = tk.Button(choose_default_frame, text="Set Default", command=lambda: self.set_default_profile(profile_combobox.get()))
        set_default_button.pack()

        self.show_frame(choose_default_frame)

    def show_edit_profiles_frame(self):
        edit_profiles_frame = self.create_basic_frame("Edit Profiles", self.show_main_menu_frame)
        
        profiles = self.get_preset_profiles()  # Replace with your code to get preset profiles
        self.selected_edit_profile = tk.StringVar(value=profiles[0] if profiles else "")

        profile_combobox = ttk.Combobox(edit_profiles_frame, textvariable=self.selected_edit_profile, values=profiles)
        profile_combobox.pack()

        load_profile_button = tk.Button(edit_profiles_frame, text="Load Profile", command=self.load_profile)
        load_profile_button.pack()

        new_profile_button = tk.Button(edit_profiles_frame, text="New Profile", command=self.new_profile)
        new_profile_button.pack()

        remove_profile_button = tk.Button(edit_profiles_frame, text="Remove Profile", command=self.remove_profile)
        remove_profile_button.pack()

        ttk.Separator(edit_profiles_frame, orient=tk.HORIZONTAL).pack(fill=tk.X, padx=10, pady=5)

        run_offline_checkbutton = tk.Checkbutton(edit_profiles_frame, text="Run Minecraft Offline?")
        run_offline_checkbutton.pack()

        change_player_name_checkbutton = tk.Checkbutton(edit_profiles_frame, text="Change Player Name?")
        change_player_name_checkbutton.pack()

        player_name_entry = tk.Entry(edit_profiles_frame)
        player_name_entry.pack()

        options_label = tk.Label(edit_profiles_frame, text="options.txt settings")
        options_label.pack()

        options_textbox = tk.Text(edit_profiles_frame, width=40, height=4)
        options_textbox.pack()

        options_shaders_label = tk.Label(edit_profiles_frame, text="optionsshaders.txt settings")
        options_shaders_label.pack()

        options_shaders_textbox = tk.Text(edit_profiles_frame, width=40, height=4)
        options_shaders_textbox.pack()

        self.show_frame(edit_profiles_frame)

    def show_write_profile_frame(self):
        write_profile_frame = self.create_basic_frame("Write Profile", self.show_main_menu_frame)
        self.show_frame(write_profile_frame)

    def show_run_minecraft_frame(self):
        run_minecraft_frame = self.create_basic_frame("Run Minecraft", self.show_main_menu_frame)
        self.show_frame(run_minecraft_frame)

    def show_manage_dependencies_frame(self):
        manage_dependencies_frame = self.create_basic_frame("Manage Program Dependencies", self.show_main_menu_frame)
        self.show_frame(manage_dependencies_frame)

    def show_main_menu_frame(self):
        self.show_frame(self.main_menu_frame)

    # ----- CHOOSE DEFAULT FRAME FUNCTIONS -----

    def get_preset_profiles(self):
        json_manager = ProfileManager(file_path=get_default_path_to_json())
        return json_manager.get_profile_names()
    
    def set_default_profile(self, profile_name):
        json_manager = ProfileManager(file_path=get_default_path_to_json())
        json_manager.set_default_profile(profile_name)
    
    # ----- EDIT PROFILES FRAME FUNCTIONS -----

    def load_profile(self):
        selected_profile = self.selected_edit_profile.get()
        if selected_profile:
            # Implement your functionality to load the selected profile
            print(f"Loading profile: {selected_profile}")
        else:
            messagebox.showwarning("Error", "Please select a profile to load.")

    def new_profile(self):
        # Implement your functionality to create a new profile
        print("Creating a new profile")

    def remove_profile(self):
        selected_profile = self.selected_edit_profile.get()
        if selected_profile:
            # Implement your functionality to remove the selected profile
            print(f"Removing profile: {selected_profile}")
        else:
            messagebox.showwarning("Error", "Please select a profile to remove.")

def main():
    root = tk.Tk()
    app = ProfileManagerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
