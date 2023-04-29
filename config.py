from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/232c3ca139605681dce4e.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/91c7806b38e7b149f5c10.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/indian_chatting_club_offical")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/shayari_ka_tadka")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1356469075").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"