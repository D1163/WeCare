# write.py
from datetime import datetime
#generate and save invoices
def generate_sales_invoice(customer_name, customer_phone, sold_items, total_amount):
    now = datetime.now()
    invoice_filename = "sales_invoice_%d%d%d_%d%d%d.txt" % (now.year, now.month, now.day, now.hour, now.minute, now.second)
    with open(invoice_filename, "w") as f:
        f.write("Customer Name: " + customer_name + "\n")
        f.write("Phone Number: " + customer_phone + "\n")
        f.write("Date of Transaction: " + str(now) + "\n")
        f.write("Products Purchased:\n")
        f.write("-" * 40 + "\n")
        for item in sold_items:
            f.write(item[0] + " - " + str(item[1]) + " pcs (Paid for " + str(item[1] - item[2]) + " items)\n")
        f.write("\nTotal Amount (excluding free items): %.2f\n" % total_amount)
    print("Invoice generated:", invoice_filename)#declaring that the invoice is saved

def generate_restock_invoice(vendor_name, restock_items, total_amount):
    now = datetime.now()
    invoice_filename = "restock_invoice_%d%d%d_%d%d%d.txt" % (now.year, now.month, now.day, now.hour, now.minute, now.second)
    with open(invoice_filename, "w") as f:
        f.write("Vendor: " + vendor_name + "\n")
        f.write("Date of Transaction: " + str(now) + "\n")
        f.write("Products Restocked:\n")
        for item in restock_items:
            f.write("%s - %d pcs at %.2f cost each\n" % (item[0], item[1], item[2]))
        f.write("\nTotal Restocking Amount: %.2f\n" % total_amount)
    print("Restock invoice generated:", invoice_filename)

def update_product_file(d):
    with open("products.txt", "w") as file:
        for pid, product in d.items():
            file.write("%s,%s,%d,%.2f,%s\n" % (
                product['name'], product['brand'], product['quantity'],
                product['cost_price'], product['origin']
            ))
