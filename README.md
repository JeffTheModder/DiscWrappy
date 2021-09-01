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
    * **event_type -** The type of event you're waiting for
> ```py
> @client.on("MESSAGE_CREATE")
> def printMessageContent(message):
>     print(message.content)
> ```
