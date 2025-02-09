from google import genai

client = genai.Client(api_key="AIzaSyBn0HK6oboIXyK9nAnlvs6mgmaMnR8_thU")

chat = client.chats.create(model='gemini-2.0-flash')

response = chat.send_message(
    message='Tell me a story in 100 words')
response = chat.send_message(
    message='What happened after that?')