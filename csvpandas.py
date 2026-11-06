import pandas as pd
import csv
path = r"/home/ajit/pd/sales copy.csv"
with open(path,"r") as file:
    data = csv.reader(file)
    row = next(data)
print(row)


df = pd.read_csv(path)
print(df)



content = sales_data = [
    {"OrderID": 1001, "Customer": "Rahul", "Product": "Laptop", "Quantity": 2, "Price": 55000, "Region": "West"},
    {"OrderID": 1002, "Customer": "Priya", "Product": "Mouse", "Quantity": 5, "Price": 500, "Region": "South"},
    {"OrderID": 1003, "Customer": "Amit", "Product": "Keyboard", "Quantity": 3, "Price": 1200, "Region": "North"},
    {"OrderID": 1004, "Customer": "Neha", "Product": "Mobile", "Quantity": 1, "Price": 25000, "Region": "East"},
    {"OrderID": 1005, "Customer": "Sneha", "Product": "Monitor", "Quantity": 2, "Price": 15000, "Region": "West"},
    {"OrderID": 1006, "Customer": "Vikas", "Product": "Desk", "Quantity": 1, "Price": 8000, "Region": "North"},
    {"OrderID": 1007, "Customer": "Anjali", "Product": "Chair", "Quantity": 4, "Price": 3500, "Region": "South"},
    {"OrderID": 1008, "Customer": "Rohit", "Product": "Headphones", "Quantity": 3, "Price": 2000, "Region": "East"},
    {"OrderID": 1009, "Customer": "Karan", "Product": "Tablet", "Quantity": 2, "Price": 18000, "Region": "West"},
    {"OrderID": 1010, "Customer": "Pooja", "Product": "Printer", "Quantity": 1, "Price": 12000, "Region": "North"},
    {"OrderID": 1011, "Customer": "Arjun", "Product": "Pen", "Quantity": 20, "Price": 10, "Region": "South"},
    {"OrderID": 1012, "Customer": "Meera", "Product": "Notebook", "Quantity": 15, "Price": 50, "Region": "East"},
]

print(content)


df1 = pd.DataFrame(content)
print(df1)

df.to_csv(r"/home/ajit/Desktop/Copy_orders.csv",index=False,encoding="UTF-8")
print("File written successfully.")


