from telethon import TelegramClient
import os
from dotenv import load_dotenv

load_dotenv()
client = TelegramClient("Something", os.getenv("API_KEY"), os.getenv("API_HASH"))

async def main():

    async for message in client.iter_messages(os.getenv("SUPER_DUPER_IMPORTANT_CHAT_ID")):
        if message.photo or message.video or message.voice:
            path = await message.download_media()
            print('File saved to', path)

with client:
    client.loop.run_until_complete(main())
    