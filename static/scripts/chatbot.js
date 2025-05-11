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
        const lower = text.toLowerCase();
        if (["hi", "hello", "hey"].includes(lower)) {
            botReply("Hi! To get a crop recommendation, please type your values as: N,P,K,temperature,humidity,pH,rainfall");
        } else if (lower === "start") {
            botReply("Please provide your values in the format: N,P,K,temp,humidity,ph,rainfall");
        } else {
            botReply("Sorry, I didn't understand that. Please enter valid crop input values or say 'hi'.");
        }
    }
});