import pandas as pd

data = {
    'First Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

df.rename(columns=lambda x: x.strip().lower().replace(" ", "_"), inplace=True)

print(df)

print(df.head(3))

mean_age = df["age"].mean()
print("Mean Age:", mean_age)

print(df[["first_name", "city"]])

import numpy as np

df["salary"] = np.random.randint(50000, 100001, size=len(df))

print(df)


print(df.describe())

import pandas as pd


data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [5000, 6000, 7500, 8000],
    "Expenses": [3000, 3500, 4000, 4500]
}

sales_and_expenses = pd.DataFrame(data)

print(sales_and_expenses)

max_sales = sales_and_expenses["Sales"].max()
max_expenses = sales_and_expenses["Expenses"].max()

print("Maximum Sales:", max_sales)
print("Maximum Expenses:", max_expenses)

min_sales = sales_and_expenses["Sales"].min()
min_expenses = sales_and_expenses["Expenses"].min()

print("Minimum Sales:", min_sales)
print("Minimum Expenses:", min_expenses)

avg_sales = sales_and_expenses["Sales"].mean()
avg_expenses = sales_and_expenses["Expenses"].mean()

print("Average Sales:", avg_sales)
print("Average Expenses:", avg_expenses)

import pandas as pd


data = {
    "Category": ["Rent", "Utilities", "Groceries", "Entertainment"],
    "January": [1200, 200, 300, 150],
    "February": [1300, 220, 320, 160],
    "March": [1400, 240, 330, 170],
    "April": [1500, 250, 350, 180]
}

expenses = pd.DataFrame(data)

print(expenses)
expenses["Max_Expense"] = expenses[["January", "February", "March", "April"]].max(axis=1)

print(expenses[["Category", "Max_Expense"]])

expenses["Min_Expense"] = expenses[["January", "February", "March", "April"]].min(axis=1)

print(expenses[["Category", "Min_Expense"]])

expenses["Avg_Expense"] = expenses[["January", "February", "March", "April"]].mean(axis=1)

print(expenses[["Category", "Avg_Expense"]])

expenses = expenses.set_index("Category")

print(expenses)

