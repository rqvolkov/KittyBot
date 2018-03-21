class Message(object):
    """
    Minimized message class for handling simple requests.
    """
    def __init__(self, message):
        self.__message = message.get('message') or message['edited_message']

    @property
    def chat_id(self):
        return self.__message['chat']['id']

    @property
    def text(self):
        return self.__message.get('text', '')

    @property
    def command(self):
        if len(self.text) != 0:
            return self.text.split()[0].replace('/', '')
        return ''
