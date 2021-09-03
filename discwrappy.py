import json
import websocket
import threading
import time
import requests
import utils
import base64

class Client:
    def __init__(self):
        self.ws = websocket.create_connection("wss://gateway.discord.gg/?v=9&encoding=json")
        self.api_base_url = "https://discord.com/api/v9"
        
        event = self.recieve_json_response(self.ws)

        heartbeat_interval = event["d"]["heartbeat_interval"]
        heartbeat_interval = heartbeat_interval / 1000

        def heartbeat(interval, ws):
            while True:
                time.sleep(interval)
                heartbeatJSON = {
                    "op": 1,
                    "d": "null"
                }
                self.send_json_request(ws, heartbeatJSON)

        threading._start_new_thread(heartbeat, (heartbeat_interval, self.ws, ))

    def recieve_json_response(self, ws):
        response = ws.recv()
        if response:
            return json.loads(response)

    def send_json_request(self, ws, request):
        ws.send(json.dumps(request))
    
    def run(self, token, activity = ""):
        self.running = True
        self.header = {
            "Authorization": f"Bot {token}"
        }
        self.bot_id = token.split(".")[0]
        self.bot_id = int(base64.b64decode(self.bot_id))

        payload = {
            "op": 2,
            "d": {
                "token": token,
                "intents": 513,
                "properties": {
                    "$os": 'windows',
                    "$browser": 'chrome',
                    "$device": 'pc',
                },
            }
        }

        self.send_json_request(self.ws, payload)
        print("Logged In")

    def on(self, eventType):
        def inner(func):
            while self.running:
                event = self.recieve_json_response(self.ws)
                event = utils.DictX(event)
                if event.t == eventType:
                    if not(int(event.d["author"]["id"]) == self.bot_id):
                        func(utils.DictX(event.d))
        return inner

    def send(self, channel_id, msgJSON):
        requests.post(f"{self.api_base_url}/channels/{channel_id}/messages", json=msgJSON, headers=self.header)