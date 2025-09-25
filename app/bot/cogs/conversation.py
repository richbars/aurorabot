from discord.ext import commands
from app.api.services.greq import greq


class Conversation(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.guild is None:
            print(f"Mensagem privada de {message.author}: {message.content}")
            response_greq = greq(message.content)
            await message.channel.send(response_greq)

async def setup(client: commands.Bot):
    await client.add_cog(Conversation(client))
