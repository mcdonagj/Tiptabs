import tkinter as tk


class UserInterface:
    user_input = ""
    entry_field = None
    window = None
    calculator = None

    def __init__(self, title, calculator):
        """
        __init__() - Constructor for the Tiptabs User Interface.
        :param title: Title of the UI window.
        :param calculator: Tiptabs object.
        """
        self.calculator = calculator

        # Declare the frame of the UI
        self.window = tk.Tk()

        # Set the title of the UI frame.
        self.window.title(title)

        # Create a label for the UI application name.
        lbl_name = tk.Label(text="Tiptabs, V3.7")
        lbl_name.grid(column=0, row=0)

        # Create a entry field for inputting the bill amount.
        self.entry_field = tk.Entry()
        self.entry_field.grid(column=0, row=1)

        # Create a button for calculating the total amount.
        btn_calc = tk.Button(self.window, text="Calculate Amount", command=lambda: self.retrieve_input())
        btn_calc.grid(column=0, row=2)

        # Set the size of the UI frame.
        self.window.geometry("400x400")

        # Call mainloop() to run the UI window.
        self.window.mainloop()

    def retrieve_input(self):
        """
        retrieve_input() - Helper function for retrieving input from the fields within the UI.
        :return: Boolean indicating valid input placed into the calculator.
        """
        input_text = str(self.entry_field.get())
        valid_input = self.check_input(input_text)

        if valid_input:
            self.calculator.set_amount(float(input_text.strip()))

        return valid_input

    def check_input(self, desired_input_text):
        """
        check_input(str) - Helper function for verifying input given in the Tkinter GUI.
        :param desired_input_text: String containing input from all fields in the GUI input fields.
        :return: Boolean condition indicated whether valid input was given.
        """
        result = False

        check_str_len = len(desired_input_text.strip()) > 0

        if check_str_len:
            result = True

        return result
