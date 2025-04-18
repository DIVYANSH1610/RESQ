// script.js
document.getElementById('sendBtn').onclick = async function() {
  const input = document.getElementById('userInput');
  const message = input.value.trim();
  if (!message) return;

  addMessage('user', message);
  input.value = '';

  // Send message to backend
  const response = await fetch('http://127.0.0.1:5000/chat', {
    method: 'POST',
    headers: {'Content-Type': 'application/json'},
    body: JSON.stringify({message})
  });
  const data = await response.json();
  addMessage('bot', data.response);
};

function addMessage(sender, text) {
  const chatbox = document.getElementById('chatbox');
  const li = document.createElement('li');
  li.className = sender;
  li.textContent = text;
  chatbox.appendChild(li);
  chatbox.scrollTop = chatbox.scrollHeight;
}