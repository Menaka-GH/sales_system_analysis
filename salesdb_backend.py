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
