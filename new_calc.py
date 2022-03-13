from tkinter import *
from tkinter import ttk


class Calculator(Tk):

    def __init__(self):
        super().__init__()

        self.title("Calculator")

        self.display_frame = Frame(bg="white", bd=10, height=25, relief="sunken")
        self.display_frame.grid(column=0, row=0, sticky='e')
        self.display_frame.propagate(0)

        self.button_frame = Frame(bg="black", bd=10, height=2)
        self.button_frame.grid()

        # Need to set two numbers, one for storing the current working number, the other for saving the current work
        # Put into string variables so that I can actively display this information to a user

        self.current_number = StringVar()
        self.current_number.set("0")

        self.saved_number = StringVar()
        self.saved_number.set("0")

        # Creating a variable that will remember my last operator, useful for stringing operations together
        self.last_used = ''

        # This is to set up two stored_ numbers (current and previous, and a flag for display purposes
        # [FLAG, PREVIOUS, CURRENT]

        self.stored_numbers = [0, 0, 0]

        # takefocus allows a user to select the entry field with tab. All others are turned off

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('TEntry', foreground='red')

        # self.style.configure('TButton', foreground='white', background='black', relief='raised',
        #                      focuscolor='none')

        self.style.configure('TButton', background='black', foreground='white', width=10, borderwidth=1, focusthickness=3,
                             focuscolor='none')
        # self.style.map('TButton', background=[('active', 'white')])

        self.current_display = ttk.Entry(master=self.display_frame, textvariable=self.current_number,
                                         takefocus=True, justify='right')
        self.current_display.grid_propagate(0)
        self.current_display.grid()

        self.saved_display = ttk.Entry(master=self.display_frame, textvariable=self.saved_number,
                                       takefocus=False, justify='right')
        self.saved_display.grid()

        # print(self.style.layout('TEntry'))
        # print(self.style.element_options('TEntry.padding'))

        print(self.style.layout('TEntry'))
        print(self.style.element_options('TEntry.padding'))
        print(self.style.lookup('TEntry.padding', 'relief'))
        self.number_buttons()
        self.operator_buttons()

    # Making all the function buttons

    def operator_buttons(self):

        function_list = ['+', '-', '*', '/', '=']
        column_var = 3
        row_var = 2

        for function in function_list:
            btn = ttk.Button(master=self.button_frame, text=function, takefocus=False,
                             command=lambda x=function: self.operator_handling(x))
            btn.grid(column=column_var, row=row_var)
            row_var += 1

    # Making all of the number buttons

    def number_buttons(self):
        # Automating my number list:

        number_list = []

        for number in range(1, 10):
            number_list.append(number)

        # Must append 0 at end, allows for correct placement

        number_list.append(0)

        # Setting variables for button placements

        column_count = 0
        row_count = 2

        # Remember the lambda function will save in place, so I can remember the number it is using.

        for number in number_list:
            btn = ttk.Button(master=self.button_frame, text=str(number), takefocus=False,
                             command=lambda entry=number: self.display_handling(entry))

            if number == 0:

                btn.grid(column=2, row=3, columnspan=3)

            if column_count == 3:

                row_count += 1
                column_count = 0
                btn.grid(column=column_count, row=row_count)
                column_count += 1

            else:
                btn.grid(column=column_count, row=row_count)
                column_count += 1


    # This is the logic for handling the numbers displayed by the calculator.

    def display_handling(self, user_entry):

        if self.stored_numbers[0]:
            self.current_number.set("0")
            self.current_number.set(str(user_entry))
            self.stored_numbers[0] = 0

        else:

            if self.current_number.get() == "0":
                self.current_number.set(str(user_entry))
                self.saved_number.set(str(self.stored_numbers[1]))

            elif self.current_number.get() != "0":
                current = self.current_number.get()
                new_value = current + str(user_entry)
                self.current_number.set(new_value)

    def do_math(self, operator):

        if self.last_used == '':
            pass

        else:
            if operator == "+":
                answer = self.stored_numbers[2] + self.stored_numbers[1]
                print(f"You added, answer is {answer}")
                return answer

            elif operator == "-":

                answer = self.stored_numbers[1] - self.stored_numbers[2]
                print(f"You subtracted, answer is {answer}")
                return answer

            elif operator == "/":
                answer = self.stored_numbers[1] / self.stored_numbers[2]
                print(f"You divided, answer is {answer}")
                return answer

            elif operator == "*":
                answer = self.stored_numbers[1] * self.stored_numbers[2]
                print(f"You multiplied, answer is {answer}")
                return answer

    # Logic for handling of operations

    def operator_handling(self, operator):

        # Converting the current number to a operable value (not a string)
        self.stored_numbers[2] = float(self.current_number.get())

        # need to check if there was an operator used before. this will do the previous function, than carry on

        if operator == "=":
            print(self.last_used)
            answer = self.do_math(self.last_used)

            # Testing for a case of hitting "=" twice will result in no change

            if answer is None:
                answer = self.stored_numbers[1]

            print(f"Your Result:{answer}")

            self.last_used = ""

        elif self.last_used:

            print('help')
            answer = self.do_math(self.last_used)

            self.last_used = operator
            self.stored_numbers[1] = answer
            self.stored_numbers[2] = 0

        # this case is for the very first use after a clear, or on app opening. Will save current number in order to
        # be able to operate on it.

        elif not self.last_used:

            if self.stored_numbers[1]:
                self.last_used = operator
                answer = self.stored_numbers[1]
            else:
                self.last_used = operator
                answer = self.stored_numbers[2]

        # Setting storage, index [0] is a flag for display purposes
        self.stored_numbers[0] = 1
        self.stored_numbers[1] = answer
        self.stored_numbers[2] = 0

        # Setting display of saved number

        if self.saved_number.get() is None:
            self.saved_number.set('0')

        else:
            self.saved_number.set(str(self.stored_numbers[1]))
        self.current_number.set("0")


if __name__ == "__main__":
    window = Calculator()
    window.mainloop()
