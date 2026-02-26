from google import genai
from google.genai import types
from PIL import Image #Import the Pillow library for image handling

## iMPORT ENV
import os
from dotenv import load_dotenv

# Load the variables from the .env file into the system environment
load_dotenv()

# The client Google IA.
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY_V2"))

# Prompt for image generation
prompt = ("imagen de una taza")

# Response for image generation
response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt],
)

image_name = "generated_image.png"

try:
    for part in response.parts:
        if part.text is not None:
            print(part.text)
        elif part.inline_data is not None:
            image = part.as_image()
            image.save(image_name)

except Exception as e:
    print(f"An error occurred: {e}")
    print(f"Image saved as {image_name}")

finally:
    print("Process completed.")
