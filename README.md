# Restaurant Management System

## Project Overview

The Restaurant Management System is a Python-based application that handles restaurant menus, customer orders and billing. This system is an interactive and menu driven system in which users can carry out important functions like adding items in the menu, ordering items in the menu and generating the bill.


## Purpose

The purpose of this project is to demonstrate fundamental programming concepts in Python, including:

* Object-Oriented Programming (OOP)
* File handling
* Exception handling
* Modular programming



## Features

* Add and manage menu items
* View available menu
* Create and manage customer orders
* Automatically calculate total bill
* Generate and display final bill
* Store menu and order data in files
* Interactive command-line interface



## Project Structure

```
Restaurant_Management_System/
│
├── main.py
├── restaurant.py
├── menu.py
├── order.py
├── customer.py
├── menu.txt
└── orders.txt
```


## How to Run the Program

### Step 1: Open Terminal / Command Prompt

Navigate to the project folder:

```
cd Restaurant_Management_System
```

### Step 2: Run the program

```
python main.py
```



## Example Usage

### Add Menu Items

```
Enter your choice: 1
Enter item name: pizza
Enter price: 250
Enter category: Fast Food
```

```
Enter your choice: 1
Enter item name: Burger
Enter price: 120
Enter category: Fast Food
```

```
Enter your choice: 1
Enter item name: pasta
Enter price: 200
Enter category: Italian
```



### View Menu

```
--- MENU ---
1. pizza (Fast Food) - €250.0
2. Burger (Fast Food) - €120.0
3. pasta (Italian) - €200.0
```



### Add Items to Order

```
Enter your choice: 3
Select item number: 1
Enter quantity: 2
Item added to order!
```

```
Enter your choice: 3
Select item number: 2
Enter quantity: 1
Item added to order!
```

```
Enter your choice: 3
Select item number: 3
Enter quantity: 1
Item added to order!
```

---

### View Order

```
--- Current Order ---
pizza x2 = €500.0
Burger x1 = €120.0
pasta x1 = €200.0
Total = €820.0
```



### Checkout

```
Enter your choice: 5
Enter customer name: Johar
```



### Output

```
===== BILL =====
Customer ID: 7763, Name: Johar

--- Current Order ---
pizza x2 = €500.0
Burger x1 = €120.0
pasta x1 = €200.0
Total = €820.0

Final Total: €820.0
Order completed!
```



## Data Storage

### menu.txt

Stores menu items in the format:

```
name,price,category
```

### orders.txt

Stores order details including:

* Order ID
* Customer name
* Items ordered
* Total amount



## Technologies Used

* Python 3
* File Handling (Text Files)
* Object-Oriented Programming


## Concepts Covered

* Classes and Objects
* Methods and Attributes
* Loops and Conditional Statements
* Exception Handling
* File Input/Output
* Modular Programming



