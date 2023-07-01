import tkinter as tk
from tkinter import messagebox


class ZestyZomatoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Zesty Zomato")
        self.menu_frame = tk.Frame(root)
        self.menu_frame.pack(padx=20, pady=20)

        self.dish_id_label = tk.Label(self.menu_frame, text="Dish ID:")
        self.dish_id_label.grid(row=0, column=0)
        self.dish_id_entry = tk.Entry(self.menu_frame)
        self.dish_id_entry.grid(row=0, column=1)

        self.name_label = tk.Label(self.menu_frame, text="Dish Name:")
        self.name_label.grid(row=1, column=0)
        self.name_entry = tk.Entry(self.menu_frame)
        self.name_entry.grid(row=1, column=1)

        self.price_label = tk.Label(self.menu_frame, text="Price:")
        self.price_label.grid(row=2, column=0)
        self.price_entry = tk.Entry(self.menu_frame)
        self.price_entry.grid(row=2, column=1)

        self.availability_label = tk.Label(
            self.menu_frame, text="Availability:")
        self.availability_label.grid(row=3, column=0)
        self.availability_entry = tk.Entry(self.menu_frame)
        self.availability_entry.grid(row=3, column=1)

        self.add_dish_button = tk.Button(
            self.menu_frame, text="Add Dish", command=self.add_dish)
        self.add_dish_button.grid(row=4, columnspan=2, pady=10)

        self.buy_frame = tk.Frame(root)
        self.buy_frame.pack(padx=20, pady=20)

        self.customer_name_label = tk.Label(
            self.buy_frame, text="Customer Name:")
        self.customer_name_label.grid(row=0, column=0)
        self.customer_name_entry = tk.Entry(self.buy_frame)
        self.customer_name_entry.grid(row=0, column=1)

        self.order_label = tk.Label(self.buy_frame, text="Order (Dish IDs):")
        self.order_label.grid(row=1, column=0)
        self.order_entry = tk.Entry(self.buy_frame)
        self.order_entry.grid(row=1, column=1)

        self.buy_button = tk.Button(
            self.buy_frame, text="Buy", command=self.buy_dishes)
        self.buy_button.grid(row=2, columnspan=2, pady=10)

        self.review_frame = tk.Frame(root)
        self.review_frame.pack(padx=20, pady=20)

        self.review_button = tk.Button(
            self.review_frame, text="Review Orders", command=self.review_orders)
        self.review_button.pack(pady=10)

        self.order_id_label = tk.Label(self.review_frame, text="Order ID:")
        self.order_id_label.pack()
        self.order_id_entry = tk.Entry(self.review_frame)
        self.order_id_entry.pack()

        self.status_label = tk.Label(self.review_frame, text="Status:")
        self.status_label.pack()
        self.status_entry = tk.Entry(self.review_frame)
        self.status_entry.pack()

        self.update_status_button = tk.Button(
            self.review_frame, text="Update Status", command=self.update_status)
        self.update_status_button.pack(pady=10)

    def add_dish(self):
        dish_id = self.dish_id_entry.get()
        name = self.name_entry.get()
        price = self.price_entry.get()
        availability = self.availability_entry.get()

        # Perform validation and add the dish to the menu
        # ...

        messagebox.showinfo("Success", "Dish added to the menu.")

    def buy_dishes(self):
        customer_name = self.customer_name_entry.get()
        order = self.order_entry.get()

        # Perform validation and process the order
        # ...

        messagebox.showinfo("Success", "Order placed successfully.")

    def review_orders(self):
        # Retrieve and display all orders
        # ...

        messagebox.showinfo("Orders", "Display all orders here.")

    def update_status(self):
        order_id = self.order_id_entry.get()
        status = self.status_entry.get()

        # Perform validation and update the order status
        # ...

        messagebox.showinfo("Success", "Order status updated.")


root = tk.Tk()
app = ZestyZomatoApp(root)
root.mainloop()


class Dish:
    def __init__(self, dish_id, name, price, availability):
        self.dish_id = dish_id
        self.name = name
        self.price = price
        self.availability = availability


class Order:
    def __init__(self, order_id, customer_name, dish_ids):
        self.order_id = order_id
        self.customer_name = customer_name
        self.dish_ids = dish_ids
        self.status = "received"


class ZestyZomato:
    def __init__(self):
        self.menu = {}
        self.orders = {}
        self.next_order_id = 1

    def add_dish(self, dish):
        self.menu[dish.dish_id] = dish

    def remove_dish(self, dish_id):
        if dish_id in self.menu:
            del self.menu[dish_id]

    def update_dish_availability(self, dish_id, availability):
        if dish_id in self.menu:
            self.menu[dish_id].availability = availability

    def take_order(self, customer_name, dish_ids):
        available_dish_ids = [
            dish.dish_id for dish in self.menu.values() if dish.availability == "yes"]
        for dish_id in dish_ids:
            if dish_id not in available_dish_ids:
                print(f"Dish with ID {dish_id} is not available.")
                return

        order = Order(self.next_order_id, customer_name, dish_ids)
        self.orders[self.next_order_id] = order
        self.next_order_id += 1
        print(f"Order placed successfully. Order ID: {order.order_id}")

    def update_order_status(self, order_id, new_status):
        if order_id in self.orders:
            self.orders[order_id].status = new_status
        else:
            print("Order not found.")

    def review_orders(self):
        if self.orders:
            for order in self.orders.values():
                print(
                    f"Order ID: {order.order_id}, Customer Name: {order.customer_name}, Status: {order.status}")
        else:
            print("No orders to review.")


def display_menu():
    print("1. Add a dish to the menu")
    print("2. Remove a dish from the menu")
    print("3. Update the availability of a dish")
    print("4. Take a new order")
    print("5. Update order status")
    print("6. Review orders")
    print("7. Exit")


def get_dish_details():
    dish_id = input("Enter dish ID: ")
    name = input("Enter dish name: ")
    price = float(input("Enter dish price: "))
    availability = input("Is the dish available? (yes/no): ")
    return Dish(dish_id, name, price, availability)


def main():
    zesty_zomato = ZestyZomato()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            dish = get_dish_details()
            zesty_zomato.add_dish(dish)
            print("Dish added to the menu.")
        elif choice == "2":
            dish_id = input("Enter dish ID to remove: ")
            zesty_zomato.remove_dish(dish_id)
            print("Dish removed from the menu.")
        elif choice == "3":
            dish_id = input("Enter dish ID to update availability: ")
            availability = input("Enter new availability (yes/no): ")
            zesty_zomato.update_dish_availability(dish_id, availability)
            print("Dish availability updated.")
        elif choice == "4":
            customer_name = input("Enter customer name: ")
            dish_ids = input("Enter dish IDs (comma-separated): ").split(",")
            zesty_zomato.take_order(customer_name, dish_ids)
        elif choice == "5":
            order_id = int(input("Enter order ID to update status: "))
            new_status = input("Enter new status: ")
            zesty_zomato.update_order_status(order_id, new_status)
            print("Order status updated.")
        elif choice == "6":
            zesty_zomato.review_orders()
        elif choice == "7":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
