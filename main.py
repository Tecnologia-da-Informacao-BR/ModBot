import os
import discord
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_COMMAND = int(os.getenv("CHANNEL_COMMAND"))

# Configure Discord intents
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

# Create the Discord client
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    # Get the configured channel from the cache
    channel = client.get_channel(CHANNEL_COMMAND)

    # If the channel is not cached, fetch it from the Discord API
    if channel is None:
        channel = await client.fetch_channel(CHANNEL_COMMAND)

    # Send the startup message
    await channel.send("Hello World!")

@client.event
async def on_message(message):
    # Ignore messages sent by the bot itself
    if message.author == client.user:
        return

    # Respond only in the configured channel
    # if message.channel.id != CHANNEL_COMMAND:
    #     return

    # !modbot command
    if message.content.strip().lower() == "!modbot":
        # await message.channel.send("Estou online")
        await message.reply("Estou online")

    # !modbot tudo bem? command
    if message.content.strip().lower() == "!modbot tudo bem?":
        await message.reply("Tudo bem! Estou funcionando, e você, está bem?")
        # await message.channel.send(
        #     f"Tudo bem, {message.author.mention}! Estou funcionando, e você, está bem?"
        # )

    # !modbot qual é o seu propósito? command
    if message.content.strip().lower() == "!modbot qual é o seu propósito?":
        await message.reply("Serei o novo moderador de spams daqui :saluting_face:")

# Start the bot
client.run(DISCORD_TOKEN)