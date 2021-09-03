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

    def send(self, msgJSON):
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

class GuildMember:
    def __init__(self, guildMemberDict):
        if guildMemberDict == None:
            return None
        self.user = guildMemberDict.get("user")
        self.nick = guildMemberDict.get("nick")
        self.roles = guildMemberDict["roles"]
        self.joined_at = guildMemberDict["joined_at"]
        self.premium_since = guildMemberDict.get("premium_since")
        self.deaf = guildMemberDict["deaf"]
        self.mute = guildMemberDict["mute"]
        self.pending = guildMemberDict.get("pending")
        self.permissions = guildMemberDict.get("permissions")