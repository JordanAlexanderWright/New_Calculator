from tkinter import *
from tkinter import ttk


class Calculator(Tk):

    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.minsize(400, 600)

        self.style = ttk.Style()
        self.style.configure('TEntry', justify='right', foreground='red')

        self.display = ttk.Entry(master=self, takefocus=True, justify='right')
        self.display.pack(fill='x')

        self.display2 = ttk.Entry(master=self, takefocus=False)
        self.display2.pack(fill='x')

calculator = Calculator()
calculator.mainloop()