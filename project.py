import json
import os

file_name = "store.dat"

def load_data():
    if not os.path.exists(file_name):
        return []
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except:
        return []

def save_data(items):
    try:
        with open(file_name, "w") as f:
            json.dump(items, f)
        print("Saved.")
    except:
        print("Could not save.")

def get_new_id(items):
    if not items:
        return 1
    nums = [x["id"] for x in items]
    return max(nums) + 1

def add_item(items):
    name = input("Enter product name: ")
    try:
        cost = float(input("Enter cost: "))
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Wrong input. Cost must be a number and quantity must be an integer.")
        return
    pid = get_new_id(items)
    items.append({"id": pid, "name": name, "cost": cost, "qty": qty})
    save_data(items)
    print("Item added.")

def show_items(items):
    if not items:
        print("No items found.")
        return
    print("\nID | Name | Cost | Qty")
    print("-----------------------")
    for it in sorted(items, key=lambda x: x["id"]):
        print(f"{it['id']} | {it['name']} | {it['cost']} | {it['qty']}")

def update_item(items):
    try:
        pid = int(input("Enter id to update: "))
        new_qty = int(input("Enter new quantity: "))
    except ValueError:
        print("Wrong input. ID and quantity must be integers.")
        return
    for it in items:
        if it["id"] == pid:
            it["qty"] = new_qty
            save_data(items)
            print("Updated.")
            return
    print("ID not found.")

def remove_item(items):
    try:
        pid = int(input("Enter id to remove: "))
    except ValueError:
        print("Wrong input. ID must be an integer.")
        return
    for i, it in enumerate(items):
        if it["id"] == pid:
            items.pop(i)
            save_data(items)
            print("Removed.")
            return
    print("ID not found.")

def main():
    print("\n===== Product Stock CRUD Manager =====\n")

    items = load_data()
    while True:
        print("\n1. Add")
        print("2. List")
        print("3. Update")
        print("4. Remove")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_item(items)
        elif choice == "2":
            show_items(items)
        elif choice == "3":
            update_item(items)
        elif choice == "4":
            remove_item(items)
        elif choice == "5":
            print("Exiting.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()