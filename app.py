from datetime import datetime

def create_invoice(customer_name, items):
    total = 0
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    with open("Shad_invoice.txt", "w") as f:
        f.write("======== INVOICE ========\n")
        f.write(f"Customer: {customer_name}\n")
        f.write(f"Date: {timestamp}\n\n")
        f.write("Items:\n")
        f.write("-------------------------\n")

        for item in items:
            name = item["name"]
            quantity = item["quantity"]
            price = item["price"]
            subtotal = quantity * price
            total += subtotal
            f.write(f"{name} (x{quantity}) - RM{subtotal:.2f}\n")

        f.write("-------------------------\n")
        f.write(f"Total: RM{total:.2f}\n")
        f.write("=========================\n")

    print("\n✅ Invoice generated and saved as 'Shad_invoice.txt'.")

def get_items_from_user():
    items = []
    while True:
        item_name = input("Enter item name (or type 'done' to finish): ")
        if item_name.lower() == 'done':
            break
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per item (RM): "))
            items.append({"name": item_name, "quantity": quantity, "price": price})
        except ValueError:
            print("❌ Invalid input. Please enter numbers for quantity and price.")
    return items

if __name__ == "__main__":
    print("🧾 Welcome to Invoice Generator 🧾")
    customer = input("Enter customer name: ")
    item_list = get_items_from_user()
    if item_list:
        create_invoice(customer, item_list)
    else:
        print("⚠️ No items entered. Invoice not generated.")
