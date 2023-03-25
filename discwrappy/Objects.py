import requests

class Message:
    def __init__(self, messageDict, client):
        self.client = client

        oMF = messageDict["d"] # Original Message Format; store the returned message Dict's "data"
        self.type = oMF["type"]
        self.tts = oMF["tts"]
        self.timestamp = oMF["timestamp"]
        self.thread = oMF.get("thread")
        self.referenced_message = oMF.get("referenced_message")
        self.reactions = oMF.get("reactions")
        self.pinned = oMF["pinned"]
        self.sticker_items = oMF.get("sticker_items")
        self.mentions = oMF["mentions"]
        self.mention_channels = oMF.get("mention_channels")
        self.mention_roles = oMF["mention_roles"]
        self.mention_everyone = oMF["mention_everyone"]
        self.member = GuildMember(oMF.get("member"))
        self.nonce = oMF.get("nonce")
        self.id = int(oMF["id"])
        self.interaction = oMF.get("interaction")
        self.flags = oMF.get("flags")
        self.embeds = oMF["embeds"]
        self.edited_timestamp = oMF["edited_timestamp"]
        self.application_id = oMF.get("application_id")
        self.application = oMF.get("application")
        self.activity = oMF.get("activity")
        self.content = oMF["content"]
        self.components = oMF.get("components")
        self.channel_id = int(oMF["channel_id"])
        self.author = User(oMF["author"])
        self.attachments = oMF["attachments"]
        self.guild_id = int(oMF.get("guild_id"))
        self.webhook_id = oMF.get("webhook_id")

    def send(self, msg):
        msgJSON = {}
        msgJSON["embeds"] = []
        msgJSON["attachments"] = []

        if type(msg) == str:
            msgJSON["content"] = msg

        if type(msg) == dict:
            for key, value in msg.items():
                if key == "content": # the content of the message
                    msgJSON["content"] = value
                elif key == "embeds": # list of embeds
                    for embeds_item in value:
                        if type(embeds_item) != dict:
                            embeds_item = vars(embeds_item)
                    msgJSON["embeds"] = value
                elif key == "embed": # single embed
                    if type(value) != dict:
                        value = vars(value)
                    msgJSON["embeds"].append(value)
                elif key == "attachments": # list of attachments
                    msgJSON["attachments"] = value
                elif key == "attachment": # single attachment
                    msgJSON["attachments"].append(value)
                else:
                    raise ValueError(f"\"{key.upper()}\" is not a valid value")

        requests.post(f"https://discord.com/api/v9/channels/{self.channel_id}/messages", json=msgJSON, headers=self.client.header)

class User:
    def __init__(self, userDict):
        self.id = int(userDict["id"])
        self.username = userDict["username"]
        self.discriminator = userDict["discriminator"]
        self.avatar = userDict["avatar"]
        self.bot = userDict.get("bot")
        self.system = userDict.get("system")
        self.mfa_enabled = userDict.get("mfa_enabled")
        self.banner = userDict.get("banner")
        self.accent_color = userDict.get("accent_color")
        self.locale = userDict.get("locale")
        self.verified = userDict.get("verified")
        self.email = userDict.get("email")
        self.flags = userDict.get("flags")
        self.premium_type = userDict.get("premium_type")
        self.public_flags = userDict.get("public_flags")

class GuildMember(dict):
    def __init__(self, guildMemberDict):
        self.user = guildMemberDict.get("user")
        self.nick = guildMemberDict.get("nick")
        self.roles = guildMemberDict["roles"]
        self.joined_at = guildMemberDict["joined_at"]
        self.premium_since = guildMemberDict.get("premium_since")
        self.deaf = guildMemberDict["deaf"]
        self.mute = guildMemberDict["mute"]
        self.pending = guildMemberDict.get("pending")
        self.permissions = guildMemberDict.get("permissions")

class MessageEmbed:
    def __init__(self, messageEmbedDict=None):
        self.type = messageEmbedDict.get("type", "rich")
        self.title = messageEmbedDict.get("title")
        self.description = messageEmbedDict.get("description")
        self.url = messageEmbedDict.get("url")
        self.timestamp = messageEmbedDict.get("timestamp")
        self.color = messageEmbedDict.get("color")
        self.footer = messageEmbedDict.get("footer", {})
        self.image = messageEmbedDict.get("image", {})
        self.thumbnail = messageEmbedDict.get("thumbnail", {})
        self.video = messageEmbedDict.get("video", {})
        self.author = messageEmbedDict.get("author", {})
        self.fields = messageEmbedDict.get("fields", [])
    def setTitle(self, title):
        self.title = title
        return self
    def setDescription(self, des):
        self.description = des
        return self
    def setUrl(self, url):
        self.url = url
        return self
    def setTimestamp(self, t):
        self.timestamp = t
        return self
    def setColor(self, c):
        self.color = c
        return self
    def setFooter(self, fObj):
        self.footer = fObj
        return self
    def setFooterText(self, txt):
        self.footer["text"] = txt
        return self
    def setFooterIcon(self, url):
        self.footer["icon_url"] = url
        return self
    def setImage(self, url):
        self.image["url"] = url
        return self
    def setThumbnail(self, url):
        self.thumbnail["url"] = url
        return self
    def setVideo(self, url):
        self.video["url"] = url
        return self
    def setAuthor(self, name, url):
        self.author["name"] = name
        self.author["url"] = url
        return self
    def addField(self, name, value, inline):
        field = {
            "name": name,
            "value": value,
            "inline": inline
        }
        self.fields.append(field)
        return self