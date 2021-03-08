from tkinter import*
import tkinter.messagebox
import salesdb_backend

class Sales:

    def __init__(self, root):
        self.root = root
        self.root.title("Sales Database Management System")
        self.root.geometry("1300x6000")
        self.root.config(bg="grey")

        Order_ID = StringVar()
        Product = StringVar()
        Quantity = StringVar()
        Price = StringVar()
        Order_date = StringVar()
        Address = StringVar()

        def Exit():
            Exit = tkinter.messagebox.askyesno("Sales database management system", "Confirm to exit")
            if Exit > 0:
                root.destroy()
                return