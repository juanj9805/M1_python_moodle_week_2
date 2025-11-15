# MY VERSION

import time

products = []

def add_product():
    product_name = input("Enter the product name: ")
    product_quantity = int(input("Enter the product quantity: "))
    product_price = int(input("Enter the product price: "))
    new_product = {
        "ID" : time.time(),
        "product_name" : product_name,
        "product_quantity" : product_quantity,
        "product_price" : product_price,
    }
    products.append(new_product)

def show_product():
    ask_show = int(input(
        "Choose one option: \n"
        "1- Print the whole list: \n"
        "2- Print each product: \n"
    ))
    if ask_show == 1:
        print(products)
    elif ask_show == 2:
        for product in products:
            print(product)
    else: 
        print("Something went wrong")

def show_statistics():
    total_price_inventory = 0
    for product in products:
        total_price_inventory += product["product_price"] * product["product_quantity"]
    print(total_price_inventory)
    print(len(products))

# def continue_in():
#     follow = True
#     ask_continue = input("Do you want to continue: ")
#     while follow:
#         if ask_continue == "s":
#             inventory_actions()
#         elif ask_continue == "n":
#             follow = False
#         else:
#             print("Something went wrong")

def inventory_actions():
    follow = True
    while follow:
        ask_user = int(input(
            "Choose one option:\n"
            "1- Add a prodcut\n"
            "2- Show inventory\n"
            "3- Calculate data\n"
            "4- Do you want to continue: s/n\n"
        ))
        if ask_user != "":
            if ask_user == 1:
                add_product()
            elif ask_user == 2:
                show_product()
            elif ask_user == 3:
                show_statistics()
            elif ask_user == 4:
                follow = False
            else:
                print("Something went wrong")

inventory_actions()

# CHATGPT VERSION

import uuid

products = []

def input_number(prompt):
    while True:
        try:
            return float(input(f"{prompt}: "))
        except ValueError:
            print("❌ Please enter a valid number.")

def add_product():
    name = input("Enter the product name: ").strip()
    quantity = int(input_number("Enter the product quantity"))
    price = float(input_number("Enter the product price"))

    new_product = {
        "ID": str(uuid.uuid4()),
        "name": name,
        "quantity": quantity,
        "price": price,
    }

    products.append(new_product)
    print("✔ Product added successfully!")

def show_products():
    print("\n---- INVENTORY ----")
    if not products:
        print("No products available.")
        return

    for product in products:
        print(f"ID: {product['ID']}")
        print(f"Name: {product['name']}")
        print(f"Quantity: {product['quantity']}")
        print(f"Price: {product['price']}")
        print("--------------------")

def show_statistics():
    total_value = sum(p["price"] * p["quantity"] for p in products)
    print("\nINVENTORY STATISTICS")
    print(f"Total value: ${total_value}")
    print(f"Total products: {len(products)}")

def inventory_actions():
    while True:
        print("\nChoose an option:")
        print("1- Add a product")
        print("2- Show inventory")
        print("3- Show statistics")
        print("4- Exit")

        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("❌ Invalid option. Please enter a number.")
            continue

        if option == 1:
            add_product()
        elif option == 2:
            show_products()
        elif option == 3:
            show_statistics()
        elif option == 4:
            print("Goodbye!")
            break
        else:
            print("❌ Invalid option. Try again.")

# inventory_actions()

# SUMMARY OF IMPROVEMENTS

# | **Problem**                                               | **Fix**                                       | **Why**                                                                   |
# | --------------------------------------------------------- | --------------------------------------------- | ------------------------------------------------------------------------- |
# | Using a **global `products` list**                        | Pass `products` as a parameter or use a class | Global variables cause bugs, make testing harder, and reduce code clarity |
# | No **input validation** for numbers → program can crash   | Wrap inputs with `try/except` or use a helper | Prevents `ValueError` when user types letters                             |
# | ID created using `time.time()`                            | Use `uuid.uuid4()`                            | Time IDs can repeat; UUIDs are unique and safer                           |
# | Misspelling: “Add a prodcut”                              | Fix to “Add a product”                        | Makes the program more professional and clear                             |
# | `show_products()` prints raw dict list                    | Loop and format output nicely                 | Raw dicts look ugly and unprofessional to the user                        |
# | Menu option “4- Do you want to continue” is confusing     | Change to “Exit”                              | UX must be intuitive; unclear labels cause confusion                      |
# | `continue_in()` function is **never used**                | Remove it or integrate properly               | Dead code creates confusion and reduces quality                           |
# | No loop when user enters invalid menu option              | Add validation and re-prompt                  | Prevents program from breaking or behaving incorrectly                    |
# | No ability to edit or delete products                     | Add option for update/remove                  | Real inventory systems need modification options                          |
# | Repeating code for printing menus                         | Create a helper function                      | Reduces duplication and makes code cleaner                                |
# | Variables like `ask_user` or `ask_show` use generic names | Use descriptive names like `choice`           | Improves readability and maintainability                                  |
# | `if ask_user != ""` is pointless                          | Remove it                                     | `ask_user` is always an integer, so this check does nothing               |
# | No feedback after adding a product                        | Print confirmation ("Product added!")         | Better user experience                                                    |
# | Statistics print raw numbers                              | Format output with labels                     | Makes the output more readable and professional                           |
# | No error handling for invalid menu input                  | Use `try/except ValueError`                   | Prevents program from crashing and improves robus                         |

