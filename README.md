# 💰 Budget App

A simple command-line **Budget App** built with **Python**, designed to manage personal finances using **Object-Oriented Programming (OOP)** concepts.

This project allows users to create budget categories, deposit money, withdraw funds, transfer money between categories, and visualize spending with a percentage chart.

---

## ✨ Features

- 💵 Deposit money into categories
- 💸 Withdraw money with balance checking
- 🔄 Transfer funds between categories
- 📊 Generate a spending percentage chart
- 📒 Store transaction history (ledger)
- 🧱 Clean OOP-based implementation

---

## 📂 Project Structure

```
budget-app/
│
├── budget.py
└── README.md
```

---

## 🧠 OOP Concepts Used

- Classes & Objects
- Constructors (`__init__`)
- Encapsulation
- Methods
- Object Interaction
- String Representation (`__str__`)

---

## 📋 Class Overview

### Category

Represents a budget category such as:

- Food
- Entertainment
- Clothing
- Transportation

### Methods

| Method | Description |
|---------|-------------|
| `deposit()` | Adds money to the category |
| `withdraw()` | Removes money if sufficient balance exists |
| `transfer()` | Transfers money to another category |
| `get_balance()` | Returns the current balance |
| `check_funds()` | Checks if enough balance is available |
| `__str__()` | Returns a formatted ledger |

---

## 📊 Spend Chart

The project includes a function that generates a vertical bar chart showing the percentage of spending in each category.

Example:

```
Percentage spent by category
100|
 90|
 80|
 70|
 60| o
 50| o
 40| o
 30| o
 20| o  o
 10| o  o
  0| o  o  o
    ----------
     F  C  A
     o  l  u
     o  o  t
     d  t  o
        h
        i
        n
        g
```

---

## 🚀 How to Run

Clone the repository:

```bash
git clone https://github.com/yourusername/budget-app.git
```

Move into the project folder:

```bash
cd budget-app
```

Run the program:

```bash
python budget.py
```

---

## 🎯 Learning Outcomes

This project helped reinforce:

- Object-Oriented Programming
- Python Lists & Dictionaries
- Data Formatting
- Method Design
- Code Organization
- Financial Data Management

---

## 🛠️ Technologies Used

- Python 3

---

## 📌 Future Improvements

- Save transactions to a file
- Load previous budget data
- Menu-driven interface
- GUI version using Tkinter or PyQt
- Data visualization with Matplotlib

---

## 👨‍💻 Author

**Mahadi**

BSBIT Student • Python Developer • AI Enthusiast

GitHub: https://github.com/mahadiurrehman-pixel
Linked in:www.linkedin.com/in/mahadi-ur-rehman-siddiqui-139b93386

---

⭐ If you found this project useful, consider giving it a star!
