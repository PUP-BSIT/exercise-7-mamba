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
    customer_name = input("Enter customer name: ")
    senior = input("Is the customer a senior citizen? (y if yes, Leave blank if not senior citizen)").lower() #Exceeds 80 columns, Spacing, add ":", remove senior variable
    senior_id = "" 
    if senior == "y": #change condition, system won't ask if the user is senior.
        senior_id = input("Enter senior id") #Add spacing and ":"
    return customer_name, senior, senior_id #remove senior variable.

def get_grand_total(orders, senior_id): # TODO BERNAS
    grand_total = sum(order["Total"] for order in orders)
    if senior_id:
        discount = grand_total * 0.10
        grand_total -= discount
        return grand_total
    return grand_total

def display_orders_customer_name_senior_id_grand_total(): # TODO TERO
    orders = get_orders()
    customer_name, senior, senior_id = get_customer_name_and_senior_id() #remove senior variable.
    grand_total = get_grand_total(orders, senior) #remove senior variable.
    
    print("\nItems:")
    for order in orders:
        print(f"Product Name: {order['Product Name']}, Price: {order['Price']}, Quantity: {order['Quantity']}, Total: {order['Total']}") #Exceeds 80 columns, add spacings dont make it in one line.
    print("\nCustomer Name:", customer_name)
    if senior == "y": #change condition, system won't ask if the user is senior.
        print("Senior id no.:", senior_id)
    print("Grand total:", grand_total)

def main():
    display_orders_customer_name_senior_id_grand_total()

main()
