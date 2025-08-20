import pandas as pd

sales_df = pd.read_csv("sales_data.csv")

category_stats = sales_df.groupby("Category").agg(
    Total_Quantity_Sold=("Quantity", "sum"),
    Average_Price=("Price", "mean"),
    Max_Quantity_Single_Transaction=("Quantity", "max")
).reset_index()

print(category_stats)

import pandas as pd

sales_df = pd.read_csv("sales_data.csv")

product_sales = sales_df.groupby(["Category", "Product"]).agg(
    Total_Quantity_Sold=("Quantity", "sum")
).reset_index()


top_products = product_sales.loc[
    product_sales.groupby("Category")["Total_Quantity_Sold"].idxmax()
].reset_index(drop=True)

print(top_products)

import pandas as pd

sales_df = pd.read_csv("sales_data.csv")

sales_df["Sales"] = sales_df["Quantity"] * sales_df["Price"]

daily_sales = sales_df.groupby("Date").agg(
    Total_Sales=("Sales", "sum")
).reset_index()

max_sales_day = daily_sales.loc[daily_sales["Total_Sales"].idxmax()]

print("Date with highest sales:", max_sales_day["Date"])
print("Total sales on that date:", max_sales_day["Total_Sales"])

import pandas as pd

orders_df = pd.read_csv("customer_orders.csv")

customer_order_counts = orders_df.groupby("CustomerID")["OrderID"].nunique()

eligible_customers = customer_order_counts[customer_order_counts >= 20].index

filtered_orders = orders_df[orders_df["CustomerID"].isin(eligible_customers)]

print(filtered_orders)

import pandas as pd

orders_df = pd.read_csv("customer_orders.csv")

customer_avg_price = orders_df.groupby("CustomerID").agg(
    Avg_Price_Per_Unit=("Price", "mean")
).reset_index()

high_value_customers = customer_avg_price[customer_avg_price["Avg_Price_Per_Unit"] > 120]

print(high_value_customers)

import pandas as pd

orders_df = pd.read_csv("customer_orders.csv")

orders_df["TotalPrice"] = orders_df["Quantity"] * orders_df["Price"]

product_summary = orders_df.groupby("Product").agg(
    Total_Quantity=("Quantity", "sum"),
    Total_Price=("TotalPrice", "sum")
).reset_index()

filtered_products = product_summary[product_summary["Total_Quantity"] >= 5]

print(filtered_products)

import sqlite3

conn = sqlite3.connect("population.db")
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(population);")
columns = cursor.fetchall()

for col in columns:
    print(col)

conn.close()

import sqlite3
import pandas as pd


bands = pd.read_csv("population_salary_analysis.csv")


conn = sqlite3.connect("population.db")
population = pd.read_sql("SELECT * FROM population", conn)
conn.close()


def assign_band(salary):
    for _, row in bands.iterrows():
        if row['MinSalary'] <= salary <= row['MaxSalary']:
            return row['Band']
    return None

population['SalaryBand'] = population['Salary'].apply(assign_band)


summary = population.groupby('SalaryBand').agg(
    PopulationCount=('Salary', 'count'),
    AvgSalary=('Salary', 'mean'),
    MedianSalary=('Salary', 'median')
).reset_index()


total_pop = len(population)
summary['PopulationPercent'] = (summary['PopulationCount'] / total_pop) * 100

print("Overall Summary:")
print(summary)


summary_state = population.groupby(['State', 'SalaryBand']).agg(
    PopulationCount=('Salary', 'count'),
    AvgSalary=('Salary', 'mean'),
    MedianSalary=('Salary', 'median')
).reset_index()


state_totals = population.groupby('State')['Salary'].count().reset_index(name='TotalStatePop')
summary_state = summary_state.merge(state_totals, on='State')
summary_state['PopulationPercent'] = (summary_state['PopulationCount'] / summary_state['TotalStatePop']) * 100
summary_state.drop(columns=['TotalStatePop'], inplace=True)

print("\nSummary by State:")
print(summary_state)

