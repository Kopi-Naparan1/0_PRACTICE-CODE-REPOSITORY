import argparse
from parser import load_expenses
from summary import summarize_expense


def print_report(summary):
    print(f"Total this month: ${summary['total_this_month']:,.0f}")
    print(f"Top Category: {summary['top_category'][0]} (${summary['top_category'][1]:,.0f})")
    print(f"Biggest Expense: ${summary['biggest_expense']['Amount']:,.0f} on {summary['biggest_expense']['Date'].date()}")
    print(f"Smallest Expense: ${summary['smallest_expense']['Amount']:,.0f}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('report', help='Generate report')
    parser.add_argument('--file', required=True, help='CSV file with expenses')
    args = parser.parse_args()

    expenses = load_expenses(args.file)
    summary = summarize_expense(expenses)
    print_report(summary)

if __name__ == '__main__':
    main()





