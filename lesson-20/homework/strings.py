import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")  


tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print(tables)

customers = pd.read_sql_query("SELECT * FROM customers;", conn)
customers.head()

customers = pd.read_sql_query("SELECT * FROM invoices;", conn)
customers.head()
query = """
SELECT c.CustomerId, 
       c.FirstName || ' ' || c.LastName AS CustomerName,
       SUM(i.Total) AS TotalSpent
FROM Customers c
JOIN Invoices i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId, CustomerName
ORDER BY TotalSpent DESC;
"""

df = pd.read_sql_query(query, conn)

conn.close()

df.head()
import sqlite3
import pandas as pd


conn = sqlite3.connect("chinook.db")


query = """
SELECT c.CustomerId, 
       c.FirstName || ' ' || c.LastName AS CustomerName,
       SUM(i.Total) AS TotalSpent
FROM Customers c
JOIN Invoices i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId, CustomerName
ORDER BY TotalSpent DESC
LIMIT 5;
"""

top5 = pd.read_sql_query(query, conn)

conn.close()

top5

import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")


query = """
SELECT c.CustomerId, 
       c.FirstName || ' ' || c.LastName AS CustomerName,
       SUM(i.Total) AS TotalSpent
FROM Customers c
JOIN Invoices i ON c.CustomerId = i.CustomerId
GROUP BY c.CustomerId, CustomerName
ORDER BY TotalSpent DESC
LIMIT 5;
"""

top5_customers = pd.read_sql_query(query, conn)

conn.close()

top5_customers

import sqlite3
import pandas as pd


conn = sqlite3.connect("chinook.db")


albums = pd.read_sql("SELECT * FROM albums", conn)
tracks = pd.read_sql("SELECT * FROM tracks", conn)
invoice_items = pd.read_sql("SELECT * FROM invoice_items", conn)
invoices = pd.read_sql("SELECT * FROM invoices", conn)
customers = pd.read_sql("SELECT * FROM customers", conn)


purchases = invoice_items.merge(invoices, on="InvoiceId")


purchases = purchases.merge(customers, on="CustomerId")


purchases = purchases.merge(tracks[["TrackId", "AlbumId"]], on="TrackId")


album_track_counts = tracks.groupby("AlbumId")["TrackId"].nunique().reset_index()
album_track_counts.rename(columns={"TrackId": "TotalTracks"}, inplace=True)


cust_album_purchases = purchases.groupby(["CustomerId", "AlbumId"])["TrackId"].nunique().reset_index()
cust_album_purchases.rename(columns={"TrackId": "PurchasedTracks"}, inplace=True)


cust_album_purchases = cust_album_purchases.merge(album_track_counts, on="AlbumId")


cust_album_purchases["FullAlbum"] = cust_album_purchases["PurchasedTracks"] == cust_album_purchases["TotalTracks"]


customer_pref = cust_album_purchases.groupby("CustomerId")["FullAlbum"].max().reset_index()
customer_pref["Preference"] = customer_pref["FullAlbum"].apply(lambda x: "Album" if x else "Tracks")


pref_counts = customer_pref["Preference"].value_counts(normalize=True) * 100
print(pref_counts)

import sqlite3
import pandas as pd

conn = sqlite3.connect("chinook.db")

tracks = pd.read_sql("SELECT TrackId, AlbumId FROM tracks", conn)
invoice_items = pd.read_sql("SELECT InvoiceId, TrackId FROM invoice_items", conn)
invoices = pd.read_sql("SELECT InvoiceId, CustomerId FROM invoices", conn)

purchases = invoice_items.merge(invoices, on="InvoiceId").merge(tracks, on="TrackId")

album_track_counts = tracks.groupby("AlbumId")["TrackId"].nunique().reset_index(name="TotalTracks")

cust_album = purchases.groupby(["CustomerId", "AlbumId"])["TrackId"].nunique().reset_index(name="PurchasedTracks")

cust_album = cust_album.merge(album_track_counts, on="AlbumId")

cust_album["FullAlbum"] = cust_album["PurchasedTracks"] == cust_album["TotalTracks"]


customer_pref = cust_album.groupby("CustomerId")["FullAlbum"].max().reset_index()
customer_pref["Preference"] = customer_pref["FullAlbum"].apply(lambda x: "Album" if x else "Tracks")


pref_percent = customer_pref["Preference"].value_counts(normalize=True) * 100

print(pref_percent)

import sqlite3
import pandas as pd


conn = sqlite3.connect("chinook.db")


tracks = pd.read_sql("SELECT TrackId, AlbumId FROM tracks", conn)
invoice_items = pd.read_sql("SELECT InvoiceId, TrackId FROM invoice_items", conn)
invoices = pd.read_sql("SELECT InvoiceId, CustomerId FROM invoices", conn)


purchases = invoice_items.merge(invoices, on="InvoiceId").merge(tracks, on="TrackId")


album_track_counts = tracks.groupby("AlbumId")["TrackId"].nunique().reset_index(name="TotalTracks")


cust_album = purchases.groupby(["CustomerId", "AlbumId"])["TrackId"].nunique().reset_index(name="PurchasedTracks")


cust_album = cust_album.merge(album_track_counts, on="AlbumId")


cust_album["FullAlbum"] = cust_album["PurchasedTracks"] == cust_album["TotalTracks"]


customer_pref = cust_album.groupby("CustomerId")["FullAlbum"].max().reset_index()
customer_pref["Preference"] = customer_pref["FullAlbum"].apply(lambda x: "Full Albums" if x else "Individual Tracks")


summary = customer_pref["Preference"].value_counts(normalize=True).reset_index()
summary.columns = ["Preference", "Percentage"]
summary["Percentage"] = summary["Percentage"] * 100

print(summary)
