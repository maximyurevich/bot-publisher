"""Bot broadcaster"""
import logging
from typing import Optional
from string import Template
from textwrap import dedent
from aiogram import Bot, Dispatcher, types
from dotenv.main import dotenv_values


logging.basicConfig(level=logging.INFO)

config = dotenv_values(".env")

API_TOKEN = config["API_TOKEN"]
CHANNEL = config["CHANNEL"]

if API_TOKEN and CHANNEL is not None:
    channel_id = int(CHANNEL)
    bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
    dp = Dispatcher(bot)

    async def write_message_to_channel(
        *,
        image_url: Optional[str],
        title: Optional[str],
        description: Optional[str] = None,
        url: Optional[str],
        author: Optional[str],
        ):
        """Write message to channel

        Args:
            img_url (str): Message image url
            caption (str): Message caption
        """

        data: dict[str, Optional[str]] = {
            "title": title,
            "description": description,
            "image_url": image_url,
            "author": author,
            "url": url,
        }

        message = Template(dedent("""
        <b>$title</b>
        $description
        <b><a href=\"$url\">More</a></b>
        <i>$author</i>
        """))

        await bot.send_photo(
            channel_id,
            data["image_url"],
            caption=message.substitute(data)
        )
