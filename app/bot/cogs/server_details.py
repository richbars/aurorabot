from discord.ext import commands
import discord

class Server(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="server_details", aliases=["sd"])
    async def server_details(self, ctx):
        guild = ctx.guild
        if guild is None:
            await ctx.send("Não consegui pegar informações do servidor!")
            return

        embed = discord.Embed(
            title=f"Informações do Servidor: {guild.name}",
            description=f"ID: {guild.id}",
            color=discord.Color.blue()
        )
        embed.set_thumbnail(url=guild.icon.url if guild.icon else "")
        embed.add_field(name="Membros", value=guild.member_count)
        embed.add_field(name="Canais", value=len(guild.channels))
        embed.add_field(name="Criado em", value=guild.created_at.strftime("%d/%m/%Y %H:%M"))

        await ctx.send(embed=embed)

async def setup(bot: commands.Bot):
    await bot.add_cog(Server(bot))
