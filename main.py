#-------------------------------------⬇️ Main Program Of Expense Tracker⬇️--------------------------------------------
from storage import load_data, save_data
from analysis import (
    View_total_amount_spent,
    Category_summary,
    Largest_smallest_expense,
    filter_by_date,
    plot_category_expense,
    export_to_csv
)
from expense_ops import (
    Add_expense,
    View_all_expenses,
    Edit_expense,
    Delete_expense,
    Search_expense,
    Exit
)
expense=load_data()
print("\n========== EXPENSE TRACKER ==========\n")
print("1. To Add An Expense")
print("2. View All Expenses")
print("3. View Total Amount Spent")
print("4. Edit/Modify an Expense")
print("5. Delete an Expense")
print("6. Category Summary")
print("7. Search Expense")
print("8. Highest & Lowest Expense")
print("0. Exit Program")
print("11. Export Expense Report (CSV)")
print("22. Display Expenses in a Graph")
print("\n=====================================\n")
while True:
    try:
        N=int(input("Enter Your Choice: "))
    except ValueError:
        print("Invalid input!, Enter a number.\n")
        continue
    if N==0:
        Exit(expense)
        break
    else:
        if N==1:
            Add_expense(expense)
        elif N==2:
            View_all_expenses(expense)
        elif N==3:
            View_total_amount_spent(expense)
        elif N==4:
            Edit_expense(expense)
        elif N==5:
            Delete_expense(expense)
        elif N==6:
            Category_summary(expense)
        elif N==7:
            Search_expense(expense)
        elif N==8:
            Largest_smallest_expense(expense)
        elif N==9:
            filter_by_date(expense)
        elif N==22:
            plot_category_expense(expense)
        elif N==11:
            export_to_csv(expense)
        else:
            print("Invalid choice, Try again.")
            