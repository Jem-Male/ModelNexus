from openai import OpenAI

from config import AI_URL, AI_API_KEY, AI_MODEL # type: ignore

client = OpenAI(
    base_url=AI_URL,
    api_key=AI_API_KEY
)