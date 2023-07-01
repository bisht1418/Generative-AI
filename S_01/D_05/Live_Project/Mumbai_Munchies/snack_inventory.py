class Snack:
    def __init__(self, id, name, price, availability, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.availability = availability
        self.quantity = quantity


class SnackInventory:
    def __init__(self):
        self.snacks = []

    def add_snack(self, snack):
        self.snacks.append(snack)

    def remove_snack(self, snack_id):
        for snack in self.snacks:
            if snack.id == snack_id:
                self.snacks.remove(snack)
                break

    def update_availability(self, snack_id, availability):
        for snack in self.snacks:
            if snack.id == snack_id:
                snack.availability = availability
                break

    def sell_snack(self, snack_id):
        for snack in self.snacks:
            if snack.id == snack_id:
                if snack.availability == "yes":
                    snack.quantity -= 1
                    return True
                else:
                    print("Snack is not available for sale.")
                    return False
        print("Snack not found.")
        return False

    def get_all_snacks(self):
        return self.snacks


def display_menu():
    print("1. Add a snack to the inventory")
    print("2. Remove a snack from the inventory")
    print("3. Update the availability of a snack")
    print("4. Sell a snack")
    print("5. List all snacks")
    print("6. Exit")


def get_snack_details():
    snack_id = input("Enter snack ID: ")
    name = input("Enter snack name: ")
    price = float(input("Enter snack price: "))
    availability = input("Is the snack available? (yes/no): ")
    quantity = int(input("Enter snack quantity: "))
    return Snack(snack_id, name, price, availability, quantity)


def add_snack_to_inventory(inventory):
    snack = get_snack_details()
    inventory.add_snack(snack)
    print("Snack added to the inventory.")


def remove_snack_from_inventory(inventory):
    snack_id = input("Enter snack ID to remove: ")
    inventory.remove_snack(snack_id)
    print("Snack removed from the inventory.")


def update_snack_availability(inventory):
    snack_id = input("Enter snack ID to update availability: ")
    availability = input("Is the snack available now? (yes/no): ")
    inventory.update_availability(snack_id, availability)
    print("Snack availability updated.")


def sell_snack(inventory):
    snack_id = input("Enter snack ID to sell: ")
    if inventory.sell_snack(snack_id):
        print("Snack sold. Inventory updated.")
    else:
        print("Snack sale unsuccessful.")


def list_all_snacks(inventory):
    all_snacks = inventory.get_all_snacks()
    if all_snacks:
        print("List of snacks:")
        for snack in all_snacks:
            print(
                f"ID: {snack.id}, Name: {snack.name}, Quantity: {snack.quantity}")
    else:
        print("No snacks in the inventory.")


def main():
    inventory = SnackInventory()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            add_snack_to_inventory(inventory)
        elif choice == "2":
            remove_snack_from_inventory(inventory)
        elif choice == "3":
            update_snack_availability(inventory)
        elif choice == "4":
            sell_snack(inventory)
        elif choice == "5":
            list_all_snacks(inventory)
        elif choice == "6":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
