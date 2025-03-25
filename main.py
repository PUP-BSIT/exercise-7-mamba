def get_orders(): # TODO BUENACIFRA
    orders = []

    while True:
        product_name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        total = price * quantity

        orders.append({
            "Product Name": product_name,
            "Price": price,
            "Quantity": quantity,
            "Total": total
        })

        add_order = input("Add another order? (y/n): ").lower()
        if add_order != "y":
            break
    return orders

def get_customer_name_and_senior_id(): # TODO ROLDAN
    customer_name = input("Enter customer name: ")
    if_senior = input("Is the customer a senior citizen? (y if yes Leave blank if not senior citizen) ").lower()
    senior_id = ""
    if if_senior == "y":
        senior_id = input("Enter senior id")
    return customer_name, if_senior, senior_id

def get_grand_total(orders, if_senior): # TODO BERNAS
    grand_total = sum(order["Total"] for order in orders)
    if if_senior == "y":
        discount = grand_total * 0.10
        grand_total -= discount
    return grand_total

def display_orders_customer_name_senior_id_grand_total(): # TODO TERO
    orders = get_orders()
    customer_name, if_senior, senior_id = get_customer_name_and_senior_id()
    grand_total = get_grand_total(orders, if_senior)
    
    print("\nItems:")
    for order in orders:
        print(f"Product Name: {order['Product Name']}, Price: {order['Price']}, Quantity: {order['Quantity']}, Total: {order['Total']}")
    print("\nCustomer Name:", customer_name)
    if if_senior == "y":
        print("Senior id no.:", senior_id)
    print("Grand total:", grand_total)

def main():
    display_orders_customer_name_senior_id_grand_total()

main()
