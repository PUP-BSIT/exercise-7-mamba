def get_orders(): # TODO BUENACIFRA

def get_customer_name_and_senior_id(): # TODO ROLDAN

def get_grand_total(): # TODO BERNAS
    grand_total = sum(order["Total"] for order in get_orders)
    if if_senior == "y":
        senior_id = input("Senior Citizen ID: ")
    grand_total /= 10

def display_orders_customer_name_senior_id_grand_total(): # TODO TERO