# operations.py
from datetime import datetime
#display products function
def display_products(d):
    print("\n" + "-" * 90)
    print("ID   | Product Name         | Brand          | Qty   | Price      | Origin")
    print("-" * 90)
    #calculating the selling price
    for pid, product in d.items():
        selling_price = product['cost_price'] * 2
        #product details formated in columns
        print("%-5d| %-20s| %-15s| %-5d | %-10.2f | %-15s" % (
            pid, product['name'], product['brand'], product['quantity'], selling_price, product['origin']
        ))
    print("-" * 90 + "\n")
# displaying sales bills
def display_sales_bill(customer_name, phone, items, total, products):
    print("\n" + "=" * 50)
    print("\t\tBILL RECEIPT")
    print("=" * 50)
    #displaying customer details
    print("Customer: " + customer_name)
    print("Phone: " + phone)
    print("Date:", datetime.now())
    print("-" * 50)
    print("ITEM                     QTY   PRICE     SUB-TOTAL")
    print("-" * 50)
    for name, qty, free in items:
        product = next(p for p in products.values() if p['name'] == name)
        price = product['cost_price'] * 2
        print("%-25s %5s %8.2f %10.2f" % (
            name, str(qty) + "(+" + str(free) + ")", price, price * qty
        ))
    print("-" * 50)
    print("TOTAL:".rjust(48) + " %.2f" % total)
    print("=" * 50 + "\n")

# restocking bill
def display_restock_bill(vendor_name, items, total, products):
    print("\n" + "=" * 50)
    print("\t\tRESTOCKING BILL")
    print("=" * 50)
    print("Vendor:", vendor_name)
    print("Date:", datetime.now())
    print("-" * 50)
    print("ITEM                     QTY      COST     SUB-TOTAL")
    print("-" * 50)
    for name, qty, cost in items:
        print("%-25s %8d %10.2f %10.2f" % (name, qty, cost, qty * cost))
    print("-" * 50)
    print("TOTAL:".rjust(48) + " %.2f" % total)
    print("=" * 50 + "\n")
