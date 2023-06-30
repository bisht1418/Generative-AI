class Snack:
    def __init__(self, snack_id, name, price, availability):
        self.snack_id = snack_id
        self.name = name
        self.price = price
        self.availability = availability


class SnackInventory:
    def __init__(self):
        self.inventory = []

    def add_snack(self, snack):
        self.inventory.append(snack)

    def remove_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                self.inventory.remove(snack)
                break

    def update_availability(self, snack_id, availability):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                snack.availability = availability
                break

    def sell_snack(self, snack_id):
        for snack in self.inventory:
            if snack.snack_id == snack_id:
                if snack.availability == "yes":
                    snack.availability = "no"
                    return True
                else:
                    print("Snack is not available.")
                    return False
        print("Snack not found.")
        return False


def display_menu():
    print("1. Add snack")
    print("2. Remove snack")
    print("3. Update snack availability")
    print("4. Sell snack")
    print("5. Exit")


def get_snack_details():
    snack_id = input("Enter snack ID: ")
    name = input("Enter snack name: ")
    price = input("Enter snack price: ")
    availability = input("Enter snack availability (yes/no): ")
    return Snack(snack_id, name, price, availability)


def get_snack_id():
    return input("Enter snack ID: ")


def main():
    inventory = SnackInventory()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            snack = get_snack_details()
            inventory.add_snack(snack)
            print("Snack added to inventory.")
        elif choice == "2":
            snack_id = get_snack_id()
            inventory.remove_snack(snack_id)
            print("Snack removed from inventory.")
        elif choice == "3":
            snack_id = get_snack_id()
            availability = input("Enter new availability (yes/no): ")
            inventory.update_availability(snack_id, availability)
            print("Snack availability updated.")
        elif choice == "4":
            snack_id = get_snack_id()
            if inventory.sell_snack(snack_id):
                print("Snack sold.")
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
