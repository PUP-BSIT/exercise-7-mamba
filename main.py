def get_orders(): # TODO BUENACIFRA 
    orders = []

    while True:
        product_name = input("Enter product name: ") #add "\n" for readability and spacings.
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        total = price * quantity

        orders.append({
            "Product Name": product_name,
            "Price": price,
            "Quantity": quantity,
            "Total": total
        })

        add_order = input("Add another order? (y/n): ").lower() #Add spacings "\n"
        if add_order != "y":
            break
    return orders

def get_customer_name_and_senior_id(): # TODO ROLDAN
    customer_name = input("\nEnter Customer Name: ")
    senior_id = input("Enter Senior ID: ? "
    "(Leave blank if not senior citizen)").lower() 
    return customer_name, senior_id

def get_grand_total(orders, senior_id): # TODO BERNAS
    grand_total = sum(order["Total"] for order in orders)
    if senior_id:
        discount = grand_total * 0.10
        grand_total -= discount
        return grand_total
    return grand_total

def display_orders_customer_name_senior_id_grand_total(): # TODO TERO
    orders = get_orders()
    customer_name, senior_id = get_customer_name_and_senior_id() #remove senior variable.
    grand_total = get_grand_total(orders, senior_id) #remove senior variable.
    
    print("\nItems:")
    for order in orders:
        print(f"Product Name: {order['Product Name']}")
        print(f"Price: {order['Price']}")
        print(f"Quantity: {order['Quantity']}")
        print(f"Total: {order['Total']}")
    print("\nCustomer Name:", customer_name)
    print("Senior ID No:", senior_id)
    print("Grand total:", grand_total)

def main():
    display_orders_customer_name_senior_id_grand_total()

main()
