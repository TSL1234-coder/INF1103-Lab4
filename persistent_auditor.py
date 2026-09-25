import os


#Global Constants
MAX_CAPACITY = 500
TAX_RATE = 0.1
INVENTORY_FILE = "inventory.txt"


# Inventory item structure
ITEM_FIELDS = {
    "id": 0,
    "name": 1,
    "quantity": 2,
    "transactions_history": 3
}


item1 = [
    "1001",
    "Mouse",
    4, [5, 12, 6]
]

item2=[
    "1002",
    "USB Drive",
    5, [4, 5, 10]
]

item3=[
    "1003",
    "Charger",
    3, [6, 5, 7]
]




# ==============================
# Functions
# ==============================
def load_inventory(new_items):
    if os.path.exists("inventory.txt"):
        inventory_from_file = open("inventory.txt", "r").read() # contents being stored as a string from file
        parsed_inventory_list = eval(f"[{inventory_from_file}]") # to convert the string into a list 

        item_list = []
        transcations_history = []

        for item in parsed_inventory_list:
            item_list.append([
                item[ITEM_FIELDS["id"]],
                item[ITEM_FIELDS["name"]],
                item[ITEM_FIELDS["quantity"]],
            ])

            transcations_history.append(item[ITEM_FIELDS["transactions_history"]])

        output_orders = ""

        for order in item_list:
            output_orders += order[ITEM_FIELDS["name"]] + " " + str(order[ITEM_FIELDS["quantity"]]) + "\n"

        print("Current Orders:\n" + output_orders)

        return inventory_from_file, transcations_history
    else:

        with open("inventory.txt", "w") as f:
            new_item_string=','.join([str(item) for item in new_items])
            f.write(new_item_string)


        print("No inventory file found. A new file has been created.")

        return new_items
        
        

    


def save_inventory(inventory, transactions_history):
    return 0;


def get_valid_input():
    failed_attempts = 0

    while True:
        product_name_input = input(
            "Enter Product Name (or type 'quit' to exit): "
        )

        if product_name_input.lower() == "quit":
            return "quit", 0, failed_attempts

        quantity_input = input("Enter Quantity: ")

        if quantity_input.lower() == "quit":
            return "quit", 0, failed_attempts

        if not quantity_input.isdigit() or int(quantity_input) < 0:
            print("Error! Please enter a valid integer.")
            failed_attempts += 1
        else:
            return product_name_input, int(quantity_input), failed_attempts
        

def process_delivery(current_total, new_value):
    new_total = current_total + new_value
    return new_total


def calculate_tax(amount):
    tax_amount = amount * 0.1
    return tax_amount


def generate_report(total_units, failed_attempts):
    print("\nInventory Report:")
    print("===================")
    print(f"Total Deliveries Processed: {total_units}")
    print(f"Total Rejected Entries: {failed_attempts}")


# ===========================
# Main Program
# ===========================
def main():

    inventory = 0
    tax_amount = 0
    failed_attempts = 0
    item_list = [item1, item2, item3]

    load_inventory(item_list)

    while True:
        product_name_input, new_value, rejected = get_valid_input()

        failed_attempts += rejected

        if product_name_input == "quit":
            generate_report(inventory, failed_attempts)
            break

        # Generate the next product ID
        if len(item_list) == 0:
            new_id = "1001"
        else:
            last_id = int(item_list[-1][ITEM_FIELDS["id"]])
            new_id = str(last_id + 1)


        # Create new item
        new_item = [
            new_id,
            product_name_input,
            new_value,
            [new_value]
        ]

        item_list.append(new_item)

        print(f"Added item: {new_id} - {product_name_input} - Quantity: {new_value}\n")
        print(item_list)

        inventory = process_delivery(inventory, new_value)

        tax_amount = calculate_tax(new_value)


if __name__ == "__main__":
    main()