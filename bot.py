# =========================================================
# 𝐅𝐈𝐋𝐄 : bot.py
# =========================================================

import os
import json
import asyncio
from pyrogram.enums import ChatMemberStatus
from pyrogram import Client, filters
from pyrogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# =========================================================
# 𝐂𝐎𝐍𝐅𝐈𝐆
# =========================================================

API_ID =  37501751
API_HASH = "795ac6fbfd091e3ded2475e4671f0ad0"
BOT_TOKEN = "8778554352:AAF-Q6zYJb69CEdpiy7qqIfdIHWfiJlKJUw"

FORCE_CHANNEL = "ethtical_zone"
CHANNEL_LINK = "https://t.me/ethtical_zone"

# =========================================================
# 𝐁𝐎𝐓
# =========================================================

app = Client(
    "FileIDBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# =========================================================
# 𝐃𝐀𝐓𝐀𝐁𝐀𝐒𝐄
# =========================================================

DB_FILE = "data.json"

if not os.path.exists(DB_FILE):
    with open(DB_FILE, "w") as f:
        json.dump({"users": []}, f)


def load_db():
    with open(DB_FILE, "r") as f:
        return json.load(f)


def save_db(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_user(user_id):
    data = load_db()

    if user_id not in data["users"]:
        data["users"].append(user_id)
        save_db(data)

# =========================================================
# 𝐒𝐓𝐈𝐂𝐊𝐄𝐑𝐒
# =========================================================

LOADING = "CAACAgUAAxkBAAMRahl6Vbc-FvIHBZ3eIjMih35Wy0gAAhkIAAJPJMlWDSb5dCNGS8keBA"

UPLOADING = "CAACAgUAAxkBAAMTahl8MFRvge59GduHf3-Enor6jT0AAogZAAJIwzlWe68FqOo9XRweBA"

WELCOME = "CAACAgQAAxkBAAMVahl8X1W22oiVbpzxHjt-0ZR-LVwAAroVAAIjpEBTbuJ0Eo9PHgceBA"

VERIFIED = "CAACAgUAAxkBAAMXahl8h44V-194KzZZJ0cUhmFB7nQAAicTAAKmqVhWBj1qFITYbUAeBA"

DENIED = "CAACAgQAAxkBAAMZahl8khLaCnazGQiOlygjNOtKEIwAAscEAAI3DX4Zus3JKEmqtAQeBA"

COMPLETED = "CAACAgQAAxkBAAMbahl9M1i8zsWzkMau3FPNErdBD7MAAjAMAALCFSBS8V5yspo5PY8eBA"

# =========================================================
# 𝐊𝐄𝐘𝐁𝐎𝐀𝐑𝐃
# =========================================================

main_keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("🎭 𝐒𝐭𝐢𝐜𝐤𝐞𝐫 𝐈𝐃"),
            KeyboardButton("🖼 𝐏𝐡𝐨𝐭𝐨 𝐈𝐃")
        ],
        [
            KeyboardButton("🎥 𝐕𝐢𝐝𝐞𝐨 𝐈𝐃"),
            KeyboardButton("🎞 𝐆𝐈𝐅 𝐈𝐃")
        ],
        [
            KeyboardButton("✨ 𝐀𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧"),
            KeyboardButton("😂 𝐄𝐦𝐨𝐣𝐢 𝐈𝐃")
        ],
        [
            KeyboardButton("💬 𝐂𝐡𝐚𝐭 𝐈𝐃"),
            KeyboardButton("🤖 𝐁𝐨𝐭 𝐈𝐃")
        ]
    ],
    resize_keyboard=True
)

back_keyboard = ReplyKeyboardMarkup(
    [
        [KeyboardButton("🔙 𝐁𝐚𝐜𝐤")]
    ],
    resize_keyboard=True
)

# =========================================================
# 𝐇𝐄𝐋𝐏𝐄𝐑
# =========================================================

async def auto_delete_sticker(msg):
    await asyncio.sleep(1.5)
    try:
        await msg.delete()
    except:
        pass


async def send_temp_sticker(message, sticker_id):
    x = await message.reply_sticker(sticker_id)
    asyncio.create_task(auto_delete_sticker(x))


# =========================================================
# 𝐅𝐎𝐑𝐂𝐄 𝐉𝐎𝐈𝐍
# =========================================================

from pyrogram.enums import ChatMemberStatus

async def joined(user_id):
    try:
        member = await app.get_chat_member(
            chat_id=f"@{FORCE_CHANNEL}",
            user_id=user_id
        )

        print(member)

        return member.status in [
            ChatMemberStatus.MEMBER,
            ChatMemberStatus.ADMINISTRATOR,
            ChatMemberStatus.OWNER
        ]

    except Exception as e:
        print(f"JOIN CHECK ERROR : {e}")
        return False

# =========================================================
# 𝐒𝐓𝐀𝐑𝐓
# =========================================================

@app.on_message(filters.command("start") & filters.private)
async def start(_, message):

    add_user(message.from_user.id)

    await send_temp_sticker(message, WELCOME)

    check = await joined(message.from_user.id)

    if not check:

        await send_temp_sticker(message, DENIED)

        return await message.reply_text(
            text="""
╭━━━〔 ⚠️ 𝐉𝐎𝐈𝐍 𝐑𝐄𝐐𝐔𝐈𝐑𝐄𝐃 ⚠️ 〕━━━╮

✨ 𝐓𝐎 𝐔𝐒𝐄 𝐓𝐇𝐈𝐒 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐅𝐈𝐋𝐄 𝐈𝐃 𝐁𝐎𝐓,
𝐉𝐎𝐈𝐍 𝐎𝐔𝐑 𝐎𝐅𝐅𝐈𝐂𝐈𝐀𝐋 𝐂𝐇𝐀𝐍𝐍𝐄𝐋.

📢 𝐀𝐅𝐓𝐄𝐑 𝐉𝐎𝐈𝐍𝐈𝐍𝐆 𝐂𝐋𝐈𝐂𝐊
✅ 𝐕𝐄𝐑𝐈𝐅𝐘 𝐍𝐎𝐖

╰━━━━━━━━━━━━━━━━━━━╯
""",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "📢 𝐉𝐎𝐈𝐍 𝐂𝐇𝐀𝐍𝐍𝐄𝐋",
                            url=CHANNEL_LINK
                        )
                    ],
                    [
                        InlineKeyboardButton(
                            "✅ 𝐕𝐄𝐑𝐈𝐅𝐘 𝐍𝐎𝐖",
                            callback_data="verify"
                        )
                    ]
                ]
            )
        )

    load = await message.reply_sticker(LOADING)
    await asyncio.sleep(1.5)
    await load.delete()

    await message.reply_text(
        f"""
╭━━━〔 👋 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 〕━━━╮

✨ 𝐏𝐑𝐄𝐌𝐈𝐔𝐌 𝐅𝐈𝐋𝐄 𝐈𝐃 𝐄𝐗𝐓𝐑𝐀𝐂𝐓𝐎𝐑

📩 𝐒𝐄𝐍𝐃 𝐀𝐍𝐘 𝐒𝐓𝐈𝐂𝐊𝐄𝐑 • 𝐆𝐈𝐅 •
𝐏𝐇𝐎𝐓𝐎 • 𝐕𝐈𝐃𝐄𝐎 • 𝐄𝐌𝐎𝐉𝐈

👤 𝐔𝐒𝐄𝐑 : {message.from_user.first_name}

🚀 𝐅𝐀𝐒𝐓 • 𝐂𝐋𝐄𝐀𝐍 • 𝐏𝐑𝐄𝐌𝐈𝐔𝐌

╰━━━━━━━━━━━━━━━━━━━╯
""",
        reply_markup=main_keyboard
    )

# =========================================================
# 𝐕𝐄𝐑𝐈𝐅𝐘
# =========================================================

@app.on_callback_query(filters.regex("verify"))
async def verify(_, query):

    ok = await joined(query.from_user.id)

    if not ok:
        await send_temp_sticker(query.message, DENIED)

        return await query.answer(
            "Join Channel First",
            show_alert=True
        )

    await send_temp_sticker(query.message, VERIFIED)

    await query.message.reply_text(
        """
╭━━━〔 ✅ 𝐕𝐄𝐑𝐈𝐅𝐈𝐄𝐃 〕━━━╮

✨ 𝐂𝐇𝐀𝐍𝐍𝐄𝐋 𝐕𝐄𝐑𝐈𝐅𝐈𝐄𝐃

🚀 𝐍𝐎𝐖 𝐘𝐎𝐔 𝐂𝐀𝐍 𝐔𝐒𝐄
𝐀𝐋𝐋 𝐁𝐎𝐓 𝐅𝐄𝐀𝐓𝐔𝐑𝐄𝐒

╰━━━━━━━━━━━━━━━━━━━╯
""",
        reply_markup=main_keyboard
    )

# =========================================================
# 𝐌𝐄𝐍𝐔 𝐁𝐔𝐓𝐓𝐎𝐍𝐒
# =========================================================

buttons = [
    "🎭 𝐒𝐭𝐢𝐜𝐤𝐞𝐫 𝐈𝐃",
    "🖼 𝐏𝐡𝐨𝐭𝐨 𝐈𝐃",
    "🎥 𝐕𝐢𝐝𝐞𝐨 𝐈𝐃",
    "🎞 𝐆𝐈𝐅 𝐈𝐃",
    "✨ 𝐀𝐧𝐢𝐦𝐚𝐭𝐢𝐨𝐧",
    "😂 𝐄𝐦𝐨𝐣𝐢 𝐈𝐃",
    "💬 𝐂𝐡𝐚𝐭 𝐈𝐃",
    "🤖 𝐁𝐨𝐭 𝐈𝐃"
]

# =========================================================
# 𝐌𝐄𝐍𝐔 𝐇𝐀𝐍𝐃𝐋𝐄𝐑
# =========================================================

@app.on_message(filters.text & filters.private)
async def menu(_, message):

    if message.text.startswith("/"):
        return

    if message.text == "🔙 𝐁𝐚𝐜𝐤":

        load = await message.reply_sticker(LOADING)
        await asyncio.sleep(1.5)
        await load.delete()

        return await message.reply_text(
            """
╭━━━〔 🏠 𝐌𝐀𝐈𝐍 𝐌𝐄𝐍𝐔 〕━━━╮

✨ 𝐒𝐄𝐋𝐄𝐂𝐓 𝐀𝐍𝐘 𝐎𝐏𝐓𝐈𝐎𝐍
𝐅𝐑𝐎𝐌 𝐓𝐇𝐄 𝐊𝐄𝐘𝐁𝐎𝐀𝐑𝐃

╰━━━━━━━━━━━━━━━━━━━╯
""",
            reply_markup=main_keyboard
        )

    if message.text in buttons:

        load = await message.reply_sticker(LOADING)
        await asyncio.sleep(1.5)
        await load.delete()

        return await message.reply_text(
            f"""
╭━━━〔 ✨ 𝐒𝐄𝐂𝐓𝐈𝐎𝐍 〕━━━╮

{message.text}

📩 𝐍𝐎𝐖 𝐒𝐄𝐍𝐃 𝐘𝐎𝐔𝐑 𝐌𝐄𝐃𝐈𝐀

🚀 𝐅𝐀𝐒𝐓 • 𝐂𝐋𝐄𝐀𝐍 • 𝐏𝐑𝐄𝐌𝐈𝐔𝐌

╰━━━━━━━━━━━━━━━━━━━╯
""",
            reply_markup=back_keyboard
        )

        return

# =========================================================
# 𝐒𝐓𝐈𝐂𝐊𝐄𝐑
# =========================================================

@app.on_message(filters.sticker & filters.private)
async def sticker_handler(_, message):

    user = message.from_user

    upload = await message.reply_sticker(UPLOADING)
    await asyncio.sleep(1.5)
    await upload.delete()

    file_id = message.sticker.file_id

    await message.reply_text(
        f"""
╭━━━〔 🎭 𝐒𝐓𝐈𝐂𝐊𝐄𝐑 𝐈𝐃 〕━━━╮

🆔 𝐅𝐈𝐋𝐄 𝐈𝐃
━━━━━━━━━━━━
`{file_id}`

📂 𝐓𝐘𝐏𝐄 : Sticker
📦 𝐀𝐧𝐢𝐦𝐚𝐭𝐞𝐝 𝐒𝐭𝐢𝐜𝐤𝐞𝐫

╭─❍
│ 𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨
╰───────────
👤 {user.first_name}
🪪 `{user.id}`

╰━━━━━━━━━━━━━━━━━━━╯
"""
    )

    await send_temp_sticker(message, COMPLETED)

# =========================================================
# 𝐏𝐇𝐎𝐓𝐎
# =========================================================

@app.on_message(filters.photo & filters.private)
async def photo_handler(_, message):

    user = message.from_user

    upload = await message.reply_sticker(UPLOADING)
    await asyncio.sleep(1.5)
    await upload.delete()

    file_id = message.photo.file_id

    await message.reply_text(
        f"""
╭━━━〔 🖼 𝐏𝐇𝐎𝐓𝐎 𝐈𝐃 〕━━━╮

🆔 𝐅𝐈𝐋𝐄 𝐈𝐃
━━━━━━━━━━━━
`{file_id}`

📂 𝐓𝐘𝐏𝐄 : Photo

╭─❍
│ 𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨
╰───────────
👤 {user.first_name}
🪪 `{user.id}`

╰━━━━━━━━━━━━━━━━━━━╯
"""
    )

    await send_temp_sticker(message, COMPLETED)

# =========================================================
# 𝐕𝐈𝐃𝐄𝐎
# =========================================================

@app.on_message(filters.video & filters.private)
async def video_handler(_, message):

    user = message.from_user

    upload = await message.reply_sticker(UPLOADING)
    await asyncio.sleep(1.5)
    await upload.delete()

    file_id = message.video.file_id

    await message.reply_text(
        f"""
╭━━━〔 🎥 𝐕𝐈𝐃𝐄𝐎 𝐈𝐃 〕━━━╮

🆔 𝐅𝐈𝐋𝐄 𝐈𝐃
━━━━━━━━━━━━
`{file_id}`

📂 𝐓𝐘𝐏𝐄 : Video

╭─❍
│ 𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨
╰───────────
👤 {user.first_name}
🪪 `{user.id}`

╰━━━━━━━━━━━━━━━━━━━╯
"""
    )

    await send_temp_sticker(message, COMPLETED)

# =========================================================
# 𝐆𝐈𝐅 / 𝐀𝐍𝐈𝐌𝐀𝐓𝐈𝐎𝐍
# =========================================================

@app.on_message(filters.animation & filters.private)
async def animation_handler(_, message):

    user = message.from_user

    upload = await message.reply_sticker(UPLOADING)
    await asyncio.sleep(1.5)
    await upload.delete()

    file_id = message.animation.file_id

    await message.reply_text(
        f"""
╭━━━〔 🎞 𝐆𝐈𝐅 𝐈𝐃 〕━━━╮

🆔 𝐅𝐈𝐋𝐄 𝐈𝐃
━━━━━━━━━━━━
`{file_id}`

📂 𝐓𝐘𝐏𝐄 : GIF / Animation

╭─❍
│ 𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨
╰───────────
👤 {user.first_name}
🪪 `{user.id}`

╰━━━━━━━━━━━━━━━━━━━╯
"""
    )

    await send_temp_sticker(message, COMPLETED)

# =========================================================
# 𝐄𝐌𝐎𝐉𝐈
# =========================================================

@app.on_message(filters.text & filters.private)
async def emoji_handler(_, message):

    if message.text.startswith("/"):
        return

    if message.text in buttons:
        return

    if message.text == "🔙 𝐁𝐚𝐜𝐤":
        return

    if len(message.text) <= 3:

        user = message.from_user

        upload = await message.reply_sticker(UPLOADING)
        await asyncio.sleep(1.5)
        await upload.delete()

        await message.reply_text(
            f"""
╭━━━〔 😂 𝐄𝐌𝐎𝐉𝐈 〕━━━╮

😂 𝐄𝐌𝐎𝐉𝐈 : {message.text}

╭─❍
│ 𝐔𝐬𝐞𝐫 𝐈𝐧𝐟𝐨
╰───────────
👤 {user.first_name}
🪪 `{user.id}`

╰━━━━━━━━━━━━━━━━━━━╯
"""
        )

        return await send_temp_sticker(message, COMPLETED)

# =========================================================
# 𝐂𝐇𝐀𝐓 𝐈𝐃
# =========================================================

@app.on_message(filters.command("chatid") & filters.private)
async def chatid(_, message):

    await message.reply_text(
        f"""
╭━━━〔 💬 𝐂𝐇𝐀𝐓 𝐈𝐃 〕━━━╮

🆔 `{message.chat.id}`

╰━━━━━━━━━━━━━━━━━━━╯
"""
    )

# =========================================================
# 𝐁𝐎𝐓 𝐈𝐃
# =========================================================

@app.on_message(filters.command("botid") & filters.private)
async def botid(_, message):

    me = await app.get_me()

    await message.reply_text(
        f"""
╭━━━〔 🤖 𝐁𝐎𝐓 𝐈𝐃 〕━━━╮

🆔 `{me.id}`

╰━━━━━━━━━━━━━━━━━━━╯
"""
    )

# =========================================================
# 𝐔𝐍𝐒𝐔𝐏𝐏𝐎𝐑𝐓𝐄𝐃
# =========================================================

@app.on_message(filters.private)
async def unsupported(_, message):

    if message.text:
        return

    await send_temp_sticker(message, DENIED)

    await message.reply_text(
        """
╭━━━〔 ❌ 𝐔𝐍𝐒𝐔𝐏𝐏𝐎𝐑𝐓𝐄𝐃 〕━━━╮

⚠️ 𝐓𝐇𝐈𝐒 𝐌𝐄𝐃𝐈𝐀 𝐈𝐒
𝐍𝐎𝐓 𝐒𝐔𝐏𝐏𝐎𝐑𝐓𝐄𝐃

📩 𝐒𝐄𝐍𝐃 𝐀 𝐕𝐀𝐋𝐈𝐃
𝐒𝐓𝐈𝐂𝐊𝐄𝐑 • 𝐏𝐇𝐎𝐓𝐎 •
𝐕𝐈𝐃𝐄𝐎 • 𝐆𝐈𝐅 • 𝐄𝐌𝐎𝐉𝐈

╰━━━━━━━━━━━━━━━━━━━╯
""",
        reply_markup=back_keyboard
    )

# =========================================================
# 𝐑𝐔𝐍
# ==================================================

print("🚀 BOT IS RUNNING...")

try:
    app.run()
except Exception as e:
    import traceback
    traceback.print_exc()
    print(e)
