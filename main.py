def get_orders():
    orders = []

    while True:
        product_name = input("\nEnter Product Name: ")
        price = float(input("Enter Price: "))
        quantity = int(input("Enter Quantity: "))
        total = price * quantity

        orders.append({
            "Product Name": product_name,
            "Price": price,
            "Quantity": quantity,
            "Total": total
        })

        add_order = input("\nAdd another order? (y/n): ").lower()
        if add_order != "y":
            break
    return orders

def get_customer_name_and_senior_id():
    customer_name = input("\nEnter Customer Name: ")
    senior_id = input("Enter Senior ID No. "
    "(Leave blank if not senior citizen): ") 
    return customer_name, senior_id

def get_grand_total(orders, senior_id):
    grand_total = sum(order["Total"] for order in orders)
    if senior_id:
        discount = grand_total * 0.10
        grand_total -= discount
        return grand_total
    return grand_total

def display_orders_customer_name_senior_id_grand_total():
    orders = get_orders()
    customer_name, senior_id = get_customer_name_and_senior_id()
    grand_total = get_grand_total(orders, senior_id)
    
    print("\nItems:")
    for order in orders:
        print(f"\nProduct Name: {order['Product Name']}")
        print(f"Price: {order['Price']}")
        print(f"Quantity: {order['Quantity']}")
        print(f"Total: {order['Total']}")
    print("\nCustomer Name:", customer_name)
    print("Senior ID No.:", senior_id)
    print("Grand Total:", grand_total)

def main():
    display_orders_customer_name_senior_id_grand_total()

main()
