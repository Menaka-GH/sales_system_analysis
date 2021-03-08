import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def salesData():
    con = sqlite3.connect("sale.db")
    cur = con.cursor()
    try:
       cur.execute("CREATE TABLE salesTable (Order_ID integer, Product text, Quantity integer, Price integer, Order_date date, Address text)")
       print("conne")
       con.commit()
       con.close()
    except ValueError:
       print(("not conn"))

def addSalesData(Order_ID, Product, Quantity, Price, Order_date, Address):
    con = sqlite3.connect("sale.db")
    cur = con.cursor()
    cur.execute("INSERT INTO salesTable VALUES(?,?,?,?,?,?)",(Order_ID, Product, Quantity, Price, Order_date, Address))
    con.commit()
    con.close()

def viewsalesData():
    con = sqlite3.connect("sale.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM salesTable")
    rows = cur.fetchall()
    con.close()
    return rows
def deletesalesData(Order_ID):
    con = sqlite3.connect("sale.db")
    cur = con.cursor()
    cur.execute("DELETE FROM salesTable WHERE Order_ID=?", (Order_ID))
    con.commit()
    con.close()

def searchData(Order_ID="",Product="", Quantity="",Price="", Order_date="", Address=""):
    con = sqlite3.connect("sale.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM salesTable WHERE Order_ID=? OR Product=? OR Quantity=? OR Price=? OR Order_date=? OR Address=? ", (Order_ID, Product, Quantity, Price, Order_date, Address))
    rows = cur.fetchall()
    con.close()
    return rows

def updatedata():
    con = sqlite3.connect("sale.db")
    cur = con.cursor()
    cur.execute(
        "UPDATE salesTable SET Order_ID=?, Product=?, Quantity=?, Price=?, Order_date=?, Address=? ",\
        (Order_ID, Product, Quantity, Price, Order_date, Address, Id))
    con.commit()
    con.close()

def salesAnalysis():
    con = sqlite3.connect("sale.db")
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

#salesData()
