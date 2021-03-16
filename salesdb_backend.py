import datetime
import sqlite3
import pandas as pd
import os
import matplotlib.pyplot as plt


def salesData():
    con = sqlite3.connect("salessys.db")
    cur = con.cursor()
    try:
       cur.execute("CREATE TABLE IF NOT EXISTS salestable (id INTEGER PRIMARY KEY, Order_ID INTEGER, Product text, Quantity INTEGER, Price INTEGER, Order_date INTEGER, Address text)")
       print("conne")
       con.commit()
       con.close()
    except ValueError:
       print(("not conn"))

def addSalesData(Order_ID, Product, Quantity, Price, Order_date, Address):
    con = sqlite3.connect("salessys.db")
    cur = con.cursor()
    cur.execute("INSERT INTO salestable VALUES(Null, ?, ?, ?, ?, ?, ?)",(Order_ID, Product, Quantity, Price, Order_date, Address))
    con.commit()
    con.close()

def viewsalesData():
    con = sqlite3.connect("salessys.db")
    cur = con.cursor()
    cur.execute("SELECT id, Order_ID, Product, Quantity, Price, Order_date, Address, (Quantity*Price) as sales FROM salestable")
    rows = cur.fetchall()
    con.close()
    return rows

def deletesalesData(id):
    con = sqlite3.connect("salessys.db")
    cur = con.cursor()
    cur.execute("DELETE FROM salestable WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(Order_ID="",Product="", Quantity="",Price="", Order_date="", Address=""):
    con = sqlite3.connect("salessys.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM salestable WHERE Order_ID=? OR Product=? OR Quantity=? OR Price=? OR Order_date=? OR Address=? ", (Order_ID, Product, Quantity, Price, Order_date, Address))
    rows = cur.fetchall()
    con.close()
    return rows

def updatedata():
    con = sqlite3.connect("salessys.db")
    cur = con.cursor()
    cur.execute(
        "UPDATE salestable SET Order_ID=?, Product=?, Quantity=?, Price=?, Order_date=?, Address=? ",\
        (Order_ID, Product, Quantity, Price, Order_date, Address, Id))
    con.commit()
    con.close()

def salesAnalysis1():
    con = sqlite3.connect("salessys.db")
    cur = con.cursor()
    #cur.execute("select Order_ID, (Quantity*Price) as sales from salestable")
    cur.execute("select strftime('%m', datetime(Order_date, 'unixepoch')) as month from salestable")
    
    months = cur.fetchall()
    for month in months:
        print(month)
    con.commit()
    con.close()

def salesAnalysis():
    #df = pd.read_csv("Sales_Data\Sales_April_2019.csv")
    #files = [file for file in os.listdir("Sales_Data")]
    #creating empty dataframe
    #all_months_data = pd.DataFrame()

    #for file in files:
        #df= pd.read_csv("Sales_Data/" +file)
        #merging to the empty dataframe
        #all_months_data = pd.concat([all_months_data,df])
        #checking-single csv file containing 12months data
    #all_months_data.to_csv("all_data.csv", index=False)
        #reading the updated datafram
    all_data = pd.read_csv("all_data.csv")
    #print(all_data.head())
#Problem : 1, what was the best month for sales and how much?
#add month column
#non_df = all_data[all_data.isna().any(axis=1)]
#removing Nan values in the data
    all_data = all_data.dropna(how='all')
#print(all_data.head())
#removing rows, find 'or' and delete it
#df_dummy=all_data[all_data['Order Date'].str[0:2]!='Or']
#get first 2 chars
#all_data['Month'] = all_data[all_data['Order Date'].str[0:2]!='Or']
    all_data['Month'] = all_data['Order Date'].str[0:2]
#pd.to_numeric(s, errors='coerce')
#to turn the data, string to int
#all_data['Month'] = all_data['Month'].astype('int')
#print(all_data.head())
#add sales column
#change into inteer
    all_data['Month'] = pd.to_numeric(all_data['Month'],errors='coerce')
    all_data['Quantity Ordered'] = pd.to_numeric(all_data['Quantity Ordered'],errors='coerce')
#all_data['Quantity Ordered'] = all_data['Quantity Ordered'].astype('int')
    all_data['Price Each'] = pd.to_numeric(all_data['Price Each'],errors='coerce')
#all_data['Price Each'] = all_data['Price Each'].astype('int')
    all_data['Sales'] = all_data['Quantity Ordered'] * all_data['Price Each']
    #print(all_data.head())
#print(all_data.dtypes)
#print(all_data.groupby('Month').sum())
    months = range(1,13)
       #print(months)
    results = all_data.groupby('Month').sum()
#print(results)
    plt.xlabel("Months")
    plt.ylabel("Sales")
    plt.title('Best month for Sales')
    plt.bar(months, results['Sales'])
    plt.show()
   

salesData()
