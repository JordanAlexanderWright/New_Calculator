from tkinter import *
from tkinter import ttk


class Calculator(Tk):

    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.minsize(400, 600)

        self.display_frame = Frame(bg="white", bd=10, height=25, relief="sunken")
        self.display_frame.grid(row=0, column=0, columnspan=3)

        # Need to set two numbers, one for storing the current working number, the other for saving the current work

        self.current_number = StringVar()
        self.current_number.set("0")

        self.saved_number = StringVar()
        self.saved_number.set("0")

        # Creating a variable to decide what to do when hitting =
        self.last_used = [0, 0, ""]

        self.stored_numbers = [0, 0]

        self.display = Label(master=self.display_frame, textvariable=self.current_number, fg="black", anchor="e")
        self.display.grid_propagate(True)
        self.display.grid(rowspan=3)
        self.display.grid_propagate(False)

        self.number_buttons()
        self.function_buttons()

    # Wrapping this so that I can use it in lambda functions

    def display_handling(self, user_entry):

        if self.last_used[0]:
            self.current_number.set("0")
            self.current_number.set(str(user_entry))
            self.last_used[0] = 0

        else:

            if self.current_number.get() == "0":
                self.current_number.set(str(user_entry))

            elif self.current_number.get() != "0":
                current = self.current_number.get()
                new_value = current + str(user_entry)
                self.current_number.set(new_value)

    def function_buttons(self):

        # Making all the function buttons
        equal = ttk.Button(text="=", command=lambda: self.operator_handling("="))
        add = ttk.Button(text="+", command=lambda: self.operator_handling("+"))
        subtract = ttk.Button(text="-", command=lambda: self.operator_handling("-"))
        multiply = ttk.Button(text='*', command=lambda: self.operator_handling("*"))
        divide = ttk.Button(text='/', command=lambda: self.operator_handling("/"))

        # Placing all the function buttons

        add.grid(column=3, row=1)
        subtract.grid(column=3, row=2)
        multiply.grid(column=3, row=3)
        divide.grid(column=3, row=4)
        equal.grid(column=3, row=5)

    def operator_handling(self, operator):

        self.stored_numbers[1] = int(self.current_number.get())
        # need to check if there was an operator used before. this will do the previous function, than carry on
        if self.last_used[1]:

            self.last_used[1] = 0
            self.operator_handling(self.last_used[2])

        if operator == "+":
            answer = sum(self.stored_numbers)
            print(f"You added, answer is {answer}")
            self.addition()
            self.current_number.set((self.saved_number.get()))
            self.last_used[0] = 1
            self.last_used[2] = operator

        elif operator == "-":
            print("You Subtracted")
            self.subtract()
            self.current_number.set((self.saved_number.get()))
            self.last_used[2] = operator

        elif operator == "/":
            print("You Divided")

        elif operator == "*":
            print("You Multiplied")

        elif operator == "=":
            print("Your Result: ")
            self.operator_handling(self.last_used[2])

        else:
            print('Nothing selected')
            self.last_used = operator
            self.saved_number.set(self.current_number.get())
            self.current_number.set("0")

    def addition(self):

        add_result = str(int(self.current_number.get()) + int(self.saved_number.get()))
        self.saved_number.set(add_result)
        self.current_number.set(add_result)
        print(f"Saved: {self.saved_number.get()}")
        print(f"current: {self.current_number.get()}")

    def subtract(self):

        sub_result = str((int(self.saved_number.get())) - int(self.current_number.get()))
        self.saved_number.set(sub_result)
        self.current_number.set("0")
        print(f"Saved: {self.saved_number.get()}")
        print(f"current: {self.current_number.get()}")

    def number_buttons(self):
        # Automating my number list:

        number_list = []

        for number in range(1,10):
            number_list.append(number)

        # Must append 0 at end

        number_list.append(0)

        # Setting variable for button placements

        column_count = 0
        row_count = 1

        # Remember the lambda function will save in place, so I can remember the number it is using.

        for number in number_list:
            btn = ttk.Button(master=self, text=str(number), command=lambda entry=number: self.display_handling(entry))

            if number == 0:

                btn.grid(column=2, row=3, columnspan=3)

            if column_count == 3:

                print(number)
                row_count += 1
                column_count = 0
                btn.grid(column=column_count, row=row_count)
                column_count += 1

            else:
                btn.grid(column=column_count, row=row_count)
                column_count += 1


if __name__ == "__main__":
    window = Calculator()
    window.mainloop()