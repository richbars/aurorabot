import os

import discord
from discord.ext import commands

class Aurora:

    def __init__(self):
        intents = discord.Intents.default()
        intents.guilds = True
        intents.voice_states = True
        intents.messages = True
        intents.message_content = True

        self.client = commands.Bot(command_prefix="@@", intents=intents)

        self.client.add_listener(self.on_ready)

    async def setup_cogs(self):
        cogs_dir = os.path.join(os.path.dirname(__file__), "cogs")
        print("🟩 Cogs Carregados:")
        for file in os.listdir(cogs_dir):
            if file.endswith(".py") and not file.startswith("__"):
                cog_name = file[:-3]
                module_path = f"app.bot.cogs.{cog_name}"
                try:
                    await self.client.load_extension(module_path)
                    print(f"\t- {cog_name}")
                except Exception as e:
                    print(f"❌ Erro ao carregar {module_path}: {e}")

    async def on_ready(self):

        print(f"Bot conectado como {self.client.user}")
        await self.client.change_presence(
            status=discord.Status.dnd,
            activity=discord.Game("Sendo editado pelo @Santosz! 🪛")
        )

        guild = self.client.get_guild(1266145403884273664)
        channel = guild.get_channel(1372249130973270066)
        await channel.connect()


    async def start(self):
        await self.setup_cogs()
        await self.client.start(os.getenv("TOKEN_BOT"))

