import asyncio
import argparse
from aiohttp import web

from bot.kitty_bot import KittyBot
from views.bot_view import BotView
from settings import settings


class Application(web.Application):
    def __init__(self):
        super().__init__(loop=asyncio.get_event_loop())
        self.bot = KittyBot(settings.BOT_TOKEN)

    def start(self, port):
        self.router.add_route('POST', settings.WEBHOOK_ROUTE, BotView)
        self.loop.run_until_complete(self.bot.start())
        web.run_app(self, host='0.0.0.0', port=port)

    async def process_message(self, data):
        await self.bot.process_message(data)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', action='store', help='Application port')
    args = parser.parse_args()

    app = Application()
    app.start(args.port or settings.DEFAULT_PORT)


if __name__ == "__main__":
    main()
