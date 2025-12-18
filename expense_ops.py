from datetime import datetime
from storage import save_data

def print_expense(expense):
    for k,i in enumerate(expense):
        print(f"{k+1}. ₹{i['amount']} - {i['category']} - {i['date']} - {i['note']}")
    return
def check_empty(expense):
    if not expense:
        print("No expenses are recorded.\n")
        return True
    return False
#---------------------⬆️ Other Functions ⬆️------------------------
def Add_expense(expense):
    try:
        x=float(input("Enter Amount: "))
    except ValueError:
        print("Invalid amount!, Enter a number.\n")
        return
    y=input("Enter Category: ").lower()
    note=input("Enter Note: ")
    expense.append({"id": len(expense)+1,"amount": x,"category": y,"date": datetime.now().strftime("%d-%m-%Y %H:%M"),"note": note})
    save_data(expense)
    print("Added Successfully.\n")
def Exit(expense):
    save_data(expense)
    print("Program Closed")
def View_all_expenses(expense):
    print("--------My Expenses-------\n")
    if check_empty(expense):
        return
    print_expense(expense)
def Delete_expense(expense):
    if check_empty(expense):
        return
    print_expense(expense)
    try:
        delete=int(input("Enter the index to Delete "))
        delete-=1
    except ValueError:
        print("Invalid input!, Enter valid index.\n")
        return
    if delete<0 or delete>=len(expense):
        print("Index Out Of Range.\n")
        return
    del expense[delete]
    save_data(expense)
    print("Successfully Deleted the expense.\n")
def Edit_expense(expense):
    if check_empty(expense):
        return
    print_expense(expense)
    try:
        Edit=int(input("Enter the index to Edit/Modify: "))
        Edit-=1
    except ValueError:
        print("Invalid input!, Enter valid index.\n")
    if Edit < 0 or Edit >= len(expense):
        print("Index Out Of Range.\n")
        return
    while True:
        try:
            new_amount = float(input("Enter New Amount: "))
            break
        except ValueError:
            print("Invalid amount! Enter a number.")
    new_category=input("Enter New Category: ").lower()
    new_note=input("Enter New Note: ")
    expense[Edit]["amount"]=new_amount
    expense[Edit]["category"]=new_category
    expense[Edit]["Note"]=new_note
    save_data(expense)
    print("Succussfully Updated Your Expense.\n")
def Search_expense(expense):
    search_item=input("Enter Search Category/Amount/Date: ").lower()
    results=[]
    for exp in expense:
        if search_item in exp["category"] or search_item in str(exp["amount"]) or search_item in exp["date"]:
            results.append(exp)
    if not results:
        print("No Results Found!\n")
        return
    print("\n-----------Search Results------------")
    for i,exp in enumerate(results, 1):
        print(f"{i}. ₹{exp['amount']} - {exp['category']} - {exp['date']} - {exp['note']}")