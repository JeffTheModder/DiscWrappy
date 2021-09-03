# DiscWrappy
A Python wrapper for the Discord bot API

# Docs
### **Initialization:**
```py
import discwrappy

client = discwrappy.Client()
client.run(TOKEN)
```

### **Commands:**
**`@Client.on()`:**
  * **Params:**
    * **[event_type](./event_type.md) -** The type of event you're waiting for
> ```py
> @client.on("MESSAGE_CREATE")
> def printMessageContent(message):
>     print(message.content)
> ```
**`@Client.send()`:**
  * **Params:**
    * **channel_id -** The channel you want to send the message to
    * **message (JSON) -** The Mesage you want to send
> ```py
> @client.on("MESSAGE_CREATE")
> def printMessageContent(message):
>     client.send(message.channel_id, { "content": message.content})
> ```
