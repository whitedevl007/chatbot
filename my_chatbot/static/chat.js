// document.addEventListener('DOMContentLoaded', function () {
//     const chatForm = document.getElementById('chat-form');
//     const userMessageInput = document.getElementById('user-message');
//     const chatContainer = document.getElementById('chat-container');

//     chatForm.addEventListener('submit', function (e) {
//         e.preventDefault();
//         const userMessage = userMessageInput.value.trim();

//         if (userMessage) {
//             // Send user message to the server
//             fetch('/chat', {
//                 method: 'POST',
//                 headers: { 'Content-Type': 'application/json' },
//                 body: JSON.stringify({ user_id: '123', user_message: userMessage })
//             })
//             .then(response => response.json())
//             .then(data => {
//                 const responseMessage = document.createElement('p');
//                 responseMessage.textContent = data.response;
//                 chatContainer.appendChild(responseMessage);
//                 userMessageInput.value = '';
//             });
//         }
//     });
// });



document.addEventListener('DOMContentLoaded', function () {
    const chatForm = document.getElementById('chat-form');
    const userMessageInput = document.getElementById('user-message');
    const chatContainer = document.getElementById('chat-container');

    chatForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const userMessage = userMessageInput.value.trim();

        if (userMessage) {
            // Display user's message
            const userMessageElement = document.createElement('p');
            userMessageElement.textContent = `You: ${userMessage}`;
            chatContainer.appendChild(userMessageElement);

            // Send user message to the server
            fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: userMessage })
            })
            .then(response => response.json())
            .then(data => {
                // Display chatbot's response
                const responseMessage = document.createElement('p');
                responseMessage.textContent = `Chatbot: ${data.response}`;
                chatContainer.appendChild(responseMessage);
                userMessageInput.value = '';
            });
        }
    });
});

