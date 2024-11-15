#Create a GUI window that displays your favorite saying.


import tkinter

class MyGUI:
    def __init__(self):
        # Create the main window widget.
        self.main_window = tkinter.Tk()

        # Title.
        self.main_window.title('Program 1 saying')

        self.label = tkinter.Label(self.main_window, text="It is never too late to be what you might have been.")
        self.label.pack(pady=20)

        # Enter the tkinter main loop.
        tkinter.mainloop()

# Create an instance of the MyGUI class.
if __name__ == '__main__':
    my_gui = MyGUI()
