import tkinter as tk
from tkinter import messagebox


class Dish:
    def __init__(self, dish_id, name, price, availability):
        self.dish_id = dish_id
        self.name = name
        self.price = price
        self.availability = availability


class ZestyZomato:
    def __init__(self):
        self.menu = []
        self.orders = []
        self.order_id = 1

    def add_dish(self, dish):
        self.menu.append(dish)

    def remove_dish(self, dish_id):
        for dish in self.menu:
            if dish.dish_id == dish_id:
                self.menu.remove(dish)
                return True
        return False

    def update_availability(self, dish_id, availability):
        for dish in self.menu:
            if dish.dish_id == dish_id:
                dish.availability = availability
                return True
        return False

    def take_order(self, customer_name, dish_ids):
        dishes_ordered = []
        for dish_id in dish_ids:
            for dish in self.menu:
                if dish.dish_id == dish_id:
                    if dish.availability == "yes":
                        dishes_ordered.append(dish)
                    else:
                        messagebox.showinfo(
                            "Error", f"{dish.name} is not available for order.")
                        return
        order = Order(self.order_id, customer_name, dishes_ordered)
        self.orders.append(order)
        self.order_id += 1
        messagebox.showinfo(
            "Success", f"Order taken successfully. Order ID: {order.order_id}")

    def update_status(self, order_id, status):
        for order in self.orders:
            if order.order_id == order_id:
                order.status = status
                messagebox.showinfo(
                    "Success", f"Order status updated. Order ID: {order.order_id}")
                return
        messagebox.showinfo("Error", "Invalid Order ID")


class Order:
    def __init__(self, order_id, customer_name, dishes_ordered):
        self.order_id = order_id
        self.customer_name = customer_name
        self.dishes_ordered = dishes_ordered
        self.status = "received"


class ZestyZomatoGUI:
    def __init__(self):
        self.zesty_zomato = ZestyZomato()

        self.root = tk.Tk()
        self.root.title("Zesty Zomato")

        self.create_menu_frame()
        self.create_orders_frame()
        self.create_buttons()

    def create_menu_frame(self):
        self.menu_frame = tk.LabelFrame(self.root, text="Menu")
        self.menu_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        self.menu_listbox = tk.Listbox(self.menu_frame, width=50)
        self.menu_listbox.pack(padx=10, pady=10)

    def update_menu_listbox(self):
        self.menu_listbox.delete(0, tk.END)
        for dish in self.zesty_zomato.menu:
            self.menu_listbox.insert(
                tk.END, f"{dish.dish_id} - {dish.name} - Rs. {dish.price}")

    def create_orders_frame(self):
        self.orders_frame = tk.LabelFrame(self.root, text="Orders")
        self.orders_frame.pack(padx=10, pady=10, fill=tk.BOTH)

        self.orders_listbox = tk.Listbox(self.orders_frame, width=50)
        self.orders_listbox.pack(padx=10, pady=10)

    def update_orders_listbox(self):
        self.orders_listbox.delete(0, tk.END)
        for order in self.zesty_zomato.orders:
            self.orders_listbox.insert(
                tk.END, f"Order ID: {order.order_id} - Customer: {order.customer_name} - Status: {order.status}")

    def create_buttons(self):
        add_dish_button = tk.Button(
            self.root, text="Add Dish", command=self.open_add_dish_window)
        add_dish_button.pack(pady=10)

        remove_dish_button = tk.Button(
            self.root, text="Remove Dish", command=self.open_remove_dish_window)
        remove_dish_button.pack(pady=10)

        update_availability_button = tk.Button(
            self.root, text="Update Availability", command=self.open_update_availability_window)
        update_availability_button.pack(pady=10)

        take_order_button = tk.Button(
            self.root, text="Take Order", command=self.open_take_order_window)
        take_order_button.pack(pady=10)

        update_status_button = tk.Button(
            self.root, text="Update Status", command=self.open_update_status_window)
        update_status_button.pack(pady=10)

    def open_add_dish_window(self):
        add_dish_window = tk.Toplevel(self.root)
        add_dish_window.title("Add Dish")

        dish_id_label = tk.Label(add_dish_window, text="Dish ID:")
        dish_id_label.grid(row=0, column=0, padx=5, pady=5)
        dish_id_entry = tk.Entry(add_dish_window)
        dish_id_entry.grid(row=0, column=1, padx=5, pady=5)

        dish_name_label = tk.Label(add_dish_window, text="Dish Name:")
        dish_name_label.grid(row=1, column=0, padx=5, pady=5)
        dish_name_entry = tk.Entry(add_dish_window)
        dish_name_entry.grid(row=1, column=1, padx=5, pady=5)

        price_label = tk.Label(add_dish_window, text="Price:")
        price_label.grid(row=2, column=0, padx=5, pady=5)
        price_entry = tk.Entry(add_dish_window)
        price_entry.grid(row=2, column=1, padx=5, pady=5)

        availability_label = tk.Label(add_dish_window, text="Availability:")
        availability_label.grid(row=3, column=0, padx=5, pady=5)
        availability_entry = tk.Entry(add_dish_window)
        availability_entry.grid(row=3, column=1, padx=5, pady=5)

        add_button = tk.Button(add_dish_window, text="Add", command=lambda: self.add_dish(
            add_dish_window, dish_id_entry.get(), dish_name_entry.get(), price_entry.get(), availability_entry.get()))
        add_button.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

    def add_dish(self, add_dish_window, dish_id, dish_name, price, availability):
        try:
            price = float(price)
            dish = Dish(dish_id, dish_name, price, availability)
            self.zesty_zomato.add_dish(dish)
            self.update_menu_listbox()
            messagebox.showinfo("Success", "Dish added successfully.")
            add_dish_window.destroy()
        except ValueError:
            messagebox.showinfo(
                "Error", "Invalid price. Please enter a numeric value.")

    def open_remove_dish_window(self):
        remove_dish_window = tk.Toplevel(self.root)
        remove_dish_window.title("Remove Dish")

        dish_id_label = tk.Label(remove_dish_window, text="Dish ID:")
        dish_id_label.grid(row=0, column=0, padx=5, pady=5)
        dish_id_entry = tk.Entry(remove_dish_window)
        dish_id_entry.grid(row=0, column=1, padx=5, pady=5)

        remove_button = tk.Button(remove_dish_window, text="Remove", command=lambda: self.remove_dish(
            remove_dish_window, dish_id_entry.get()))
        remove_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

    def remove_dish(self, remove_dish_window, dish_id):
        if self.zesty_zomato.remove_dish(dish_id):
            self.update_menu_listbox()
            messagebox.showinfo("Success", "Dish removed successfully.")
            remove_dish_window.destroy()
        else:
            messagebox.showinfo("Error", "Invalid Dish ID.")

    def open_update_availability_window(self):
        update_availability_window = tk.Toplevel(self.root)
        update_availability_window.title("Update Availability")

        dish_id_label = tk.Label(update_availability_window, text="Dish ID:")
        dish_id_label.grid(row=0, column=0, padx=5, pady=5)
        dish_id_entry = tk.Entry(update_availability_window)
        dish_id_entry.grid(row=0, column=1, padx=5, pady=5)

        availability_label = tk.Label(
            update_availability_window, text="Availability:")
        availability_label.grid(row=1, column=0, padx=5, pady=5)
        availability_entry = tk.Entry(update_availability_window)
        availability_entry.grid(row=1, column=1, padx=5, pady=5)

        update_button = tk.Button(update_availability_window, text="Update", command=lambda: self.update_availability(
            update_availability_window, dish_id_entry.get(), availability_entry.get()))
        update_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def update_availability(self, update_availability_window, dish_id, availability):
        if self.zesty_zomato.update_availability(dish_id, availability):
            self.update_menu_listbox()
            messagebox.showinfo(
                "Success", "Availability updated successfully.")
            update_availability_window.destroy()
        else:
            messagebox.showinfo("Error", "Invalid Dish ID.")

    def open_take_order_window(self):
        take_order_window = tk.Toplevel(self.root)
        take_order_window.title("Take Order")

        customer_name_label = tk.Label(
            take_order_window, text="Customer Name:")
        customer_name_label.grid(row=0, column=0, padx=5, pady=5)
        customer_name_entry = tk.Entry(take_order_window)
        customer_name_entry.grid(row=0, column=1, padx=5, pady=5)

        dish_ids_label = tk.Label(
            take_order_window, text="Dish IDs (comma-separated):")
        dish_ids_label.grid(row=1, column=0, padx=5, pady=5)
        dish_ids_entry = tk.Entry(take_order_window)
        dish_ids_entry.grid(row=1, column=1, padx=5, pady=5)

        take_button = tk.Button(take_order_window, text="Take Order", command=lambda: self.take_order(
            take_order_window, customer_name_entry.get(), dish_ids_entry.get()))
        take_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def take_order(self, take_order_window, customer_name, dish_ids):
        dish_ids = dish_ids.split(",")
        dish_ids = [dish_id.strip() for dish_id in dish_ids]
        self.zesty_zomato.take_order(customer_name, dish_ids)
        self.update_orders_listbox()
        take_order_window.destroy()

    def open_update_status_window(self):
        update_status_window = tk.Toplevel(self.root)
        update_status_window.title("Update Status")

        order_id_label = tk.Label(update_status_window, text="Order ID:")
        order_id_label.grid(row=0, column=0, padx=5, pady=5)
        order_id_entry = tk.Entry(update_status_window)
        order_id_entry.grid(row=0, column=1, padx=5, pady=5)

        status_label = tk.Label(update_status_window, text="Status:")
        status_label.grid(row=1, column=0, padx=5, pady=5)
        status_entry = tk.Entry(update_status_window)
        status_entry.grid(row=1, column=1, padx=5, pady=5)

        update_button = tk.Button(update_status_window, text="Update", command=lambda: self.update_status(
            update_status_window, order_id_entry.get(), status_entry.get()))
        update_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    def update_status(self, update_status_window, order_id, status):
        self.zesty_zomato.update_status(order_id, status)
        self.update_orders_listbox()
        update_status_window.destroy()

    def run(self):
        self.update_menu_listbox()
        self.update_orders_listbox()
        self.root.mainloop()


if __name__ == "__main__":
    gui = ZestyZomatoGUI()
    gui.run()
