from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.API_ID = int(getenv("API_ID", 32076000))
        self.API_HASH = getenv("API_HASH", "22adb8c3d3f905d09fe41cf4ae805b71")

        self.BOT_TOKEN = getenv("BOT_TOKEN", "9173764504:AAGRt39tiyTaRW1jJOtjhyraKSUfvT-omAU")
        self.MONGO_URL = getenv("MONGO_URL", "mongodb+srv://Yash:80571457Ya@cluster0.pgtxsro.mongodb.net/")

        self.LOGGER_ID = int(getenv("LOGGER_ID", -1004423141244))
        self.OWNER_ID = int(getenv("OWNER_ID", 8516736963))

        self.DURATION_LIMIT = int(getenv("DURATION_LIMIT", 60)) * 60
        self.QUEUE_LIMIT = int(getenv("QUEUE_LIMIT", 20))
        self.PLAYLIST_LIMIT = int(getenv("PLAYLIST_LIMIT", 20))

        self.SESSION1 = getenv("SESSION", "AQFRwgAAeslA5lD6moL5N7tOIzOKKf2bjUWgWCDJwAV9ijo11zJih7xtOn-jBjEJfkjTCyXpK7jJwQD3JcT6wYV_uUNoET4ZY3WPSyq3f8kzJ755FSwBFNW-sOqGBvJ6MfB_KC0mvKX_llju1uLhUrgWJw7Sid5OXp31psWbtyyxMBK142NCQ5DQXadUDiSwJCgBM8oq3KDfqh33FN2R4uu0SCoSXbOHhlb7J0BWhABuuFgz0XZurwqDVXZPsqcorvOpLrzLF6Oz4pbsWmdn8tSc_p8xP8A8XvjM0-Kbra1QYYKTzj5Vd0iliCI54HsmXtky9pRjCFlLfBnsDJfqAh77fe_0ngAAAAIV40B-AA")
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
