// script.js

// Retrieve the form and input elements
const addDishForm = document.getElementById("addDishForm");
const removeDishForm = document.getElementById("removeDishForm");
const updateAvailabilityForm = document.getElementById(
  "updateAvailabilityForm"
);
const takeOrderForm = document.getElementById("takeOrderForm");
const updateStatusForm = document.getElementById("updateStatusForm");

// Add event listener to the form for adding a dish
addDishForm.addEventListener("submit", (e) => {
  e.preventDefault();

  // Retrieve the input values
  const dishName = document.getElementById("dishName").value;
  const price = parseFloat(document.getElementById("price").value);
  const availability = document.getElementById("availability").checked;

  // Perform validation on the input values (you can add more validation as needed)
  if (!dishName || isNaN(price)) {
    alert("Please enter a dish name and a valid price.");
    return;
  }

  // Make a POST request to the backend to add the dish
  fetch("/menu/add", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      dish_name: dishName,
      price: price,
      availability: availability ? "on" : "off",
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Handle the response from the backend
      if (data.success) {
        // If the dish was successfully added, refresh the page to update the menu
        location.reload();
      } else {
        // If there was an error, display the error message
        alert(data.message);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    });
});

// Add event listener to the form for removing a dish
removeDishForm.addEventListener("submit", (e) => {
  e.preventDefault();

  // Retrieve the input values
  const dishId = parseInt(document.getElementById("removeDishId").value);

  // Make a POST request to the backend to remove the dish
  fetch("/menu/remove", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      dish_id: dishId,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Handle the response from the backend
      if (data.success) {
        // If the dish was successfully removed, refresh the page to update the menu
        location.reload();
      } else {
        // If there was an error, display the error message
        alert(data.message);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    });
});

// Add event listener to the form for updating dish availability
updateAvailabilityForm.addEventListener("submit", (e) => {
  e.preventDefault();

  // Retrieve the input values
  const dishId = parseInt(document.getElementById("updateDishId").value);
  const availability = document.getElementById("updateAvailability").checked;

  // Make a POST request to the backend to update the dish availability
  fetch("/menu/update_availability", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      dish_id: dishId,
      availability: availability ? "on" : "off",
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Handle the response from the backend
      if (data.success) {
        // If the availability was successfully updated, refresh the page to update the menu
        location.reload();
      } else {
        // If there was an error, display the error message
        alert(data.message);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    });
});

// Add event listener to the form for taking a new order
takeOrderForm.addEventListener("submit", (e) => {
  e.preventDefault();

  // Retrieve the input values
  const customerName = document.getElementById("customerName").value;
  const dishIds = Array.from(
    document.querySelectorAll('input[name="dishIds[]"]:checked')
  ).map((input) => parseInt(input.value));

  // Perform validation on the input values (you can add more validation as needed)
  if (!customerName || dishIds.length === 0) {
    alert("Please enter a customer name and select at least one dish.");
    return;
  }

  // Make a POST request to the backend to place the order
  fetch("/order/new", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      customer_name: customerName,
      dish_ids: dishIds,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Handle the response from the backend
      if (data.success) {
        // If the order was successfully placed, display a success message
        alert(data.message);
        // Clear the form inputs
        takeOrderForm.reset();
      } else {
        // If there was an error, display the error message
        alert(data.message);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    });
});

// Add event listener to the form for updating the order status
updateStatusForm.addEventListener("submit", (e) => {
  e.preventDefault();

  // Retrieve the input values
  const orderId = parseInt(document.getElementById("order_id").value);
  const status = document.getElementById("new_status").value;

  // Make a POST request to the backend to update the order status
  fetch("/order/update_status", {
    method: "POST",
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      order_id: orderId,
      status: status,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Handle the response from the backend
      if (data.success) {
        // If the status was successfully updated, display a success message
        alert(data.message);
        // Clear the form inputs
        updateStatusForm.reset();
      } else {
        // If there was an error, display the error message
        alert(data.message);
      }
    })
    .catch((error) => {
      console.error("Error:", error);
      alert("An error occurred. Please try again.");
    });
});
