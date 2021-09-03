import discwrappy

client = discwrappy.Client()

client.run("ODgyNzE4NDQ4MzczODcwNjYy.YS_dng.wbInPOY5VU5OC10pbIQFrFuzvwk")

@client.on("MESSAGE_CREATE")
def printMessageContent(message):
    if message.content.startswith("+"):
        command_content = message.content[1:]
        cmd = command_content.strip().split()[0]

        if cmd == "say":
            client.send(message.channel_id, { "content": command_content.strip()[3:].strip() })