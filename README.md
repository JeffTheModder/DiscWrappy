# DiscWrappy
A Python wrapper for the Discord bot API

# Docs
### **Initialization:**
```py
import discwrappy

client = discwrappy.Client()

...

client.run(TOKEN)
```

### **Functions:**
**`@Client.on() - decorator`:**
  * **Params:**
    * **[event_type](./event_types.md) -** The type of event you're waiting for
  * **Function:**
    * Creates a "listener" which waits for the given event and triggers your function
> ```py
> @client.on("READY")
> def onReady(ready):
>     print("bot online")
> ```

**`Message.send() - function`:**
  * **Params:**
    * **message (dict) -** The Mesage you want to send
  * **Function:**
    * Sends the given dict to the message's channel
> ```py
> @client.on("MESSAGE_CREATE")
> def printMessageContent(message):
>     message.send({ "content": message.content})
> ```

**`discwrappy.Message() - class`:**
  * **Params:**
    * **message (dict) -** The default Discord message dict
  * **Function:**
    * Turns given message dict into a "proper object" (keys can be access with dot notation), converts numeric ids to ints, and gives the message send functions

**`discwrappy.User() - class`:**
  * **Params:**
    * **user (dict) -** The default Discord user dict
  * **Function:**
    * Turns given user dict into a "proper object" (keys can be access with dot notation) and converts numeric ids to ints

**`discwrappy.GuildMember() - class`:**
  * **Params:**
    * **user (dict) -** The default Discord guild member dict
  * **Function:**
    * Turns given guild member dict into a "proper object" (keys can be access with dot notation)
