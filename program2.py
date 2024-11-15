'''Program #2: Write a GUI program that displays your name and address when a "Show Info" button is clicked.
There should also be a "Quit" button which exists the GUI.'''

import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        # Create the main window widget
        self.main_window = tkinter.Tk()

        # Create a Button widget. The text 'Click Me!'
        # should appear on the face of the Button. The
        # do_something method should be executed when
        # the user clicks the Button.
        self.my_button = tkinter.Button(self.main_window, text='Show me!',
                                        command=self.do_something)
        self.quit_button = tkinter.Button(self.main_window, text='Quit', command = self.main_window.destroy)

        # Pack the Button
        self.my_button.pack(pady=10)
        self.quit_button.pack(pady=10)

        # Enter the tkinter main loop
        tkinter.mainloop()

    # The do_something method is a callback function for the button widget
    def do_something(self):
        # Display an info dialog box
        tkinter.messagebox.showinfo('Information', 'My name is lizzie kerr and I live at Albano Trial, IGH, Minnesota')

# Create an instance of the MyGUI class
if __name__ == '__main__':
    my_gui = MyGUI()
