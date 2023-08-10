import tkinter as tk
from tkinter import ttk

class ComplexInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Complex Tkinter Interface")
        
        # Top Frame
        top_frame = tk.Frame(root)
        top_frame.pack(fill="both", expand=True)
        
        # Left Side
        left_frame = tk.Frame(top_frame)
        left_frame.pack(side="left", padx=10, pady=10, fill="y")
        
        tk.Label(left_frame, text="Program Settings", font=("Helvetica", 16, "bold")).pack(anchor="w")
        
        self.disable_wifi_var = tk.BooleanVar()
        self.change_name_var = tk.BooleanVar()
        self.new_name_var = tk.StringVar()
        self.write_settings_var = tk.BooleanVar()
        
        tk.Checkbutton(left_frame, text="Disable/Enable WiFi", variable=self.disable_wifi_var).pack(anchor="w")
        tk.Checkbutton(left_frame, text="Change Player Name", variable=self.change_name_var).pack(anchor="w")
        tk.Entry(left_frame, textvariable=self.new_name_var).pack(fill="x", pady=5)
        tk.Checkbutton(left_frame, text="Write New Settings", variable=self.write_settings_var).pack(anchor="w")
        
        profiles = ["Profile 1", "Profile 2", "Profile 3"]
        self.profile_var = tk.StringVar()
        self.profile_var.set(profiles[0])
        tk.Label(left_frame, text="Profile").pack(anchor="w", pady=5)
        ttk.Combobox(left_frame, textvariable=self.profile_var, values=profiles).pack(fill="x")
        
        # Right Side
        right_frame = tk.Frame(top_frame)
        right_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)
        
        tk.Label(right_frame, text="Minecraft Settings", font=("Helvetica", 16, "bold")).pack(anchor="w")
        
        self.group_boxes = []  # (key box, value box)
        self.input_frame = tk.Frame(right_frame)  # frame to hold all groups
        self.add_group()

        plus_button = tk.Button(right_frame, text="+", command=self.add_group)
        minus_button = tk.Button(right_frame, text="-", command=self.remove_group)
        
        plus_button.pack(side="left")
        minus_button.pack(side="right")
        
        # Bottom Frame
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(fill="x", pady=20)
        
        tk.Button(bottom_frame, text="Load Profile").pack(side="left", padx=10)
        tk.Button(bottom_frame, text="WRITE!", command=self.write_settings).pack(side="right", padx=10)

    def add_group(self):
        group_frame = tk.Frame(self.groups_frame)  # add frame inside bigger frame
        
        key_entry = tk.Entry(group_frame)
        value_entry = tk.Entry(group_frame)
        
        group_frame.pack(padx=10, pady=5, fill="x")
        key_entry.pack(side="left", padx=5)
        value_entry.pack(side="right", padx=5)
        
        self.group_boxes.append((key_entry, value_entry))

    def remove_group(self):
        # removes last group from list
        if len(self.groups) > 0:
            key_entry, value_entry = self.groups[-1]
            key_entry.pack_forget()
            value_entry.pack_forget()

    def write_settings(self):
        # Here you can implement the functionality to write the settings based on user input.
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ComplexInterface(root)
    root.mainloop()