# sales_system_analysis
-----------------------
1. The sales system analysis project is about the database connectivity(SQLite) using Python.
2. I have done CRUD operations which is Create, Read, Update and Delete.
3. I have created the table salesTable in the database "sales.db"
4. Also I have imported the file "all_data.csv" with the data of "sales".
5. Using all_data.csv, I have created the visualizations.

Libraries to install
--------------------

1. pip install tkinter
2. pip install tkinter.messagebox
3. pip install sqlite3
4. pip install pandas 
5. pip install os
6. pip install matplotlib.pyplot

HOW TO RUN THE APPLICATION
----------------------------

1. Run the file "main.py".
2. Enter the data in the textboxes for order id, product, quantity, price etc
3. Click "Add New"
4. If you click "Display", it will show the records in the "Sales Details" frame
5. To clear the data in the textboxes, click "clear".
6. To delete the records, first click "Display", then select the record from the "Sales Details" frame. Finally click "Delete".
7. To update the record,  first click "Display", then select the record from the "Sales Details" frame. 
   Then change the values in the textbox, finally click "Update".
8. To search the record, type any value (which is already in the database) in the textboxes(order id, product etc), 
   then click "Search", the result will be displayed in the "Sales Details"
9. If you click "Analyze", the bar chart for the data will show.
10. To exit the application click "Exit".     




Features added from the Project Requirements
----------------------------------------------
 •	Implement a “master loop” console application where the user can repeatedly enter commands/perform actions, including choosing to exit the program

 •	Create a class, then create at least one object of that class and populate it with data

 •	Create and call at least 3 functions, at least one of which must return a value that is used
 
 •	Read data from an external file, such as text, JSON, CSV, etc and use that data in your application

 •	Visualize data in a graph, chart, or other visual representation of data

 •	Use pandas, matplotlib, and/or numpy to perform a data analysis project. Ingest 2 or more pieces of data, analyze that data in some manner, and display a new result to a graph, chart, or other display

 
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

