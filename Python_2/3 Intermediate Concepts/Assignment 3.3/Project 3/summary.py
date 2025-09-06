from collections import defaultdict
from datetime import datetime




def summarize_expense(expenses):
    now = datetime.now()
    this_month = [e for e in expenses if e['Date'].month == now.month and e['Date'].year == now.year]

    total_this_month = sum(e['Amount'] for e in this_month)

    category_totals = defaultdict(float)

    for e in expenses:
        category_totals[e['Category']] += e["Amount"]

        biggest = max(expenses, key=lambda x: x['Amount'])
        smallest = min(expenses, key=lambda x: x['Amount'])

        top_category = max(category_totals.items(), key=lambda x: x[1])

        return {
            'total_this_month': total_this_month,
            'top_category': top_category,
            'biggest_expense': biggest,
            'smallest_expense': smallest
        }



