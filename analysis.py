from expense_ops import print_expense
from expense_ops import check_empty
import matplotlib.pyplot as plt
import csv

#---------------------⬆️ Other Functions ⬆️------------------------
def View_all_expenses(expense):
    print("--------My Expenses-------\n")
    if check_empty(expense):
        return
    print_expense(expense)
def View_total_amount_spent(expense):
    total=sum(i["amount"] for i in expense)
    print(f"Total Expenses is ₹{total}.\n")
def Category_summary(expense):
    summary={}
    for exp in expense:
        cat=exp["category"]
        amt=exp["amount"]
        if cat in summary:
            summary[cat]+=amt
        else:
            summary[cat]=amt
    print("\n----------Category Summary-----------")
    for k,(i,j) in enumerate(summary.items(),start=1):
        print(f"{k}. {i} - ₹{j}")
def Largest_smallest_expense(expense):
    if check_empty(expense):
        return
    high = max(expense, key=lambda x: x["amount"])
    low = min(expense, key=lambda x: x["amount"])
    print("\n------------Expense Analysis------------")
    print(f"Highest: ₹{high['amount']} - {high['category']} - {high['date']} - {high['note']}")
    print(f"Lowest:  ₹{low['amount']} - {low['category']} - {low['date']} -{low['note']}")
def filter_by_date(expense):
    start = input("Start date (YYYY-MM-DD): ")
    end = input("End date (YYYY-MM-DD): ")
    found=False

    for e in expense:
        if start <= e["date"] <= end:
            print(e)
            found=True
    if not found:
        print(f"\nNo Expense Recorded between {start} and {end}.")

def plot_category_expense(expense):
    if not expense:
        print("No expenses to plot.\n")
        return

    category_total = {}

    for e in expense:
        category_total[e["category"]] = category_total.get(e["category"], 0) + e["amount"]

    categories = list(category_total.keys())
    amounts = list(category_total.values())

    plt.bar(categories, amounts)
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.title("Category-wise Expense Analysis")
    plt.tight_layout()
    plt.show()
    print("Done")

def export_to_csv(expense):
    if not expense:
        print("No Expenses to Report.\n")
        return

    with open("expense_report.csv", "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["id", "amount", "category", "date", "note"]
        )
        writer.writeheader()
        writer.writerows(expense)

    print("Expense Report Exported as expense_report.csv\n")

def monthly_summary(expense):
    summary = {}
    for e in expense:
        date_part = e["date"].split(" ")[0]
        day, month, year = date_part.split("-")
        month_key = f"{year}-{month}"
        if month_key not in summary:
            summary[month_key] = 0
        summary[month_key] += e["amount"]
    if not summary:
        print("No expenses available.")
        return
    print("\n📅 Monthly Expense Summary:")
    for month in sorted(summary):
        print(f"{month} → ₹{summary[month]}")
#--------------------⬆️ Expense Functions ⬆️-----------------------