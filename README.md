# Expense Tracker (Python)

## 📌 Overview

Expense Tracker is a command-line based Python application designed to help users record, manage, and analyze their daily expenses. The project focuses on clean code structure, data persistence, and basic data analysis with visualization.

This project is suitable for beginners to intermediate learners and demonstrates real-world programming practices such as modular design, file handling, and data visualization.

---

## 🚀 Features

## Core Features

* Add a new expense (amount, category, date, note)
* View all recorded expenses
* Edit or delete existing expenses
* Persistent storage using JSON

## Analysis Features

* View total amount spent
* Category-wise expense summary
* Identify highest and lowest expenses
* Search expenses by keyword or date range

## Advanced Features

* Export expense report to CSV
* Category-wise expense graph using matplotlib
* Error handling for invalid input and empty data

---

## 🛠 Technologies Used

* **Python 3**
* **JSON** for data storage
* **CSV** for report export
* **Matplotlib** for data visualization

---

## 📂 Project Structure

expense_tracker/
│── main.py              # Entry point of the application
│── expense_ops.py       # CRUD operations (add, edit, delete, view)
│── analysis.py          # Analysis, graphs, and export functions
│── storage.py           # JSON load/save functions
│── expenses.json        # Stored expense data
│── expense_report.csv   # Exported CSV report
│── README.md            # Project documentation

---

## ▶ How to Run the Project

1. Clone or download the repository
2. Open the project folder in VS Code
3. Ensure Python is installed and configured
4. Install required dependency:

   — pip install matplotlib

5. Run the application:

   — python main.py

---

## 📊 Sample Output

## Terminal Output

```
1. ₹150.0 - food - 18-12-2025 18:15 - evening snacks at home
2. ₹300.0 - travel - 18-12-2025 18:15 - went to beach

```

## Graph Output

* Category-wise bar chart showing spending distribution

---

## ✅ Learning Outcomes

* Modular Python programming
* Working with files (JSON & CSV)
* Data aggregation and analysis
* Basic data visualization
* Writing clean, maintainable code

---

## 🔮 Future Improvements

* Monthly and yearly summary graphs
* GUI using Tkinter or PyQt
* Database integration (SQLite)
* User authentication

---

## 👤 Author

**Teja.P**
B.Sc Student | Python Developer (Beginner–Intermediate)

---

## 📄 License

This project is for learning and educational purposes.
