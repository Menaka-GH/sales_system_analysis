# sales_system_analysis
1. The sales system analysis project is about the database connectivity(SQLite) using Python.
2. I have done CRUD operations which is Create, Read, Update and Delete.
3. I have created the table salesTable in the database "sales.db"
4. Also I have imported the file "all_data.csv" with the data of "sales".
5. Using all_data.csv, I have created the visualizations.

Libraries to import
-------------------

from tkinter import*
import tkinter.messagebox
import sqlite3
import pandas as pd
import os
import matplotlib.pyplot

Class and functions: main.py
----------------------------
1. created the class "Sales"
2. Functions:    addData(), displayData, searchsalesData(), updatesalesData(), analysis()

Functions added in "salesdb_backend.py"
---------------------------------------
salesData()       - creating the table "salesTable"
addSalesData()    - inserting records into the table "salesTable"
viewsalesData()   - This function will return the rows and display the records from the table.
deletesalesData() - to delete the data from the table.
searchData()      - to search the records in the table.
updatedata()      - to update the data.
salesAnalysis()   - to analyze the data from the csv file "all_data". I have visualized the data for "which is the best month for sales?"

How to run the application:
--------------------------
1. Enter the data in the textboxes for order id, product, quantity, price etc
2. Click "Add New"
3. If you click "Display", it will show the records in the "Sales Details" frame
4. To clear the data in the textboxes, click "clear".
5. To delete the records, first click "Display", then select the record from the "Sales Details" frame. Finally click "Delete".
6. To update the record,  first click "Display", then select the record from the "Sales Details" frame. 
   Then change the values in the textbox, finally click "Update".
7. To search the record, type any value (which is already in the database) in the textboxes(order id, product etc), 
   then click "Search", the result will be displayed in the "Sales Details"
8. If you click "Analyze", the bar chart for the data will show.
9. To exit the application click "Exit".     

