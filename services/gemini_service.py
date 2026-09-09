from google import genai

from config import Config


client = genai.Client(
    api_key=Config.GEMINI_API_KEY
)


SYSTEM_PROMPT = """
You are MobileBot, an AI assistant specializing
exclusively in mobile phones and smartphones.

You are similar to an intelligent mobile phone advisor.

You help users with:

- Mobile phone recommendations
- Phone comparisons
- Phone specifications
- Camera performance
- Gaming performance
- Battery life
- Processor performance
- Displays
- RAM and storage
- Android and iPhone information
- Budget phone recommendations
- Indian smartphone market

Important Rules:

1. Use the phone database information provided to you.
2. Never invent specifications.
3. If exact information is unavailable, clearly say so.
4. Recommend phones based on budget and requirements.
5. Use Indian Rupees (₹).
6. Keep answers clear and mobile-friendly.
7. You specialize in smartphones only.
8. When comparing phones, clearly explain which one is better and why.
"""


def generate_response(
    user_message,
    phone_data=None,
    history=None
):

    prompt = SYSTEM_PROMPT

    if phone_data:

        prompt += """

PHONE DATABASE INFORMATION:
"""

        for phone in phone_data:

            prompt += f"""

Phone: {phone.get('full_name')}
Brand: {phone.get('brand')}
Price: ₹{phone.get('price')}
Processor: {phone.get('processor')}
Display: {phone.get('display')}
Battery: {phone.get('battery')}
Camera: {phone.get('camera')}
RAM: {phone.get('ram')}
Storage: {phone.get('storage')}
Ratings: {phone.get('ratings')}
"""

    if history:

        prompt += """

RECENT CONVERSATION:
"""

        for item in history[-5:]:

            prompt += f"""

User: {item['message']}
Assistant: {item['response']}
"""

    prompt += f"""

USER QUESTION:

{user_message}
"""

    try:

        response = (
            client.models.generate_content(

                model="gemini-3.1-flash-lite",

                contents=prompt

            )
        )

        return response.text

    except Exception as error:

        print(
            "Gemini Error:",
            str(error)
        )

        return (
            "Sorry, I am unable to process "
            "your request right now."
        )