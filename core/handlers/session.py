from pyrogram import Client, filters
from pyrogram.types import Message
import asyncio

from ..helpers.session import main as generate_session


async def session_command(client: Client, message: Message):
    await message.reply_text(
        "⏳ Session string yaratilmoqda...\n"
        "Render'da bu buyruq ishlamaydi.\n"
        "Session stringni lokal kompyuter yoki Termuxda yaratish kerak."
    )

    try:
        await asyncio.to_thread(lambda: asyncio.run(generate_session()))
    except Exception as e:
        await message.reply_text(f"❌ Xatolik:\n{e}")
