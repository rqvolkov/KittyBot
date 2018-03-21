import os
import logging


logging.basicConfig(level=logging.INFO)

CAT_API_ENDPOINT = 'http://thecatapi.com/api/images/get?format=html'

CAT_API_KEY = os.environ.get('KITTY_BOT_API_KEY')
BOT_TOKEN = os.environ.get('KITTY_BOT_TOKEN')
WEBHOOK_HOST = os.environ.get('KITTY_BOT_HOST')

CAT_API_URL = CAT_API_ENDPOINT
if CAT_API_KEY:
    CAT_API_URL += f'&api_key={CAT_API_KEY}'
WEBHOOK_ROUTE = f'/{BOT_TOKEN}/'
WEBHOOK_URL_PATH = WEBHOOK_HOST + WEBHOOK_ROUTE

DEFAULT_PORT = 8081

assert BOT_TOKEN is not None
assert WEBHOOK_HOST is not None
