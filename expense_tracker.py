import csv
import os
from datetime import datetime

FILE_NAME = "expenses.csv"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])

initialize_file()

print("Welcome to Personal Expense Tracker!")
