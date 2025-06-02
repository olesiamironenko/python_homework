import pandas as pd

# Task 3: List Comprehensions Practice
# 3.1: Add code that reads the contents of ../csv/employees.csv into a DataFrame.
df = pd.read_csv("../csv/employees.csv")
# print(df.head(3))

# 3.2: Using a list comprehension, create a list of the employee names, first_name + space + last_name.
#  Print the resulting list.
full_names = [row["first_name"] + " " + row["last_name"] for _, row in df.iterrows()]
print("All employee names:")
print(full_names)

# 3.3: Create a new list that includes full_names containing letter "e". 
# Print the list
names_with_e = [name for name in full_names if "e" in name.lower()]
print("\nNames containing the letter 'e':")
print(names_with_e)