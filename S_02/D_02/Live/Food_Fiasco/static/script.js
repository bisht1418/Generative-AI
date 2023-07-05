document.addEventListener("DOMContentLoaded", function () {
  // Handle form submission for adding a menu item
  document
    .getElementById("add-menu-form")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      var formData = new FormData(this);
      fetch("/menu", {
        method: "POST",
        body: formData,
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          alert(data.message);
          // Perform any additional actions after successful menu item addition
          // Refresh the menu list
          fetchMenuItems();
        })
        .catch(function (error) {
          console.log(error);
        });
    });

  // Handle form submission for updating menu item availability
  document
    .getElementById("update-menu-form")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      var formData = new FormData(this);
      fetch("/menu", {
        method: "PUT",
        body: formData,
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          alert(data.message);
          // Perform any additional actions after successful menu item availability update
          // Refresh the menu list
          fetchMenuItems();
        })
        .catch(function (error) {
          console.log(error);
        });
    });

  // Handle form submission for deleting a menu item
  document
    .getElementById("delete-menu-form")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      var formData = new FormData(this);
      fetch("/menu", {
        method: "DELETE",
        body: formData,
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          alert(data.message);
          // Perform any additional actions after successful menu item deletion
          // Refresh the menu list
          fetchMenuItems();
        })
        .catch(function (error) {
          console.log(error);
        });
    });

  // Handle form submission for placing an order
  document
    .getElementById("order-form")
    .addEventListener("submit", function (event) {
      event.preventDefault();
      var formData = new FormData(this);
      fetch("/order", {
        method: "POST",
        body: formData,
      })
        .then(function (response) {
          return response.json();
        })
        .then(function (data) {
          alert(data.message);
          // Perform any additional actions after successful order placement
          fetchOrders();
        })
        .catch(function (error) {
          console.log(error);
        });
    });

  var toggleButton = document.getElementById("toggle-button");
  var adminSection = document.getElementById("admin-section");
  var userSection = document.getElementById("user-section");

  toggleButton.addEventListener("click", function () {
    if (adminSection.style.display === "none") {
      adminSection.style.display = "block";
      userSection.style.display = "none";
      toggleButton.classList.remove("toggle-active");
    } else {
      adminSection.style.display = "none";
      userSection.style.display = "block";
      toggleButton.classList.add("toggle-active");
    }
  });

  // Fetch the menu items initially
});

function fetchMenuItems() {
  fetch("/menu")
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      // Update the menu list in the UI
      var menuList = document.getElementById("menu-list");
      menuList.innerHTML = "";
      data.forEach(function (item) {
        var listItem = document.createElement("li");
        listItem.innerText =
          item.name +
          " - Price: " +
          item.price +
          " - Availability: " +
          item.availability;
        menuList.appendChild(listItem);
      });
    })
    .catch(function (error) {
      console.log(error);
    });
}

function fetchOrders() {
  fetch("/orders")
    .then(function (response) {
      return response.json();
    })
    .then(function (data) {
      // Update the order list in the admin UI
      var orderList = document.getElementById("order-list");
      console.log(data, "****");
      orderList.innerHTML = "";
      data.forEach(function (order) {
        var listItem = document.createElement("li");
        listItem.innerText =
          "Order ID: " +
          order.item_id +
          " - Quantity: " +
          order.quantity +
          " - User Name: " +
          order.user_name;
        orderList.appendChild(listItem);
      });
    })
    .catch(function (error) {
      console.log(error.message, "#######");
    });
}

// =================================================

var chatContainer = document.getElementById("chat-container");
var userInput = document.getElementById("user-input");

var chatBox = document.getElementById("chat-box");

function toggleChatBox() {
  chatBox.classList.toggle("collapsed");
}

var generalProblems = [
  "I have a technical issue",
  "I have a billing problem",
  "I need assistance with my account",
  "I want to give feedback",
  "I have a question about a product",
];

var currentProblem = null;

// Event handler for user input
userInput.addEventListener("keypress", function (event) {
  if (event.keyCode === 13) {
    // Enter key pressed
    var userMessage = userInput.value;
    addMessage("user", userMessage);

    if (currentProblem === null) {
      processGeneralProblem(userMessage);
    } else {
      processSpecificProblem(userMessage);
    }

    userInput.value = ""; // Clear the input field
  }
});

// Function to add a message to the chat container
function addMessage(sender, message) {
  var messageDiv = document.createElement("div");
  messageDiv.className = sender + "-message";
  messageDiv.innerHTML = message;
  chatContainer.appendChild(messageDiv);
  chatContainer.scrollTop = chatContainer.scrollHeight; // Scroll to the bottom of the chat container
}

// Function to display general problems and handle user selection
function processGeneralProblem(userInput) {
  // Check if the user selected a general problem from the list
  var problemIndex = generalProblems.findIndex(function (problem) {
    return userInput.toLowerCase().includes(problem.toLowerCase());
  });

  if (problemIndex !== -1) {
    currentProblem = generalProblems[problemIndex];
    addMessage(
      "chatbot",
      "Great! How can I assist you with " + currentProblem.toLowerCase() + "?"
    );
    displaySpecificProblems();
  } else {
    addMessage(
      "chatbot",
      "Please select a general problem from the following list:"
    );
    displayGeneralProblems();
  }
}

// Function to display specific problems based on the selected general problem
function displaySpecificProblems() {
  var specificProblems;

  // Determine specific problems based on the selected general problem
  switch (currentProblem) {
    case "I have a technical issue":
      specificProblems = [
        "My device is not working",
        "I cannot access the website",
        "I am experiencing slow internet speed",
      ];
      break;
    case "I have a billing problem":
      specificProblems = [
        "I was charged incorrectly",
        "I did not receive my invoice",
        "I want to change my payment method",
      ];
      break;
    case "I need assistance with my account":
      specificProblems = [
        "I forgot my password",
        "I want to update my contact information",
        "I need to delete my account",
      ];
      break;
    case "I want to give feedback":
      specificProblems = [
        "I have a suggestion for improvement",
        "I want to report a bug",
        "I want to share a positive experience",
      ];
      break;
    case "I have a question about a product":
      specificProblems = [
        "I need more information about a specific product",
        "I want to know the warranty details",
        "I want to request a product demonstration",
      ];
      break;
    default:
      specificProblems = [];
      break;
  }

  addMessage(
    "chatbot",
    "Please select a specific problem from the following list:"
  );
  displaySuggestions(specificProblems);
}

// Function to display general problems as suggestions
function displayGeneralProblems() {
  addMessage(
    "chatbot",
    "Please select a general problem from the following list:"
  );
  displaySuggestions(generalProblems);
}

// Function to display a list of suggestions
function displaySuggestions(suggestions) {
  var suggestionsList = document.createElement("ul");
  suggestionsList.className = "suggestion-list";

  suggestions.forEach(function (suggestion) {
    var listItem = document.createElement("li");
    listItem.textContent = suggestion;
    listItem.addEventListener("click", function () {
      userInput.value = suggestion;
      userInput.dispatchEvent(new KeyboardEvent("keypress", { keyCode: 13 }));
    });
    suggestionsList.appendChild(listItem);
  });

  chatContainer.appendChild(suggestionsList);
}

// Function to process specific problem and generate chatbot response
function processSpecificProblem(userInput) {
  // Your logic to process the specific problem and generate a response from the chatbot
  // Here, we have a simple predefined set of responses for demonstration purposes

  var response;

  switch (currentProblem) {
    case "I have a technical issue":
      response =
        "Please provide more details about the technical issue you're facing.";
      break;
    case "I have a billing problem":
      response =
        "Please provide more details about the billing problem you're experiencing.";
      break;
    case "I need assistance with my account":
      response =
        "Please provide more details about the assistance you need with your account.";
      break;
    case "I want to give feedback":
      response =
        "Please provide more details about the feedback you want to give.";
      break;
    case "I have a question about a product":
      response =
        "Please provide more details about the product you have a question about.";
      break;
    default:
      response = "I'm sorry, but I didn't understand your query.";
      break;
  }

  // Display the chatbot's response
  setTimeout(function () {
    addMessage("chatbot", response);
  }, 500);
}
