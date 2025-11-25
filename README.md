# PRODUCT-STOCK-CRUD-MANAGER

The Product Stock CRUD Manager is a simple yet efficient Python-based inventory management system. It allows users to Create, Read, Update, and Delete (CRUD) product records stored locally in a JSON-formatted data file.
This project is perfect for beginners learning Python file handling, data persistence using JSON, and building menu-driven programs.


---

**🚀 Features.** -

Add Products
Easily insert new product entries with name, cost, and quantity.

View Product List
Display all stored items in a clean, tabular format.

Update Product Quantity
Change quantity of any product by referencing its unique ID.

Delete Products
Remove items from the stock database permanently.

Data Persistence
Automatically saves and loads data using store.dat (JSON format).

User-Friendly CLI
Fully interactive command-line interface.



---

**📂 Project Structure.**

Product-Stock-CRUD-Manager/
│
├── store.dat   # Data file (auto-created)
├── main.py     # Main program
└── README.md   # Documentation


---

**🛠️ Technologies Used.**

Python 3

JSON for data storage

OS module for file handling



---

**📌 How It Works**

The program stores every product as a dictionary with:

{
  "id": 1,
  "name": "Sample Product",
  "cost": 100.0,
  "qty": 5
}

The system auto-generates unique IDs to prevent duplication.


---

**▶️ How to Run**

1. Make sure Python 3 is installed.


2. Download or clone this project:

git clone https://github.com/yourusername/Product-Stock-CRUD-Manager.git


3. Navigate into the folder:

cd Product-Stock-CRUD-Manager


4. Run the script:

python main.py




---

**📸 Program Demo (Menu)**

===== Product Stock CRUD Manager =====

1. Add
2. List
3. Update
4. Remove
5. Exit
Enter your choice:


---

**🧩 Use Cases**

Small shop stock management

College Python project

Intro to CRUD operations

Learning file handling and JSON



---
