from google import genai

client = genai.Client(api_key="AIzaSyBn0HK6oboIXyK9nAnlvs6mgmaMnR8_thU")

# Normal generated content

# chat = client.chats.create(model="gemini-2.0-flash")
# response = chat.send_message("I have 2 dogs in my house.")
# print(response.text)
# response = chat.send_message("How many paws are in my house?")
# print(response.text)
# for message in chat._curated_history:
#     print(f'role - ', message.role, end=": ")
#     print(message.parts[0].text)

# Stream generated content

chat = client.chats.create(model="gemini-2.0-flash")
response = chat.send_message_stream("I have 2 dogs in my house.")
for chunk in response:
    print(chunk.text, end="")
response = chat.send_message_stream("How many paws are in my house?")
for chunk in response:
    print(chunk.text, end="")
for message in chat._curated_history:
    print(f'role - ', message.role, end=": ")
    print(message.parts[0].text)