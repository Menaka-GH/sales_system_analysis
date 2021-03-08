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


        #-----------------------------Frames--------------------------------
        MainFrame = Frame(self.root, bg="grey")
        MainFrame.grid()

        TitleFrame = Frame(MainFrame, bd=2, padx=55, pady=8, bg="white", relief=RIDGE )
        TitleFrame.pack(side=TOP)

        self.lblTitle = Label(TitleFrame, font=('arial', 45, 'bold'), text="Sales Management System", bg="white")
        self.lblTitle.grid()

        ButtonFrame = Frame(MainFrame, bd=2, width=1300, height=75, padx=18, pady=20, bg="white", relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrame = Frame(MainFrame, bd=2, width=1300, height=350, padx=20, pady=20, bg="grey", relief=RIDGE)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, bg="white", relief=RIDGE,
                                   font=('arial', 20, 'bold'), text="Sales Info\n")
        DataFrameLEFT.pack(side=LEFT)

        DataFrameRIGHT =LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, bg="white", relief=RIDGE,
                                   font=('arial', 20, 'bold'), text="Sales Details")
        DataFrameRIGHT.pack(side=RIGHT)

        #---------------------------------labels and entry widget-------------------------

        self.lblOrderId = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Student ID:", padx=2, pady=2,bg="white")
        self.lblOrderId.grid(row=0, column=0, sticky=W )
        self.txtOrderId = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Order_ID, width=38)
        self.txtOrderId.grid(row=0, column=1)

        self.lblProduct = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Product:", padx=2, pady=2, bg="white")
        self.lblProduct.grid(row=1, column=0, sticky=W)
        self.txtProduct = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Product, width=38)
        self.txtProduct.grid(row=1, column=1)

        self.lblQuantity = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Quantity:", padx=2, pady=2, bg="white")
        self.lblQuantity.grid(row=2, column=0, sticky=W )
        self.txtQuantity = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Quantity, width=38)
        self.txtQuantity.grid(row=2, column=1)

        self.lblPrice = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Price:", padx=2, pady=2, bg="white")
        self.lblPrice.grid(row=3, column=0, sticky=W)
        self.txtPrice = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Price, width=38)
        self.txtPrice.grid(row=3, column=1)

        self.lblOrderdate = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Order Date:", padx=2, pady=2,bg="white")
        self.lblOrderdate.grid(row=4, column=0, sticky=W )
        self.txtOrderdate = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Order_date, width=38)
        self.txtOrderdate.grid(row=4, column=1)

        self.lblAddress = Label(DataFrameLEFT, font=('arial', 20, 'bold'), text="Address", padx=2, pady=2,bg="white")
        self.lblAddress.grid(row=5, column=0, sticky=W)
        self.txtAddress = Entry(DataFrameLEFT, font=('arial', 20, 'bold'), textvariable=Address, width=38)
        self.txtAddress.grid(row=5, column=1)
#----------------------listbox and scrollbarwidget-------------------------------
        scrollbar = Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0, column=1, sticky='ns')

        saleslist = Listbox(DataFrameRIGHT, width=41, height=16, font=('arial', 20, 'bold'), yscrollcommand=scrollbar.set )
        saleslist.grid(row=0, column=0, padx=8)
        scrollbar.config(command = saleslist.yview)


#---------------------------------------button widget------------------------------------

        self.btnAddData = Button(ButtonFrame, text="Add New", font=('arial', 20, 'bold'),height=1,width=10,bd=4, command = addData)
        self.btnAddData.grid(row=0, column=0)

        self.btnDisplayData = Button(ButtonFrame, text="Display", font=('arial', 20, 'bold'), height=1, width=10, bd=4,command=displayData)
        self.btnDisplayData.grid(row=0, column=1)


        self.btnclearData = Button(ButtonFrame, text="Clear", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                                 command=clearData)
        self.btnclearData.grid(row=0, column=2)

        self.btndeleteData = Button(ButtonFrame, text="Delete", font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btndeleteData.grid(row=0, column=3)

        self.btnsearchData = Button(ButtonFrame, text="Search", font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnsearchData.grid(row=0, column=4)

        self.btnupdateData = Button(ButtonFrame, text="Update", font=('arial', 20, 'bold'), height=1, width=10, bd=4)
        self.btnupdateData.grid(row=0, column=4)

        self.btnexit = Button(ButtonFrame, text="Exit", font=('arial', 20, 'bold'), height=1, width=10, bd=4, command=Exit)
        self.btnexit.grid(row=0, column=5)
        self.btnexit = Button(ButtonFrame, text="Analyze", font=('arial', 20, 'bold'), height=1, width=10, bd=4,
                              command=analysis)
        self.btnexit.grid(row=0, column=5)

if __name__=='__main__':
    root = Tk()
    application = Sales(root)
    root.mainloop()