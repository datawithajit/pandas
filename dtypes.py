import pandas as pd

import csv

data = {
    'Employee_ID': [101, 102, 103],
    'Name': ['Rahul', 'Priya', 'Amit'],
    'Age': ['25', '30', '28'],
    'Salary': ['25000', '35000', '40000'],
    'Joining_Date': [
        '2023-01-10',
        '2022-05-15',
        '2024-02-20'
    ]
}


df = pd.read_csv("data.csv",chunksize=1)
for chunk in df:
    print(chunk)


df = pd.read_csv("data.csv", nrows=5) # load 1st 5rows
print(df)



import os

file_size = os.path.getsize("data.csv")

print("File Size in Bytes:", file_size)
print("File Size in MB:", file_size / (1024 * 1024))


'''

Method	Purpose	Example
df.dtypes	Check all column data types	df.dtypes
df.info()	Get DataFrame structure	df.info()
type()	Check individual value type	type(df.loc[0,'Age'])
astype()	Convert column data type	df['Age'].astype(str)
pd.to_numeric()	Convert values to numbers	pd.to_numeric(df['Price'])
pd.to_datetime()	Convert values to dates	pd.to_datetime(df['Date'])
select_dtypes()	Select columns by data type	df.select_dtypes(include='number')

'''

df = pd.DataFrame(data)

# Step 1: Check DataFrame information
df.info()

# Step 2: Check column data types
print(df.dtypes)

# Step 3: Convert Employee_ID into string
df['Employee_ID'] = df['Employee_ID'].astype(str)

# Step 4: Convert Age into numeric
df['Age'] = pd.to_numeric(df['Age'])

# Step 5: Convert Salary into numeric
df['Salary'] = pd.to_numeric(df['Salary'])

# Step 6: Convert Joining_Date into datetime
df['Joining_Date'] = pd.to_datetime(
    df['Joining_Date']
)

# Step 7: Select numeric columns
numeric_columns = df.select_dtypes(
    include='number'
)

# Step 8: Check final data types
print(df.dtypes)

# Step 9: Display cleaned DataFrame
print(df)


'''
What happens in this project?

    Employee_ID → Converted into string because it is an identifier.
    Age → Converted into numeric for calculations.
    Salary → Converted into numeric for salary analysis.
    Joining_Date → Converted into datetime for date analysis.
    select_dtypes() → Extracts numerical columns for further analysis.

Interview Tip: Remember these three important differences:

    astype() – Converts data types when values are compatible with the requested type.
    pd.to_numeric() – Specifically converts values into numeric format and can handle invalid values using errors='coerce'.
    pd.to_datetime() – Converts values into date and time format.

These seven methods are frequently useful in Pandas data cleaning, exploratory data analysis (EDA), and data preprocessing for machine learning.
'''
