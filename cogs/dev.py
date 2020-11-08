import discord
import datetime

from discord.ext import commands

class dev(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

	@commands.command(alias=["r", "reload"])
	@commands.is_owner()
	async def restart(self, ctx, cog):
		message = await ctx.send(f"Restarting ``{cog}``...")
		self.bot.unload_extension(f"cogs.{cog}")
		self.bot.load_extension(f"cogs.{cog}")
		await message.edit(content=f"Restarted ``{cog}``.")

def setup(bot):
	bot.add_cog(dev(bot))

