import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
response = client.models.generate_content(model="gemini-2.0-flash-001",contents="why should one consider learning when they already know python")
if response.prompt_feedback and response.prompt_feedback.block_reason:
    print(f"Response was blocked. Reason: {response.prompt_feedback.block_reason}")
else:

    print(response.text)
    print(f"prompt_tokens:{response.usage_metadata.prompt_token_count}")
    print(f"response_tokens:{response.usage_metadata.candidates_token_count}")


