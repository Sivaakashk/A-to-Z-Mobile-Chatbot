def validate_message(message):

    if not message:

        return False

    if not isinstance(
        message,
        str
    ):

        return False

    if len(message.strip()) < 1:

        return False

    if len(message) > 2000:

        return False

    return True