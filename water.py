# import necessary modules and libraries
from tkinter import *
import datetime

# initialize the water intake tracker
water_tracker = []

# define the GUI interface
class WaterTrackerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Water Tracker")

        # create the input form
        self.form_frame = Frame(master)
        self.form_frame.pack()

        self.form_label = Label(self.form_frame, text="Enter amount of water consumed (in ml):")
        self.form_label.pack()

        self.form_entry = Entry(self.form_frame)
        self.form_entry.pack()

        self.form_button = Button(self.form_frame, text="Submit", command=self.submit_entry)
        self.form_button.pack()

        # create the water intake log
        self.log_frame = Frame(master)
        self.log_frame.pack()

        self.log_label = Label(self.log_frame, text="Water Intake Log:")
        self.log_label.pack()

        self.log_listbox = Listbox(self.log_frame)
        self.log_listbox.pack()

        # load the existing water intake log, if it exists
        try:
            with open("water_log.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    self.log_listbox.insert(END, line.strip())
                    water_tracker.append(int(line.strip()))
        except:
            pass

    # define a function to submit a new water intake entry
    def submit_entry(self):
        try:
            amount = int(self.form_entry.get())
            water_tracker.append(amount)
            self.log_listbox.insert(END, f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}: {amount} ml")
            self.form_entry.delete(0, END)

            # save the updated water intake log
            with open("water_log.txt", "w") as f:
                for amount in water_tracker:
                    f.write(str(amount) + "\n")
        except:
            pass

# create and run the GUI application
root = Tk()
water_tracker_gui = WaterTrackerGUI(root)
root.mainloop()