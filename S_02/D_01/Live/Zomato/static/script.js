// Retrieve the dish menu and display it on the page
fetch("/menu")
  .then((response) => response.json())
  .then((data) => {
    const menuList = document.getElementById("menu-list");
    data.forEach((dish) => {
      const li = document.createElement("li");
      li.textContent = `${dish.name} - Price: $${dish.price}`;
      menuList.appendChild(li);
    });
  });

// Handle form submission for placing an order
const orderForm = document.getElementById("order-form");
orderForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const customerName = document.getElementById("customer-name").value;
  const dishIds = document.getElementById("dish-ids").value.split(",");

  const order = {
    customer_name: customerName,
    dish_ids: dishIds.map((id) => parseInt(id.trim())),
  };

  fetch("/orders", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(order),
  })
    .then((response) => response.json())
    .then((data) => {
      const ordersList = document.getElementById("orders-list");
      const li = document.createElement("li");
      li.textContent = `Order ID: ${data.order_id} - Status: ${data.status}`;
      ordersList.appendChild(li);
    });

  orderForm.reset();
});

// Retrieve the orders and display them on the page
fetch("/orders")
  .then((response) => response.json())
  .then((data) => {
    const ordersList = document.getElementById("orders-list");
    data.forEach((order) => {
      const li = document.createElement("li");
      li.textContent = `Order ID: ${order.order_id} - Status: ${order.status}`;
      ordersList.appendChild(li);
    });
  });
