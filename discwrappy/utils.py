import json

def recieve_json_response(ws):
    response = ws.recv()
    if response:
        return json.loads(response)

def send_json_request(ws, request):
    ws.send(json.dumps(request))