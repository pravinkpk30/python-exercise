from google import genai
from PIL import Image

client = genai.Client(api_key="AIzaSyBn0HK6oboIXyK9nAnlvs6mgmaMnR8_thU")

response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents=[
        'Tell me a story based on this image',
        Image.open("./assests/Man.jpeg")
    ]
)
print(response.text)