import sys
import csv
import os

def input_file():
    input_file_name = sys.argv[1]
    if os.path.exists(input_file_name):
        return True
    else:
        return False

def argv_check():
    if not input_file():
        print(f"File {sys.argv[1]} not found.")
    else:
        pass

def run_app():
    if len(sys.argv) < 4:
        print("FATAL ERROR")
        print("NOT ENOUGH DATA")
    else:
        argv_check()

run_app()
