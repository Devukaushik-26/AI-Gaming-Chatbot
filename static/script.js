const chatForm = document.getElementById("chatForm");
const userInput = document.getElementById("userInput");
const messages = document.getElementById("messages");

const suggestions = document.getElementById("suggestions");

const chatbot = document.getElementById("chatbot");
const minimizeBtn = document.getElementById("minimizeBtn");
const restoreBtn = document.getElementById("restoreBtn");
const expandBtn = document.getElementById("expandBtn");
const clearBtn = document.getElementById("clearBtn");

const STORAGE_KEY = "valorantChatHistory";

let chatHistory = [];


/* Display a chat message */

function addMessage(text, sender, save = true) {
    const messageDiv = document.createElement("div");

    messageDiv.classList.add(
        "message",
        sender === "user" ? "user-message" : "bot-message"
    );

    const textSpan = document.createElement("span");
    textSpan.textContent = text;

    const timeSpan = document.createElement("span");
    timeSpan.className = "message-time";
    timeSpan.textContent = new Date().toLocaleTimeString([], {
        hour: "2-digit",
        minute: "2-digit"
    });

    messageDiv.appendChild(textSpan);
    messageDiv.appendChild(timeSpan);

    messages.appendChild(messageDiv);

    messages.scrollTop = messages.scrollHeight;

    if (save) {
        chatHistory.push({ text, sender });
        localStorage.setItem(
            STORAGE_KEY,
            JSON.stringify(chatHistory.slice(-100))
        );
    }
}


/* Restore previous chat */

function loadChatHistory() {
    const saved = localStorage.getItem(STORAGE_KEY);

    if (!saved) return;

    try {
        chatHistory = JSON.parse(saved);

        chatHistory.forEach(message => {
            addMessage(message.text, message.sender, false);
        });
    } catch {
        chatHistory = [];
        localStorage.removeItem(STORAGE_KEY);
    }
}


/* Send message to Flask */

async function sendMessage(message) {
    if (!message.trim()) return;

    addMessage(message, "user");

    userInput.value = "";
    userInput.focus();

    try {
        const response = await fetch("/api/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ message })
        });

        const data = await response.json();

        addMessage(
            data.reply || "I couldn't process that message.",
            "bot"
        );

    } catch (error) {
        addMessage(
            "Connection error! Please make sure the server is running.",
            "bot"
        );
    }
}


/* Form submission */

chatForm.addEventListener("submit", function(event) {
    event.preventDefault();

    sendMessage(userInput.value);
});


/* Suggested questions */

async function loadSuggestions() {
    try {
        const response = await fetch("/api/questions");
        const questions = await response.json();

        suggestions.innerHTML = "";

        questions.slice(0, 5).forEach(question => {
            const button = document.createElement("button");

            button.className = "suggestion-btn";
            button.textContent = question;

            button.addEventListener("click", () => {
                sendMessage(question);
            });

            suggestions.appendChild(button);
        });

    } catch (error) {
        console.error("Could not load suggestions:", error);
    }
}


/* Minimize chatbot */

minimizeBtn.addEventListener("click", () => {
    chatbot.classList.add("minimized");
    restoreBtn.classList.add("visible");
});


/* Restore chatbot */

restoreBtn.addEventListener("click", () => {
    chatbot.classList.remove("minimized");
    restoreBtn.classList.remove("visible");
});


/* Expand chatbot */

expandBtn.addEventListener("click", () => {
    chatbot.classList.toggle("expanded");
});


/* Clear chat history */

clearBtn.addEventListener("click", () => {
    chatHistory = [];

    localStorage.removeItem(STORAGE_KEY);
    messages.innerHTML = "";
});


/* Initialize */

loadChatHistory();
loadSuggestions();

