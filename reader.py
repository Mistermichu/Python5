import sys
import csv
import os

input_file_data = []

def read_file():
    with open(sys.argv[1], "r") as input_file:
        for row_data in input_file:
            input_file_data.append(row_data)

def edit_data():
    

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
        print("Nazwa pliku ok")
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
