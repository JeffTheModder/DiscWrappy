import websocket
import threading
import time
import requests
from .utils import *
from .Objects import *
import base64

class Client:
    def __init__(self):
        self.ws = websocket.create_connection("wss://gateway.discord.gg/?v=9&encoding=json")
        
        self.parsers = {}
        
        event = recieve_json_response(self.ws)

        heartbeat_interval = event["d"]["heartbeat_interval"]
        heartbeat_interval = heartbeat_interval / 1000

        def heartbeat(interval, ws):
            while True:
                time.sleep(interval)
                heartbeatJSON = {
                    "op": 1,
                    "d": "null"
                }
                send_json_request(ws, heartbeatJSON)

        threading._start_new_thread(heartbeat, (heartbeat_interval, self.ws, ))
    
    def run(self, token, activity = ""):
        self.header = {
            "Authorization": f"Bot {token}"
        }
        self.running = True

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

        send_json_request(self.ws, payload)

        while True:
            event = recieve_json_response(self.ws)
            try:
                for i in self.parsers[event["t"]]:
                    if event["t"] == "MESSAGE_CREATE":
                        i(Message(event, self))
                    else:
                        i(event)
            except:
                pass

    def on(self, eventType):
        def inner(func):
            """
            parser idea and code by Dynamo#3349
            """
            try:
                self.parsers[eventType].append(func)
            except:
                self.parsers[eventType] = []
                self.parsers[eventType].append(func)
        return inner