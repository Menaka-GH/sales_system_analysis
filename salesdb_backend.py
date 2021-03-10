import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def salesData():
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    try:
       cur.execute("CREATE TABLE IF NOT EXISTS salesTable (id INTEGER PRIMARY KEY, Order_ID text, Product text, Quantity text, Price text, Order_date text, Address text)")
       print("conne")
       con.commit()
       con.close()
    except ValueError:
       print(("not conn"))

def addSalesData(Order_ID, Product, Quantity, Price, Order_date, Address):
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    cur.execute("INSERT INTO salesTable VALUES(Null, ?, ?, ?, ?, ?, ?)",(Order_ID, Product, Quantity, Price, Order_date, Address))
    con.commit()
    con.close()

def viewsalesData():
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM salesTable")
    rows = cur.fetchall()
    con.close()
    return rows

def deletesalesData(id):
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    cur.execute("DELETE FROM salesTable WHERE id=?", (id,))
    con.commit()
    con.close()

def searchData(Order_ID="",Product="", Quantity="",Price="", Order_date="", Address=""):
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM salesTable WHERE Order_ID=? OR Product=? OR Quantity=? OR Price=? OR Order_date=? OR Address=? ", (Order_ID, Product, Quantity, Price, Order_date, Address))
    rows = cur.fetchall()
    con.close()
    return rows

def updatedata():
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    cur.execute(
        "UPDATE salesTable SET Order_ID=?, Product=?, Quantity=?, Price=?, Order_date=?, Address=? ",\
        (Order_ID, Product, Quantity, Price, Order_date, Address, Id))
    con.commit()
    con.close()

def salesAnalysis():
    con = sqlite3.connect("sales.db")
    cur = con.cursor()
    query = pd.read_sql_query("""
    SELECT
        Order_ID, Price
    FROM
        salesTable
    ;""", con)
    # for row in df:
    #   print(row)
    # df.head()
    df = pd.DataFrame(query)
    df.plot(kind="bar", x="Order_ID", y="Price")
    plt.show()

    con.commit()
    con.close()

salesData()
