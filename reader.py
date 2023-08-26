import sys
import csv
import os

input_file_data = []

def bad_input_data(value_type, argv_number):
    print(f"Argv number: {argv_number}. Value provided in argv for {value_type} is incorrect.")
    print("Try again.")

def read_file():
    with open(sys.argv[1], "r") as input_file:
        file_reader = csv.reader(input_file)
        for row_data in file_reader:
            input_file_data.append(row_data)

def edit_data():
    global changes, input_file_data
    for new_value in changes:
        column, row, value = new_value.split(",")
        column, row = int(column), int(row)
        print(f"Column: {column + 1}")
        print(f"Row: {row + 1}")
        print(f"New Value: {value}")
        print(input_file_data[row][column])
        input_file_data[row][column] = value
        print(input_file_data)





def input_file():
    input_file_name = sys.argv[1]
    if os.path.exists(input_file_name):
        return True
    else:
        return False

def argv_check():
    if not input_file():
        print(f"File {sys.argv[1]} not found.")
        return False
    else:
        print("Input file detected.")
        changes = sys.argv[3:]
        for change_number, requested_change in enumerate(changes):
            if "," not in requested_change:
                print("Error. Wrong argv format.")
                return False
            column_row_value = requested_change.split(",")
            if len(column_row_value) != 3:
                print("Error. Wrong argv format.")
                return False
            column = column_row_value[0]
            row = column_row_value[1]
            new_value = column_row_value[2]
            try:
                int(column)
            except ValueError:
                bad_input_data("column", change_number + 3)
                return False
            try:
                int(row)
            except ValueError:
                bad_input_data("row", change_number + 3)
                return False
            print(f"Requested change: {change_number + 1} in column {column}, row {row}, new value: {new_value}")
        return True
    
#RUN APP
if len(sys.argv) < 4:
    print("FATAL ERROR")
    print("NOT ENOUGH DATA")
else:
    if not argv_check():
        pass
    else:
        output_file_name = sys.argv[2]
        read_file()
        print(input_file_data)
        changes = sys.argv[3:]
        print(changes)
        edit_data()
