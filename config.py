from dotenv import load_dotenv
import os

load_dotenv()

VALID_USERNAME = os.getenv("VALID_USERNAME")
VALID_PASSWORD = os.getenv("VALID_PASSWORD")

FIRST_NAME_CHECKOUT = os.getenv("FIRST_NAME_CHECKOUT")
LAST_NAME_CHECKOUT = os.getenv("LAST_NAME_CHECKOUT")
POSTAL_CODE_CHECKOUT = os.getenv("POSTAL_CODE_CHECKOUT")