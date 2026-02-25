from google import genai
from google.genai import types
from PIL import Image #Import the Pillow library for image handling

## iMPORT ENV
import os
from dotenv import load_dotenv

# Load the variables from the .env file into the system environment
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY_V2"))

prompt = ("como dieñador grafico, genera una imagen de una taza de cafe para una camapaña")
response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")