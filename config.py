from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", 32076000))
        self.API_HASH = getenv("API_HASH", "22adb8c3d3f905d09fe41cf4ae805b71")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "9173764504:AAGRt39tiyTaRW1jJOtjhyraKSUfvT-omAU")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://public:yash@cluster0.uchqjbz.mongodb.net/")

        self.LOGGER_ID = int(getenv("LOGGER_ID", -1004423141244))
        self.OWNER_ID = int(getenv("OWNER_ID", 8516736963))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", "AQFRwgAAUcwCn20huFIyCS-IXff2_SXra7cxmQu3Bdy73YiLMfktyi6xttFVtx4pkd4ELf4_2myLCljqZqh2Zc2vhPDKKZgGsazN1km-kLNwNXJOsAPVZt-r01xnS4IDcoYwHA368PChut5h6Jn_61rRpHYJB7e5r417cv_8reba6tsny29UIa0TRhIEmIK7elnFPuYeZU5mWKTZ98plDl1NT9QjENGsyTpwbgHZZmCyEI01-e162WN1j6J-eVuuC4FwvWBc4CoyPQc_-eVptJeiN2tWo1kiMQx2PH6OtzWSuqa6N7sXJNq98RtgTEwig1uWUSV7xSvbUhn_9dPf9mGZhxW-sAAAAAIV40B-AA")
        self.SESSION2 = getenv("SESSION2", None)
        self.SESSION3 = getenv("SESSION3", None)

        self.SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/mizuu_update")
        self.SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/vistoriyachat")

        self.AUTO_LEAVE: bool = getenv("AUTO_LEAVE", "False").lower() == "true"
        self.AUTO_END: bool = getenv("AUTO_END", "False").lower() == "true"

        self.THUMB_GEN: bool = getenv("THUMB_GEN", "True").lower() == "true"
        self.VIDEO_PLAY: bool = getenv("VIDEO_PLAY", "True").lower() == "true"

        self.LANG_CODE = getenv("LANG_CODE", "en")

        self.COOKIES_URL = [
            url for url in getenv("COOKIES_URL", "https://batbin.me/deejay").split(" ")
            if url and "batbin.me" in url
        ]
        self.DEFAULT_THUMB = getenv("DEFAULT_THUMB", "https://te.legra.ph/file/3e40a408286d4eda24191.jpg")
        self.PING_IMG = getenv("PING_IMG", "https://files.catbox.moe/haagg2.png")
        self.START_IMG = getenv("START_IMG", "https://files.catbox.moe/zvziwk.jpg")

    def check(self):
        missing = [
            var
            for var in ["API_ID", "API_HASH", "BOT_TOKEN", "MONGO_URL", "LOGGER_ID", "OWNER_ID", "SESSION1"]
            if not getattr(self, var)
        ]
        if missing:
            raise SystemExit(f"Missing required environment variables: {', '.join(missing)}")
