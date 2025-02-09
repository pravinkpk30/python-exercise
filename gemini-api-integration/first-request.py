from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyBn0HK6oboIXyK9nAnlvs6mgmaMnR8_thU")
response = client.models.generate_content(
    model="gemini-2.0-flash", contents="Explain how AI works",
    # config=types.GenerateContentConfig(
    #     max_output_tokens=500,
    #     temperature=0.1
    # )
)
print(response.text)