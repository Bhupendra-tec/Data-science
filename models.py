from google import genai
import os
api_key = os.getenv('GEMINI_API_KEY')
#configure API Key
client = genai.Client(api_key = api_key)
# API model
def gemini_model(prompt):
    interaction = client.interactions.create(
        model="gemini-3.8-flash",
        input=prompt
    )

    return interaction.output_text

