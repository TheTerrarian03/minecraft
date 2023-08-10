import tkinter as tk
from tkinter import ttk

class ComplexInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Complex Tkinter Interface")
        
        # Left Side
        left_frame = tk.Frame(root)
        left_frame.pack(side="left", padx=10, pady=10)
        
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
        right_frame = tk.Frame(root)
        right_frame.pack(side="right", padx=10, pady=10)
        
        self.groups = []
        self.add_group()
        
        tk.Button(right_frame, text="+", command=self.add_group).pack()
        tk.Button(right_frame, text="-", command=self.remove_group).pack()
        
        # Bottom
        bottom_frame = tk.Frame(root)
        bottom_frame.pack(fill="x", pady=20)
        
        tk.Button(bottom_frame, text="WRITE!", command=self.write_settings).pack()

    def add_group(self):
        group_frame = tk.Frame(self.root)
        group_frame.pack(side="top", padx=10, pady=5, fill="x")
        
        key_entry = tk.Entry(group_frame)
        value_entry = tk.Entry(group_frame)
        
        key_entry.pack(side="left", padx=5)
        value_entry.pack(side="right", padx=5)
        
        self.groups.append((key_entry, value_entry))
        
    def remove_group(self):
        if self.groups:
            group_frame = self.groups.pop()
            group_frame[0].destroy()
            group_frame[1].destroy()

    def write_settings(self):
        # Here you can implement the functionality to write the settings based on user input.
        pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ComplexInterface(root)
    root.mainloop()