from progress.spinner import PieSpinner
from telethon import TelegramClient
from dotenv import load_dotenv
import os

load_dotenv()
client = TelegramClient("Something", os.getenv("API_KEY"), os.getenv("API_HASH"))


def create_folder(path: str, name: str) -> str:
    try:
        os.mkdir(f"{path}/{name}")
    except FileExistsError as e:
        pass

    return "/" + name


async def main(chat_id: str, save_to: str):
    save_to += create_folder(save_to, chat_id)
    spinner = PieSpinner(f"Downloading from {chat_id} ")

    async for message in client.iter_messages(int(chat_id)):
        if message.photo or message.video or message.voice:
            await message.download_media(file=save_to)
        spinner.next()


if __name__ == "__main__":
    chats = []

    writing = True
    while writing:
        user_input = str(input("Enter chat id (for exit type: /done): "))
        if user_input.strip(" ") != "/done":
            chats.append(user_input)
        else:
            writing = False

    for chat in chats:
        with client:
            client.loop.run_until_complete(main(chat, os.getenv("OUTPUT_FOLDER")))
