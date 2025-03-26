import csv
import traceback
import os
import custom_module
from datetime import datetime


#  Task 2: Read a CSV File

def read_employees():
    employees_dict = {}
    employees_rows = []

    with open('../csv/employees.csv', 'r') as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                # Store the first row in the dictionary
                employees_dict["fields"] = row
            else:
                employees_rows.append(row)
        # Store all rows, except the first one, in the dictionary
        employees_dict["rows"] = employees_rows 
    
    return employees_dict 

employees = read_employees()

print(f"\nTask 2: employees: \n{employees}")


# Task 3: Find the Column Index

def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

print(f"\nTask 3: employee_id_column: \n{employee_id_column}")


# Task 4: Find the Employee First Name

def first_name(row_number):
    
    first_name_column = column_index("first_name") # 1
    employee_id = row_number

    employee_first_name = employees["rows"][employee_id][first_name_column]

    return employee_first_name

print(f"\nTask 4: employee's first name: \n{first_name(4)}")


# Task 5: Find the Employee: a Function in a Function

def employee_find(employee_id):
    
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    
    matches = list(filter(employee_match, employees["rows"]))
    return matches

print(f"\nTask 5: find employee: \n{employee_find(5)}")


# Task 6: Find the Employee with a Lambda

def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id, employees["rows"]))
    return matches

print(f"\nTask 6: find employee with lambda: \n{employee_find_2(6)}")


# Task 7: Sort the Rows by last_name Using a Lambda

def sort_by_last_name():
    employees["rows"].sort(key=lambda row : row[column_index("last_name")])
    return employees["rows"]

print(f"\nTask 7: sort_by_last_name: \n{sort_by_last_name()}")


# Task 8: Create a dict for an Employee

def employee_dict(row):
    employee_info = {}
    for i, field in enumerate(employees["fields"]):
        if field != "employee_id":
            employee_info[field] = row[i]
    return employee_info

print(f"\nTask 8: sort_by_last_name: \n{employee_dict(employees['rows'][6])}")

# Task 9: A dict of dicts, for All Employees

def all_employees_dict():
    employees_info = {}
    for _, row in enumerate(employees["rows"]):
        empployee_id = row[employee_id_column]
        employees_info[empployee_id] = employee_dict(row)
    return employees_info

print(f"\nTask 9: all_employees_dict: \n{all_employees_dict()}")


# Task 10: Use the os Module

def get_this_value():
    return os.getenv("THISVALUE")

print(f"\nTask 10: os module get_this_value: \n{get_this_value()}")


# Task 11: Creating Your Own Module

def set_that_secret(new_secret):
    return custom_module.set_secret(new_secret)

set_that_secret("swordfish")
print(custom_module.secret)
        
print(f"\nTask 11: custom module set_that_secret: \n{custom_module.secret}")


# Task 12: Read minutes1.csv and minutes2.csv

# Helper function
def read_scv_file(file_path):
    with open(file_path, 'r') as file:
        read_minutes_dict = {}
        read_minutes_rows = []
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                # Store the first row in the dictionary
                read_minutes_dict["fields"] = row
            else:
                read_minutes_rows.append(tuple(row))
        # Store all rows, except the first one, in the dictionary
        read_minutes_dict["rows"] = read_minutes_rows

    return read_minutes_dict

def read_minutes():

    minutes1 = read_scv_file('../csv/minutes1.csv')
    minutes2 = read_scv_file('../csv/minutes2.csv')

    return (minutes1, minutes2)

minutes1, minutes2 = read_minutes()

print(f"\nTask 12: Read minutes1.csv and minutes2.csv: \n{read_minutes()}")


# Task 13: Create minutes_set

def create_minutes_set():

    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])

    minutes_set = set1.union(set2)

    return minutes_set

minutes_set = create_minutes_set()

print(f"\nTask 13: Create minutes_set: \n{len(minutes_set)}")


# Task 14: Convert to datetime

def create_minutes_list():
    minutes_list = list(minutes_set)
    
    minutes_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))

    return minutes_list

minutes_list = create_minutes_list()
print(f"\nTask 14: Convert to datetime: \n{minutes_list}")


# Task 15: Write Out Sorted List


def write_sorted_list():
    try:
        # Sort minutes_list in ascending order of datetime
        minutes_list.sort(key=lambda x: x[1])

        # Convert datetime back into a string
        sorted_list = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))

        # Write to CSV file
        with open("./minutes.csv", "w", newline="") as file:
            writer = csv.writer(file)

            # Write header from minutes1 dictionary
            writer.writerow(minutes1["fields"])

            # Write sorted and formatted rows
            writer.writerows(sorted_list)

        return sorted_list  # Return the final processed list
    
    except Exception as e:
        print(f"An exception occurred. Exception type: {type(e).__name__}")

        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        message = str(e)

        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')

        if message:
            print(f"Exception message: {message}")

        print(f"Stack trace: {stack_trace}")

write_sorted_list()

print(f"\nTask 15: Write Out Sorted List: \n{write_sorted_list()}")

print(f"\nTask 15: Write Out Sorted List: \n{read_scv_file('./minutes.csv')}")

