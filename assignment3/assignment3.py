import numpy as np
import pandas as pd
import os


"""Task 1: Introduction to Pandas - Creating and Manipulating DataFrames"""

# 1. Create a DataFrame from a dictionary
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
print(f"\nTask 1.1: DataFrame from a dictionary: \n{df}")
task1_data_frame = df

# 2. Add a new column
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(f"\nTask 1.2: Add a new column: \n{task1_with_salary}")

# 3. Modify an existing column
task1_older = task1_with_salary.copy()
task1_older['Age'] = task1_older['Age'] + 1
print(f"\nTask 1.3: Modify an existing column: \n{task1_older}")

# 4. Save the DataFrame as a CSV file 
task1_older.to_csv('employees.csv', index=False)
# print(pd.read_csv('employees.csv').head())


"""Task 2: Loading Data from CSV and JSON"""

# 1. Read data from a CSV file
task2_employees = pd.read_csv('employees.csv')
print(f"\nTask 2.1: Read data from a CSV file: \n{task2_employees.head()}")

# 2. Read data from a JSON file
json_employees = pd.read_json('additional_employees.json')
print(f"\nTask 2.2: Read data from a JSON file: \n{json_employees}")

# 3. Combine DataFrames
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(f"\nTask 2.3: Combine DataFrames: \n{more_employees}")


"""Task 3: Data Inspection - Using Head, Tail, and Info Methods"""

# 1. Use the head() method
first_three = more_employees.head(3)
print(f"\nTask 3.1: the head() method: \n{first_three}")

# 2. Use the tail() method
last_two = more_employees.tail(2)
print(f"\nTask 3.2: the tail() method: \n{last_two}")

# 3. Get the shape of a DataFrame
employee_shape = more_employees.shape
print(f"\nTask 3.3: Get the shape of a DataFrame: \n{employee_shape}")

# 4. Use the info() method
print(f"\nTask 3.4: the info() method: ")
more_employees.info()


"""Task 4: Data Cleaning"""

# 1. Create a DataFrame from dirty_data.csv file and assign it to the variable dirty_data
dirty_data = pd.read_csv('dirty_data.csv')
print(f"\nTask 4.1: dirty_data DataFrame from dirty_data.csv file: \n{dirty_data}")

clean_data = dirty_data.copy()

# 2. Remove any duplicate rows from the DataFrame
clean_data.drop_duplicates(inplace=True)
print(f"\nTask 4.2: Remove any duplicate: \n{clean_data}")

# 3. Convert Age to numeric and handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors='coerce')
print(f"\nTask 4.3: Convert Age to numeric and handle missing values: \n{clean_data}")

# 4. 
# Convert Salary to numeric and 
# replace known placeholders (unknown, n/a) with NaN
clean_data['Salary'] = clean_data['Salary'].str.strip().replace(['unknown', 'n/a'], np.nan)
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'])
print(f"\nTask 4.4: Convert Salary to numeric and replace known placeholders (unknown, n/a) with NaN: \n{clean_data}")

# 5. 
# Fill missing numeric values (use fillna).  
# Fill Age which the mean and 
# Salary with the median
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
clean_data['Salary'] = clean_data['Salary'].fillna(clean_data['Salary'].median())
print(f"\nTask 4.5: Fill missing numeric values (use fillna). Fill Age which the mean and Salary with the median: \n{clean_data}")

# 6. Convert Hire Date to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors='coerce')
print(f"\nTask 4.6: Convert Hire Date to datetime: \n{clean_data}")

# 7. 
# Strip extra whitespace and 
# standardize Name and Department as uppercase
clean_data['Name'] = clean_data['Name'].str.strip().str.upper()
clean_data['Department'] = clean_data['Department'].str.strip().str.upper()
print(f"\nTask 4.7: Strip extra whitespace and standardize Name and Department as uppercase: \n{clean_data}")
