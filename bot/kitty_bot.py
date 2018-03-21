import logging

import aiohttp
from bs4 import BeautifulSoup

from bot.message import Message
from settings import settings


class KittyBot:
    message_cls = Message

    def __init__(self, token):
        self.token = token

    async def start(self):
        url = f'https://api.telegram.org/bot{self.token}/setWebhook?url={settings.WEBHOOK_URL_PATH}'
        async with aiohttp.request('POST', url, headers={'Content-Type': 'application/json'}) as response:
            assert response.status == 200, 'Setting the hook failed.'
        logging.info('KittyBot started webhook mode')

    async def process_message(self, msg):
        message = self.message_cls(msg)
        await getattr(self, str(u'cmd_{}'.format(message.command)), self.cmd_unknown)(message)

    async def send_msg(self, chat_id, text):
        url = f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={chat_id}>&text={text}'
        async with aiohttp.request('GET', url) as response:
            if response.status != 200:
                logging.warning(f'Received response status {response.status}')

    async def cmd_start(self, message):
        logging.info(f'New user with chat_id {message.chat_id}')
        await self.cmd_help(message)

    async def cmd_unknown(self, message):
        kitty = await self.get_kitty()
        await self.send_msg(message.chat_id, kitty)

    async def cmd_help(self, message):
        response = "This is a Kitty Bot! Just type me anything and I will send you some kitty!"
        await self.send_msg(message.chat_id, response)

    @staticmethod
    async def get_kitty():
        async with aiohttp.request('GET', settings.CAT_API_URL) as response:
            body = await response.read()
        soup = BeautifulSoup(body, 'html.parser')
        return soup.img["src"]
