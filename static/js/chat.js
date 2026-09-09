async function sendMessage() {

    const input = document.getElementById(
        "message-input"
    );

    const message = input.value.trim();

    if (!message) {
        return;
    }

    addMessage(
        message,
        "user-message"
    );

    input.value = "";


    try {

        const response = await fetch(
            "/api/chat",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({

                    message: message,

                    user_id:
                        "guest_user"

                })

            }
        );


        const data = await response.json();


        addMessage(
            data.response ||
            data.message ||
            "Sorry, I could not process your request.",

            "bot-message"
        );

    }

    catch (error) {

        console.error(error);

        addMessage(

            "Server connection error.",

            "bot-message"
        );

    }

}


function addMessage(
    message,
    className
) {

    const chatBox = document.getElementById(
        "chat-box"
    );

    const messageDiv =
        document.createElement("div");


    messageDiv.className =
        "message " + className;


    const paragraph =
        document.createElement("p");


    paragraph.textContent =
        message;


    messageDiv.appendChild(
        paragraph
    );


    chatBox.appendChild(
        messageDiv
    );


    chatBox.scrollTop =
        chatBox.scrollHeight;
}


document
    .getElementById("message-input")
    .addEventListener(

        "keypress",

        function (event) {

            if (
                event.key === "Enter"
            ) {

                sendMessage();

            }

        }

    );