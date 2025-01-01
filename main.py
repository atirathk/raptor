from dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPEN_AI_API_KEY")
os.environ["OPENAI_API_KEY"] = your-openai-api-key

from raptor import RetrievalAugmentation

# Initialize with default configuration. For advanced configurations, check the documentation. [WIP]
RA = RetrievalAugmentation()

with open('sample.txt', 'r') as file:
    text = file.read()
RA.add_documents(text)