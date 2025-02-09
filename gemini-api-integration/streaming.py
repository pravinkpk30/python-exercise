from google import genai

client = genai.Client(api_key="AIzaSyBn0HK6oboIXyK9nAnlvs6mgmaMnR8_thU")

for chunk in client.models.generate_content_stream(
  model='gemini-2.0-flash',
  contents='Tell me a story in 300 words.'
):
    print(chunk.text)