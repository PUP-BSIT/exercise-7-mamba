def get_orders(): # TODO BUENACIFRA
    orders = []

    while True:
        product_name = input("Enter product name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        total = price * quantity

        orders.append({
            "Product Name: ": product_name,
            "Price: ": price,
            "Quantity: ": quantity,
            "Total: ": total
        })

        add_order = input("Add another order? (y/n): ").lower()
        if add_order != "y":
            break
    return orders

def get_customer_name_and_senior_id(): # TODO ROLDAN
    customer_name = input("Enter customer name: ")
    if_senior = input("Is the customer a senior citizen? (y/n): ").lower()
    return customer_name, if_senior

def get_grand_total(): # TODO BERNAS
    grand_total = sum(order["Total"] for order in get_orders)
    if if_senior == "y":
        senior_id = input("Senior Citizen ID: ")
    grand_total /= 10

def display_orders_customer_name_senior_id_grand_total(): # TODO TERO