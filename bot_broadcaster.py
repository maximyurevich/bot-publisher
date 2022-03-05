"""Bot broadcaster"""
import logging
import os
import sys
from typing import Optional
from string import Template
from textwrap import dedent
from aiogram import Bot, Dispatcher, types, executor
from dotenv.main import dotenv_values


logging.basicConfig(level=logging.INFO)


config = dotenv_values(os.environ["ENVPATH"])


API_TOKEN = config["API_TOKEN"]
CHANNEL = config["CHANNEL"]


try:
    if API_TOKEN is None or CHANNEL is None:
        raise ValueError("API_TOKEN or CHANNEL is not defined")
except ValueError as e:
    logging.error(e)
    sys.exit(1)


bot = Bot(token=API_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot)


async def write_message_to_channel(
    *,
    image_url: Optional[str],
    title: Optional[str],
    description: Optional[str],
    url: Optional[str],
    hashtags: Optional[str]
    ):
    """Write message to channel

    Args:
        img_url (str): Message image url
        caption (str): Message caption
    """

    message_data: dict[str, Optional[str]] = {
        "title": title,
        "description": description,
        "image_url": image_url,
        "url": url,
        "hashtags": hashtags
    }

    message = Template(dedent("""
    <b>$title</b>

    $description

    👉 <b><a href=\"$url\">Подробнее</a></b>
    
    $hashtags"""))

    await bot.send_photo(
        CHANNEL,
        message_data["image_url"],
        caption=message.substitute(message_data)
    )

async def main():
    """Main function"""
    await write_message_to_channel(
        image_url="https://www.dropbox.com/s/2k6k4ugh3f3qmca/590px-Test_ttp_big.jpg?dl=0",
        title="Lorem ipsum",
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        url="https://www.dropbox.com/",
        hashtags="#Lorem #Ipsum"
    )

if __name__ == "__main__":
    executor.start(dp, main())
