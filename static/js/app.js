let userId = localStorage.getItem(
    "mobilebot_user_id"
);


if (!userId) {

    userId = crypto.randomUUID();

    localStorage.setItem(
        "mobilebot_user_id",
        userId
    );
}


function quickMessage(message) {

    const input = document.getElementById(
        "message-input"
    );

    input.value = message;

    sendMessage();
}