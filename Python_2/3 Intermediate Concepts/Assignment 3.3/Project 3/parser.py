import csv
from datetime import datetime

def load_expenses(file):
    expenses = []
    with open(file, mode='r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            expenses.append({
                'Date': datetime.strptime(row['Date'], '%Y-%m-%d'),
                'Category': row['Category'],
                'Amount': float(row['Amount']),
            })
    return expenses
