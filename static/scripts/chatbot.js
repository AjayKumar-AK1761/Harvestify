function toggleChatbot() {
    const container = document.getElementById('chatbot-container');
    container.style.display = (container.style.display === 'none' || container.style.display === '') ? 'block' : 'none';
}

const chatBox = document.getElementById("chat");
const userInput = document.getElementById("userInput");

function addMessage(sender, text) {
    const msg = document.createElement("div");
    msg.className = `message ${sender}`;
    msg.innerText = text;
    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function botReply(text) {
    addMessage("bot", text);
}

document.getElementById("chat-form").addEventListener("submit", async function (e) {
    e.preventDefault();
    const text = userInput.value.trim();
    if (!text) return;

    addMessage("user", text);
    userInput.value = "";

    if (/^\d/.test(text)) {
        try {
            const response = await fetch("/recommend", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ input: text })
            });

            const data = await response.json();
            if (response.ok) {
                botReply(data.message);
            } else {
                botReply(`Input Error: ${data.message}`);
            }
        } catch (err) {
            botReply("Server error: Could not connect to the recommendation API.");
        }
    } else {
        try {
            const response = await fetch("http://127.0.0.1:5001/chatbot", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ question: text })
            });
            const data = await response.json();
            if (response.ok) {
                botReply(data.answer || data.message || "No answer received from chatbot.");
            } else {
                botReply(`Chatbot Error: ${data.message || "Unknown error."}`);
            }
        } catch (err) {
            botReply("Server error: Could not connect to the chatbot API.");
        }
    }
});