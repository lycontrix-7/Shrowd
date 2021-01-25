import json
from asgiref.sync import async_to_sync
from channels.generic.websocket import AsyncWebsocketConsumer

class ServerConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.server_name = self.scope['url_route']['kwargs']['server_name']
        self.server_group_name = 'chat_%s' % self.server_name

        # Join server group
        await self.channel_layer.group_add(
            self.server_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave server group
        await self.channel_layer.group_discard(
            self.server_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        # Send message to server group
        await self.channel_layer.group_send(
            self.server_group_name,
            {
                'type': 'chat_message',
                'message': message
            }
        )

    # Receive message from server group
    async def chat_message(self, event):
        message = event['message']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message
        }))