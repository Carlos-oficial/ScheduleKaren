from db import db as db
import discord

bot = discord.Client()

@bot.event
async def on_ready():
	guild_count = 0

	for guild in bot.guilds:
		print(f"- {guild.id} (name: {guild.name})")
		guild_count = guild_count + 1

	print("SampleDiscordBot is in " + str(guild_count) + " guilds.")

@bot.event
async def on_message(message):
	if message.content == "hello":
		await message.channel.send("hey dirtbag")

bot.run("MTAyNjg1NjE4NjE0ODAzNjY2OQ.GipG7r.i5cM1Mpr-n6WOa-6jQS2haiJ_Iza9SfCAEstRI")