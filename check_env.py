import os

from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv("API_KEY")
sec_user_agent = os.getenv("SEC_USER_AGENT")

if api_key:
    print(f"API_KEY: {api_key[:4]}...")
else:
    print("API_KEY is missing")

if sec_user_agent:
    print(f"SEC_USER_AGENT: {sec_user_agent}")
else:
    print("SEC_USER_AGENT is missing")
