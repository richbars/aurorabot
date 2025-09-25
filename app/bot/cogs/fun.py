from discord.ext import commands

class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='ping')
    async def ping(self, ctx):
        print(f"!ping chamado por {ctx.author}")
        await ctx.send("Pong! 🏓")

async def setup(client: commands.bot):
    await client.add_cog(Fun(client))
