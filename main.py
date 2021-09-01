import discwrappy

client = discwrappy.Client()

client.run("ODgyNzE4NDQ4MzczODcwNjYy.YS_dng.wbInPOY5VU5OC10pbIQFrFuzvwk", "hi")

@client.on("MESSAGE_CREATE")
def printMessageContent(message):
    print(message["d"]["content"])