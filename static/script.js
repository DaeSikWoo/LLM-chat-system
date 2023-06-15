// Display and append the messages
function appendMessage(sender, message, className) {
  var chatLog = document.getElementById("chat-log");
  var messageElem = document.createElement("div");
  messageElem.innerHTML = "<strong>" + sender + ": </strong>" + message;
  messageElem.className = className;
  chatLog.appendChild(messageElem);
  chatLog.scrollTop = chatLog.scrollHeight;
}

// Function to handle user input
function handleUserInput() {
  var userInput = document.getElementById("user-input");
  var message = userInput.value;
  userInput.value = "";

  // Display the user message
  appendMessage("You", message, "user-message");
  // Display the response time
  var responseTimeElem = document.createElement("div");
  responseTimeElem.innerHTML = "Response Time: " + responseTime.toFixed(2) + " seconds";
  responseTimeElem.className = "response-time";
  chatLog.appendChild(responseTimeElem);
  
  // Send the user input to the Python backend for processing
  var xhr = new XMLHttpRequest();
  xhr.open("POST", "/", true);

  xhr.onreadystatechange = function() {
    if (xhr.readyState === XMLHttpRequest.DONE && xhr.status === 200) {
      var response = JSON.parse(xhr.responseText);
      var answer = response.answer;
      // Remove "Bot is typing" message
      var botTypingMessage = document.getElementById("bot-typing-message");
      if (botTypingMessage) {
        botTypingMessage.remove();
      }
      appendMessage("Bot", answer, "bot-message");
    }
  };

  // Show "Bot is typing" message while waiting for response
  appendMessage("Bot", "Bot is typing...", "typing-message");
  // Assign an ID to "Bot is typing" message for easy removal
  var botTypingMessage = document.getElementsByClassName("typing-message")[0];
  botTypingMessage.setAttribute("id", "bot-typing-message");

  var formData = new FormData();
  formData.append("query", message);

  xhr.send(formData);
}

// Attach event listener to the send button
var sendButton = document.getElementById("send-btn");
sendButton.addEventListener("click", handleUserInput);

// Attach event listener to handle user input on Enter key press
var userInputField = document.getElementById("user-input");
userInputField.addEventListener("keyup", function(event) {
  if (event.keyCode === 13) {
    event.preventDefault();
    handleUserInput();
  }
});
