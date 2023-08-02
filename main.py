import products
import store

def list_products(stock):
    """
    Lists available products
    """
    print("------")
    for num, item in enumerate(stock.get_all_products(), 1):
        print('. '.join([str(num), item]))
    print("------\n")


def total_products(stock):
    """
    Lists total stock for the entire store
    """
    print(f"\nTotal of {stock.get_total_quantity()} items in store\n")


def order_products(stock):
    """
    Orders products that are in stock
    """
    list_products(stock)

    stock_list = [(num, item)
        for num, item in enumerate(stock.get_all_products(), 1)]

    order_list = []

    print("When you want to finish order, enter empty text.")
    while True:
        try:
            product_num = int(input("Which product # do you want? "))
            product_amt = int(input("What amount do you want? "))
        except ValueError:
            if order_list:
                print("******")
                print(f"Order made! Total payment: ${sum(order_list)}\n")
            return
        if product_num not in list(zip(*stock_list))[0]:
            print("Error adding product!")
        elif product_amt > 2:
            print("Limited quantity of 2 per customer!")
        else:
            order_item = stock.order([(product_list[product_num-1], product_amt)])
            order_list.append(order_item)
            print("Product added to list!\n")


def start(stock):
    """
    Menu functionality
    """
    menu = ("1. List all products in the store\n"
            "2. Show total amount in store\n"
            "3. Make an order\n"
            "4. Quit"
        )

    opt_list = {
        1: "list_products",
        2: "total_products",
        3: "order_products"
    }

    while True:
        print("   Store Menu\n"
              "   ----------")

        print(menu)
        opt = int(input("Please choose a number: "))

        if opt in opt_list:
            globals()[opt_list[opt]](stock)
        elif opt == 4:
            break


"""
Setup default inventory, initiate the store and the menu
"""
product_list = [
    products.Product("MacBook Air M2", price=1450, quantity=100),
    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
    products.Product("Google Pixel 7", price=500, quantity=250)
    ]
best_buy = store.Store(product_list)

start(best_buy)
