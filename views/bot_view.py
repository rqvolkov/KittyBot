import json

from aiohttp import web


class BotView(web.View):
    """
    View for handling income messages requests.
    """
    async def post(self):
        try:
            data = await self.request.json()
        except json.decoder.JSONDecodeError:
            return web.Response(status=400, text=json.dumps({'message': 'Cannot decode json.'}))
        await self.request.app.process_message(data)
        return web.Response()
