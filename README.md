# AI Gaming Chatbot (Valorant Assistant)

A lightweight, web-based gaming assistant designed to help **Valorant** players quickly access information about agents, roles, abilities, and core gameplay mechanics.

### **Live Application:** [https://ai-gaming-chatbot.onrender.com/](https://ai-gaming-chatbot.onrender.com/)

---

## Problem & Solution

* **Problem:** Players often struggle to quickly look up specific details regarding Valorant agents, roles, abilities, and gameplay strategies without interrupting their flow or sifting through lengthy wikis.
* **Solution:** This project provides an instant, responsive gaming chatbot powered by a keyword-matching knowledge base, delivering immediate answers to common Valorant queries through an intuitive chat interface.

---

## Features

* **Interactive Chat Interface:** Clean, user-friendly chat window built for quick Q&A.
* **Instant Keyword-Based Responses:** Fast query matching against a structured Valorant knowledge base.
* **Suggested Questions:** One-click prompt suggestions to help users explore topics effortlessly.
* **Local Chat History:** Automatically saves conversations locally so users can revisit past queries.
* **Window Controls:** Includes minimize, expand, and clear-chat options for a flexible user experience.
* **Responsive Design:** Adapts smoothly across desktop and mobile screen sizes.

---

## System Architecture & Modules

| Module | Description |
| :--- | :--- |
| **Frontend Module** | Manages the chat interface layout, styling, and responsiveness. |
| **User Interaction Module** | Handles user text input, button clicks, and suggested question triggers. |
| **Backend Module** | Processes incoming HTTP requests and routes responses using Flask. |
| **Knowledge Base Module** | Stores predefined Valorant questions, keywords, and answers. |
| **Response Matching Module** | Analyzes user queries and matches them with the most relevant stored response. |
| **Chat History Module** | Persists user conversation logs locally in the browser. |

---

## Chatbot Workflow

1. **Initialization:** User opens the chatbot web application.
2. **Onboarding:** Chatbot displays a welcome message alongside clickable suggested questions.
3. **Query Input:** User types a gaming-related question or selects a suggestion.
4. **Request Transmission:** Frontend sends the query payload to the Flask backend.
5. **Keyword Matching:** Backend processes the text and matches it against stored keywords.
6. **Response Generation:** Backend returns the matching answer as a JSON response.
7. **Display:** Frontend renders the bot's reply in the chat window.
8. **Persistence:** The conversation is saved to local storage for future sessions.

---

## Technologies Used

| Technology | Purpose / Role |
| :--- | :--- |
| **HTML5** | Semantic structure of the web application. |
| **CSS3** | Custom styling, animations, and responsive layout. |
| **JavaScript** | Client-side chat logic, DOM updates, API calls, and local storage. |
| **Python** | Core backend programming language and matching logic. |
| **Flask** | Lightweight web framework serving the UI and REST endpoints. |

---

## API Endpoints

| Endpoint | Method | Description |
| :--- | :--- | :--- |
| `/` *(Home API)* | `GET` | Renders and serves the main chatbot web interface. |
| `/chat` *(Chat API)* | `POST` | Receives user messages and returns matched chatbot responses. |
| `/questions` *(Questions API)* | `GET` | Fetches the list of predefined suggested questions. |

---

  ## Author

**Devu Veera Krishna Kaushik**

B.Tech – Computer Science & Engineering 

Python Developer | AI Enthusiast | Machine Learning

GitHub: [https://github.com/Devukaushik-26](https://github.com/Devukaushik-26)
