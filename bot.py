import discord
import random
import datetime
from discord.ext import commands

client = commands.Bot(command_prefix = ">")

@client.event
async def on_ready():
	print("RDY")

@client.command(aliases=["kula", "8ball"])
async def _8ball(ctx, *, question):
	responses = ["Jak chuj.",
				 "Jest możliwe.",
				 "Jak najbardziej, jeszcze jak!",
				 "Nie ma opcji.",
				 "Nie zrozumiałem pytania.",
				 "W żadnym wypadku.",
				 "Tak.",
				 "Nomć.",
				 "Prawdopodobnie.",
				 "Jest na to szansa.",
				 "Nie, skądże!",
				 "Absolutnie nie.",
				 "Nigdy.",
				 "Nawet nie licz.",
				 "Wszystko wskazuje na to że tak.",
				 "Szczerze wątpię.",
				 "Haha, dobre żarty!",
				 "Niemożliwe.",
				 "Nie.",
				 "Bardzo mała szansa."]
	embed=discord.Embed()
	embed.add_field(name=f"Pytanie: {question}", value=f"Odpowiedź: {random.choice(responses)}", inline=False)
	await ctx.send(embed=embed)

@client.command()
async def staty(ctx):
	file=open("stat.txt")


@client.command()
async def q(ctx):
	await ctx.send("#z graspikiem es B)")

cogs = {
	'cogs.dev', 'cogs.mod'
}

if __name__ == "__main__":
	for cog in cogs:
		client.load_extension(cog)
		print(f"{cog} has been sucessfully loaded.")

with open("xrckwo.0", "r", encoding="utf-8") as f:
	bottoken = f.read()


client.run(bottoken)