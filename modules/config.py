# 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐚𝐧𝐝 𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭𝐬
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# 𝐈𝐧𝐭𝐞𝐫𝐧𝐚𝐥 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 (@𝗜_𝗟𝗢𝗩𝗘_𝗬𝗢𝗨_𝗠𝗬_𝗛𝗘𝗔𝗥𝗧𝗕𝗘𝗘𝗧 @𝗕𝗛𝗥𝗔𝗠𝗔𝗡_𝗔𝗡𝗦𝗛)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 //𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @𝗜_𝗟𝗢𝗩𝗘_𝗬𝗢𝗨_𝗠𝗬_𝗛𝗘𝗔𝗥𝗧𝗕𝗘𝗘𝗧 @𝗕𝗛𝗥𝗔𝗠𝗔𝗡_𝗔𝗡𝗦𝗛
API_HASH = getenv("API_HASH", "XXXXX")
API_ID = int(getenv("API_ID", "XXXXX"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "XXXXX")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "XXXXX")
BOT_IMAGE = getenv("BOT_IMAGE", "https://telegra.ph/file/72fc4ed0b02894736b3b7.jpg")
BOT_NAME = getenv("BOT_NAME", "XXXXX")
BOT_TOKEN = getenv("BOT_TOKEN", "12345:XXXXX")
BOT_USERNAME = getenv("BOT_USERNAME", "XXXXX")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
OWNER_NAME = getenv("OWNER_NAME", "")
OWNER_USERNAME = getenv("OWNER_USERNAME", "I_LOVE_YOU_MY_HEARTBEET")
SOURCE_CODE = getenv("SOURCE_CODE", "https://t.me/SHH_X0X0")
STRING_SESSION = getenv("STRING_SESSION", "session")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1952625698").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/ISHQ00_I")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/XD_CUTETY")

# 𝐃𝐨 𝐍𝐨𝐭 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐞𝐬 // 𝐈𝐠𝐧𝐨𝐫𝐞 𝐓𝐡𝐢𝐬 (𝗔𝗻𝘀𝗵 𝗺𝘂𝘀𝗶𝗰) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/SHH_X0X0")
