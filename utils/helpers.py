def format_price(price):

    if not price:

        return "Price unavailable"

    return f"₹{price:,}"


def clean_text(text):

    if not text:

        return ""

    return text.strip()