### v1.0
### -Logan Meyers
### -06232023

### [*] scalable user input
### [*] update graph
### [*] handle errors
### [*] find best equation algorithmically
### [ ] add multiple example data sets
### [ ] improve input box handling:
###       remove current selected box if any else last one
### [ ] scale image label to window size
### [ ] add more graph customization by user
###       i.e. title, x label, y label

### weather website used:
### https://www.wunderground.com/

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import graphing, calculations
import os

# constants
GRAPH_NAME   = "data_graph.png"
MISSING_NAME = "Images/missing_garfe.png"
ERROR_NAME   = "Images/error_garfe.png"

# predefined data (collections)
EXAMPLE = {
  "Points": [1, 2, 1, 0, 1, 2],
  "Title": "Example data",
  "Short Title": "Example",
  "X Label": "X-value",
  "Y Label": "Y-value"
}
OREGON = {
  "Points": [64.36, 72.49, 73.72, 68.34, 59.8, 43.41, 38.92, 43.12, 41.08, 44.48, 51.05, 63.3],
  "Title":  "Avg Temps: Portland, Oregon (2022)",
  "Short Title": "Oregon",
  "X Label": "Month number",
  "Y Label": "Temp (ºF)"
}
GEORGIA = {
  "Points": [50.61, 56.79, 62.82, 67.57, 74.38, 80.69, 80.83, 79.81, 76.92, 65.42, 63.5, 53.43],
  "Title":  "Avg Temps: Statenville, Georgia (2022)",
  "Short Title": "Georgia",
  "X Label": "Month number",
  "Y Label": "Temp (ºF)"
}
UTAH = {
  "Points": [21.29, 26, 31.52, 40.9, 43.39, 52.8, 62.42, 59.9, 52.3, 35.6, 27.87, 25.74],
  "Title":  "Avg Low Temps: East Carbon, Utah (2019)",
  "Short Title": "Utah",
  "X Label": "Month number",
  "Y Label": "Temp (ºF)"
}
MISSISSIPPI = {
  "Points": [59.58, 58.14, 71.94, 75.1, 81.42, 87.63, 88.94, 90.61, 84.83, 79.55, 67.6, 70.74],
  "Title":  "Avg Max Temps: State Line Mississippi (2021)",
  "Short Title": "Mississippi",
  "X Label": "Month number",
  "Y Label": "Temp (ºF)"
}
NORTH_DAKOTA = {
  "Points": [27, 12, 33, 54, 57, 72, 75, 68, 67, 54, 33, 27],
  "Title":  "Max of Min Temps: Grand Forks, North Dakota (2005)",
  "Short Title": "North Dakota",
  "X Label": "Month number",
  "Y Label": "Temp (ºF)"
}

# function to close root window
close_window = lambda root: root.destroy()

# function to delete data graph image
def delete_image():
  try:
    os.remove(GRAPH_NAME)
  except FileNotFoundError:
    pass

# window class, makes input management easy
class Window:
  def __init__(self, title="TK Window"):
    # root Window
    self.root = tk.Tk()
    self.root.title(title)

    # defining frames
    self.left_frame = tk.Frame(self.root)
    self.input_frame = tk.Frame(self.left_frame)
    self.right_frame = tk.Frame(self.root)

    # defining buttons and boxes
    # customization
    self.customization_frame = tk.Frame(self.left_frame)

    self.cust_title_frame = tk.Frame(self.customization_frame)
    self.cust_title_label = tk.Label(self.cust_title_frame, text="Title:")
    self.cust_title_box = tk.Entry(self.cust_title_frame)

    self.cust_x_frame = tk.Frame(self.customization_frame)
    self.cust_x_label = tk.Label(self.cust_x_frame, text="X-Label:")
    self.cust_x_box = tk.Entry(self.cust_x_frame)

    self.cust_y_frame = tk.Frame(self.customization_frame)
    self.cust_y_label = tk.Label(self.cust_y_frame, text="Y-Label:")
    self.cust_y_box = tk.Entry(self.cust_y_frame)

    # data input
    self.data_input_frames = []  # [ ( number label, box ) , etc ]
    self.data_manage_frame = tk.Frame(self.left_frame)
    self.addButton = tk.Button(self.data_manage_frame, text="+", command=self.addTextBox)
    self.removeButton = tk.Button(self.data_manage_frame, text="-", command=self.removeTextBox)
    self.calcButton = tk.Button(self.data_manage_frame, text="Calculate!", command=self.calcGraph)

    # predefined loads
    self.predefined_buttons = []
    self.predefined_frame = tk.Frame(self.left_frame)

    # defining graph label
    self.graphLabel = tk.Label(self.right_frame)
    self.graph_est_eq_label = tk.Label(self.right_frame, text="Best Estimate Equation: (None)")

    # defining seperators
    self.left_right_seperator = ttk.Separator(self.root, orient="vertical")
    self.cust_data_seperator = ttk.Separator(self.left_frame, orient="horizontal")
    self.data_predef_seperator = ttk.Separator(self.left_frame, orient="horizontal")

    # placing (packing) items into their place
    # left side
    # customization
    self.cust_title_label.pack(side=tk.LEFT)
    self.cust_title_box.pack()
    self.cust_title_frame.pack()
    self.cust_x_label.pack(side=tk.LEFT)
    self.cust_x_box.pack()
    self.cust_x_frame.pack()
    self.cust_y_label.pack(side=tk.LEFT)
    self.cust_y_box.pack()
    self.cust_y_frame.pack()
    self.customization_frame.pack()
    self.cust_data_seperator.pack(fill="x")
    self.input_frame.pack()
    # data input
    self.addButton.pack(side="left")
    self.removeButton.pack(side="left")
    self.calcButton.pack(side="left")
    self.data_manage_frame.pack()
    # predefined button loads
    self.data_predef_seperator.pack(fill="x")
    self.predefined_frame.pack()

    # right side
    self.graphLabel.pack()
    self.graph_est_eq_label.pack()

    # overarching frames
    self.left_frame.pack(side=tk.LEFT)
    self.left_right_seperator.pack(side=tk.LEFT, fill="y")
    self.right_frame.pack(side=tk.RIGHT)

    # initial image load
    self.loadImage()

    # initial box value setup
    self.addTextBox()

    # binding customization boxes to: enter -> calculate
    self.cust_title_box.bind("<Return>", lambda event: self.calcGraph())  # bind enter to calculate
    self.cust_x_box.bind("<Return>", lambda event: self.calcGraph())  # bind enter to calculate
    self.cust_y_box.bind("<Return>", lambda event: self.calcGraph())  # bind enter to calculate

  def loadData(self, info_dict):
    # values
    # clear boxes
    while len(self.data_input_frames) > 0:
      self.removeTextBox()
    if len(info_dict["Points"]) == 0:
      self.addTextBox()
    else:
      self.initBoxesToValues(info_dict["Points"])
    
    # customization options
    self.setCustomizationOptions(info_dict["Title"], info_dict["X Label"], info_dict["Y Label"])

  # load data graph or missing graph image to label
  def loadImage(self):
    try:
      image = Image.open(GRAPH_NAME)
      photo = ImageTk.PhotoImage(image)
      
      self.graphLabel.configure(image=photo)
      self.graphLabel.image = photo
    except:
      image = Image.open(MISSING_NAME)
      photo = ImageTk.PhotoImage(image)

      self.graphLabel.configure(image=photo)
      self.graphLabel.image = photo
  
  # load error image to label
  def loadErrorImage(self):
      image = Image.open(ERROR_NAME)
      photo = ImageTk.PhotoImage(image)
      
      self.graphLabel.configure(image=photo)
      self.graphLabel.image = photo

  # add a text box at the end
  def addTextBox(self, value=None):
    # define new elements
    frame = tk.Frame(self.input_frame)
    text_box = tk.Entry(frame)
    text_box.bind("<Return>", lambda event: self.calcGraph())  # bind enter to calculate
    number_label = tk.Label(frame, text=str(len(self.data_input_frames)))

    # set value to box if given
    if value != None:
      text_box.insert(0, str(value))

    # place (pack) elements into place
    frame.pack()
    number_label.pack(side=tk.LEFT)
    text_box.pack(side=tk.RIGHT)
    
    # append items to self list to future reference
    self.data_input_frames.append((frame, number_label, text_box))

  # remove text box at end if there are more than 1 present
  def removeTextBox(self):
    if len(self.data_input_frames) > 0:
      text_box = self.data_input_frames.pop()[0]
      text_box.pack_forget()

  # add boxes for each value in the list of values given
  def initBoxesToValues(self, values):
    for value in values:
      self.addTextBox(value)

  # returns a list of the float versions of the content in each box, from top to bottom, 0-end
  def getInputValues(self):
    values = [float(tkWidgets[2].get()) for tkWidgets in self.data_input_frames]
    return values

  def getCustomizationOptions(self):
    return {"Title": self.cust_title_box.get(),
            "X-Label:": self.cust_x_box.get(),
            "Y-Label:": self.cust_y_box.get()}

  def setCustomizationOptions(self, title, x_label, y_label):
    setBox = lambda box, text: (box.delete(0, tk.END), box.insert(0, text))
    
    if title: setBox(self.cust_title_box, title)
    if x_label: setBox(self.cust_x_box, x_label)
    if y_label: setBox(self.cust_y_box, y_label)

  def setPredefinedLoadButtons(self, data_dictionaries):
    # clear self list of buttons
    for button in self.predefined_buttons:
      button.pack_forget()

    def make_func(info):
      def the_func():
        self.loadData(info)
        self.calcGraph()
      return the_func

    # for each dictionary of data:
    for info_dict in data_dictionaries:
      # make button
      new_button = tk.Button(self.predefined_frame, text=info_dict["Short Title"], command=make_func(info_dict))

      # add to list and pack
      new_button.pack()
      self.predefined_buttons.append(new_button)

  # function to handle all graph making
  def calcGraph(self):
    # try the following until somegoes wrong possibly
    try:
      graphing.close_plot()
      values = self.getInputValues()  # get all values
      title, x_label, y_label = self.getCustomizationOptions().values()
      best_eq_formatted = graphing.export_graph(values, title, x_label, y_label)   # plot and export graph
      self.loadImage()                # load new image into label for viewing
      self.graph_est_eq_label.config(text="Best Estimate Equation: "+best_eq_formatted)
    
    # if anything goes wrong, tell user and load error image
    except Exception as e:
      messagebox.showerror("There was an error!", f"The error:\n{e}")
      self.loadErrorImage()

  # function to start tkinter mainloop, to keep window up and open
  def startMainLoop(self):
    self.root.mainloop()

# remove data graph at start to refresh
delete_image()

# object of window class
window = Window(title="Mr. Ornelas Grapher")

window.loadData(OREGON)

window.setPredefinedLoadButtons([EXAMPLE, OREGON, GEORGIA, UTAH, MISSISSIPPI, NORTH_DAKOTA])

on_close = lambda : (delete_image(), close_window(window.root))

window.root.protocol("WM_DELETE_WINDOW", on_close)
window.startMainLoop()
