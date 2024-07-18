import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
from controller.library import controller

# Function to create and update plots
def update_plots():
	try:
		# Retrieve values from input fields
		kp = float(param1_entry.get())
		ki = float(param2_entry.get())
		kd = float(param3_entry.get())
		Initial_Angle = float(param4_entry.get())
		Ball_Initial_Pos = float(param5_entry.get())
		final_position = float(param6_entry.get())
		iterations = int(param7_entry.get())
		
		
		# Data for plotting
		myController = controller(	type="PID", 
							example="ball", 
							iterations=iterations)

		myController.Run( kp=kp, ki=ki, kd=kd, 
		Ball_Final_Pos = final_position,
		Initial_Angle  = Initial_Angle,
		Ball_Initial_Pos = 	Ball_Initial_Pos)
		


		
		# Redraw the canvas
		canvas.draw()
	except ValueError:
		tk.messagebox.showerror("Invalid Input", "Please enter valid numbers.")

# Start button callback
def start_plotting():
	update_plots()
"""
# Stop button callback
def stop_plotting():
	# Optionally, you can implement stopping functionality here
	print("Stop button clicked")
"""


# Create the main window
root = tk.Tk()
root.title("PID controller simulation")

# Create and place widgets
control_frame = tk.Frame(root)
control_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.Y)

# Float input fields
tk.Label(control_frame, text="Kp:").pack(pady=5)
param1_entry = tk.Entry(control_frame)
param1_entry.insert(0, "0.1")  # Set initial value
param1_entry.pack(pady=5)

tk.Label(control_frame, text="Ki:").pack(pady=5)
param2_entry = tk.Entry(control_frame)
param2_entry.insert(0, "0.18")  # Set initial value
param2_entry.pack(pady=5)

tk.Label(control_frame, text="Kd:").pack(pady=5)
param3_entry = tk.Entry(control_frame)
param3_entry.insert(0, "0.45")  # Set initial value
param3_entry.pack(pady=5)



tk.Label(control_frame, text="Bar initial tilt angle:").pack(pady=5)
param4_entry = tk.Entry(control_frame)
param4_entry.insert(0, "10")  # Set initial value
param4_entry.pack(pady=5)

tk.Label(control_frame, text="Ball's initial position:").pack(pady=5)
param5_entry = tk.Entry(control_frame)
param5_entry.insert(0, "3")  # Set initial value
param5_entry.pack(pady=5)

tk.Label(control_frame, text="Ball's desired balance position:").pack(pady=5)
param6_entry = tk.Entry(control_frame)
param6_entry.insert(0, "0")  # Set initial value
param6_entry.pack(pady=5)

tk.Label(control_frame, text="Maximum number of iterations:").pack(pady=5)
param7_entry = tk.Entry(control_frame)
param7_entry.insert(0, "100")  # Set initial value
param7_entry.pack(pady=5)

# Start and Stop buttons
start_button = tk.Button(control_frame, text="Start", command=start_plotting)
start_button.pack(pady=5)

"""
stop_button = tk.Button(control_frame, text="Stop", command=stop_plotting)
stop_button.pack(pady=5)
"""

# Create a frame for the plots
plot_frame = tk.Frame(root)
plot_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Create plots
#fig = plt.figure(figsize=(10, 5))

#ax1 = plt.subplot2grid((1, 2), (0, 0), rowspan=1, colspan=1)
#ax2 = plt.subplot2grid((1, 2), (0, 1), rowspan=1, colspan=1)


# Create a canvas to display the plots
#canvas = FigureCanvasTkAgg(fig, master=plot_frame)
#canvas.draw()
#canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Run the application
root.mainloop()
