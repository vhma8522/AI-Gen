from google import genai

## iMPORT ENV
import os
from dotenv import load_dotenv

# Load the variables from the .env file into the system environment
load_dotenv()

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client()
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY_V2"))

response = client.models.generate_content(
    model="gemini-3-flash-preview",contents="Como desarrollador de videojuegos, explicame como se hacian las integraciones de npcs en los juegos de los 90s y como se hacen ahora"
)
print(response.text)