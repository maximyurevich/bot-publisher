"""Main file"""
from aiogram.utils import executor
from bot_broadcaster import write_message_to_channel, dp


async def main():
    """Main function"""
    await write_message_to_channel(
        image_url="https://www.dropbox.com/s/2k6k4ugh3f3qmca/590px-Test_ttp_big.jpg?dl=0",
        title="Lorep ipsum",
        description="Lorem ipsum dolor sit amet, consectetur adipiscing elit",
        author="Maxim Yurevich",
        url="https://www.dropbox.com/",
        hashtags="#Lorem #Ipsum"
    )

if __name__ == "__main__":
    executor.start(dp, main())
