import os
import discord
from dotenv import load_dotenv

# Carrega as variáveis do .env
load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
CHANNEL_COMMAND = int(os.getenv("CHANNEL_COMMAND"))

# Configura as intents
intents = discord.Intents.default()
intents.message_content = True  # Necessário para ler mensagens

# Cria o cliente
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")

    # Obtém o canal
    channel = client.get_channel(CHANNEL_COMMAND)

    # Caso não esteja em cache, busca pela API
    if channel is None:
        channel = await client.fetch_channel(CHANNEL_COMMAND)

    # Envia a mensagem
    await channel.send("Hello World!")

@client.event
async def on_message(message):
    # Ignora mensagens do próprio bot
    if message.author == client.user:
        return

    # Responde apenas no canal configurado
    #if message.channel.id != CHANNEL_COMMAND:
    #    return

    # Comando !modbot
    if message.content.strip().lower() == "!modbot":
        #await message.channel.send("Estou online")
        await message.reply("Estou online")

    # Comando !modbot tudo bem?
    if message.content.strip().lower() == "!modbot tudo bem?":
        await message.reply("Tudo bem! Estou funcionando, e você, está bem?")
        #await message.channel.send(
        #    f"Tudo bem, {message.author.mention}! Estou funcionando, e você, está bem?"
        #)

    # Comando !modbot tudo bem?
    if message.content.strip().lower() == "!modbot qual é o seu propósito?":
        await message.reply("Serei o novo moderador de spams daqui :saluting_face:")

# Inicia o bot
client.run(DISCORD_TOKEN)