import discord
import os

# Your Discord bot token
TOKEN = os.environ.get('DISCORD_TOKEN')
CHANNEL_ID = int(os.environ.get('DISCORD_CHANNEL_ID'))

class Client(discord.Client):
	def __init__(self, audio_path):
		intents = discord.Intents.default()

		super().__init__(intents=intents)
		self.audio_path = audio_path

	async def on_ready(self):
		print('Logged in as')
		print(f'{self.user.name=}')
		print(f'{self.user.id=}')
		print('------')

		# Get the channel where you want to send the MP3
		# Replace 'channel_id_here' with the actual ID of the channel
		channel = self.get_channel(CHANNEL_ID)
		if channel:
				print('found channel', channel)
				await channel.send('hi all! here\'s the news')
				# Send the fixed MP3 file to the channel
				with open(self.audio_path, 'rb') as f:
						await channel.send(file=discord.File(f, self.audio_path))
		else:
			print('channel not found')

		# this doesn't seem to work, but at least the client terminates.?
		await self.close()

def send_audio(audio_path):
	client = Client(audio_path)
	client.run(TOKEN)


