# main.py
from read import load_products
from write import generate_sales_invoice, generate_restock_invoice, update_product_file
from operations import display_products, display_sales_bill, display_restock_bill
#main function to run the system
def main():
    print("\n\n\t\t\t\t\tWeCare Wholesale")
    print("-" * 150)
    print("\t\t\tKamalpokhari, Kathmandu, Nepal | Phone No: 9863472312")
    print("-" * 150)
    print("\n\t\t\tWelcome to the system Admin! Hope you are doing great!\n")
    print("-" * 150)

    products = load_products()#loading products from the file
    if not products:
        print("No products choosen. Please check products.txt file.")
        return

    while True:
        print("\nOptions:")
        print("-" * 50)
        print("1. Selling products to customer")
        print("2. Restocking products from supplier")
        print("3. Exit system")
        print("-" * 50)

        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a valid number")
            continue

        if option == 1:#option1
            while True:
                customer_name = input("Enter the customer's Name: ")
                if customer_name.replace(" ", "").isalpha():
                    break
                else:
                    print("Invalid name! Please enter letters only.")
            customer_phone = input("Enter the customer's Phone Number: ")
            
            sold_items = []
            total_amount = 0

            while True:#loop used to sell multiple products
                display_products(products)
                try:
                    product_id = int(input("Enter the product ID to sell (0 to finish): "))
                except ValueError:
                    print("Invalid input. Please enter a valid number")
                    continue

                if product_id == 0:
                    break
                if product_id not in products:
                    print("Invalid product ID!")
                    continue

                product = products[product_id]
                try:
                    quantity = int(input("Enter the quantity for " + product['name'] + ": "))
                except ValueError:
                    print("Invalid quantity!")
                    continue

                free_items = quantity // 3
                total_deduct = quantity + free_items

                if quantity <= 0 or total_deduct > product['quantity']:
                    print("Not enough stock! (Available: %d)" % product['quantity'])
                    continue

                selling_price = product['cost_price'] * 2
                total_amount += selling_price * quantity
                sold_items.append((product['name'], quantity, free_items))
                products[product_id]['quantity'] -= total_deduct

            if sold_items:
                display_sales_bill(customer_name, customer_phone, sold_items, total_amount, products)
                generate_sales_invoice(customer_name, customer_phone, sold_items, total_amount)
                update_product_file(products)

        elif option == 2:#option2
            vendor_name = input("Enter the supplier's Name: ")
            restock_items = []
            restock_total = 0

            while True:
                display_products(products)
                try:
                    product_id = int(input("Enter the product ID to restock (0 to finish): "))
                except ValueError:
                    print("Invalid input!!")
                    continue

                if product_id == 0:
                    break
                if product_id not in products:
                    print("Invalid product ID")
                    continue

                try:
                    quantity = int(input("Enter the quantity for " + products[product_id]['name'] + ": "))
                    cost_price = float(input("Enter the cost price: "))
                except ValueError:
                    print("Invalid input!!")
                    continue

                total_cost = cost_price * quantity
                restock_items.append((products[product_id]['name'], quantity, cost_price))
                restock_total += total_cost
                products[product_id]['quantity'] += quantity
                products[product_id]['cost_price'] = cost_price

            if restock_items:#displaying and saving restock invoice
                display_restock_bill(vendor_name, restock_items, restock_total, products)
                generate_restock_invoice(vendor_name, restock_items, restock_total)
                update_product_file(products)

        elif option == 3:# option 3
            print("Exiting system...")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
