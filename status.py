import discord # Discord module (external)
import requests # HTTP request module (internal)
import json # JSON parsing module (internal)
import datetime # Date+time parsing module (internal)
from time import sleep # time parsing module (internal)

ServerAddress="http://localhost" # Address of server
ChannelID=709801509210030160 # ID of channel to output
ChannelObject=None # Object of channel from ID above
ActiveMessageObject=None # Temporary value of current message object
BotToken="" # Bot's token

class MyClient(discord.Client):
	async def on_ready(self): # when bot initialised
		print('I am running as {0}'.format(self.user)) # output running alias
		ChannelObject=await self.fetch_channel(ChannelID) # get object of channel
		await ChannelObject.send("Clearing...")
		sleep(2) # Wait 2 seconds
		await ChannelObject.purge() # clear all messages in channel
		while True:
			"""
			try/except is used for error handling. If an error is thrown in the try block, it runs the except function as a failback
			in this case, if the try clause throws an error, we can assume the server is offline

			timeout: value in seconds, if no data is recieved within 2 seconds, the connection has failed
			verify: if I recall correctly it's SSL verification. It's a localhost server, so no worries disabling it.
			.json(): coverts the json array into a Python array. Combined with len() gets the number of players in players.json
			"""
			
			try:
				statusLS1=":green_circle: "+str(len(requests.get(ServerAddress+":30120/players.json", timeout=2, verify=False).json()))+"/32 players"+" <:pepecool:666781477224054814>"+"\n\nFind me on the FiveM server listings!\nDirect connect via: `54.37.245.85:30120`"
			except:
				statusLS1=":red_circle: No response <:pepesad:666781477236768768>\n\n I'm probably just offline"
			try:
				statusLS2=":green_circle: "+str(len(requests.get(ServerAddress+":30122/players.json", timeout=2, verify=False).json()))+"/32 players"+" <:pepecool:666781477224054814>"+"\n\nFind me on the FiveM server listings!\nDirect connect via: `54.37.245.85:30122`"
			except:
				statusLS2=":red_circle: No response <:pepesad:666781477236768768>\n\n I'm probably just offline"
			try:
				statusLS3=":green_circle: "+str(len(requests.get(ServerAddress+":30124/players.json", timeout=2, verify=False).json()))+"/32 players"+" <:pepecool:666781477224054814>"+"\n\nFind me on the FiveM server listings!\nDirect connect via: `54.37.245.85:30124`"
			except:
				statusLS3=":red_circle: No response <:pepesad:666781477236768768>\n\n I'm probably just offline"
			try:
				statusLS4=":green_circle: "+str(len(requests.get(ServerAddress+":30126/players.json", timeout=2, verify=False).json()))+"/32 players"+" <:pepecool:666781477224054814>"+"\n\nFind me on the FiveM server listings!\nDirect connect via: `54.37.245.85:30126`"
			except:
				statusLS4=":red_circle: No response <:pepesad:666781477236768768>\n\n I'm probably just offline"

			try:
				statusTR1=":green_circle: "+str(len(requests.get(ServerAddress+":30121/players.json", timeout=2, verify=False).json()))+"/32 players"+" <:pepecool:666781477224054814>"+"\n\nFind me on the FiveM server listings!\nDirect connect via: `54.37.245.85:30121`"
			except:
				statusTR1=":red_circle: No response <:pepesad:666781477236768768>\n\n I'm probably just offline"
			try:
				statusTR2=":green_circle: "+str(len(requests.get(ServerAddress+":30123/players.json", timeout=2, verify=False).json()))+"/32 players"+" <:pepecool:666781477224054814>"+"\n\nFind me on the FiveM server listings!\nDirect connect via: `54.37.245.85:30123`"
			except:
				statusTR2=":red_circle: No response <:pepesad:666781477236768768>\n\n I'm probably just offline"
			try:
				statusTR3=":green_circle: "+str(len(requests.get(ServerAddress+":30125/players.json", timeout=2, verify=False).json()))+"/32 players"+" <:pepecool:666781477224054814>"+"\n\nFind me on the FiveM server listings!\nDirect connect via: `54.37.245.85:30125`"
			except:
				statusTR3=":red_circle: No response <:pepesad:666781477236768768>\n\n I'm probably just offline"
			try:
				statusTR4=":green_circle: "+str(len(requests.get(ServerAddress+":30127/players.json", timeout=2, verify=False).json()))+"/32 players"+" <:pepecool:666781477224054814>"+"\n\nFind me on the FiveM server listings!\nDirect connect via: `54.37.245.85:30127`"
			except:
				statusTR4=":red_circle: No response <:pepesad:666781477236768768>\n\n I'm probably just offline"

			try:
				statusUG1=":green_circle: "+str(len(requests.get(ServerAddress+":30130/players.json", timeout=2, verify=False).json()))+"/32 players"+" <:pepecool:666781477224054814>"+"\n\nFind me on the FiveM server listings!\nDirect connect via: `54.37.245.85:30130`"
			except:
				statusUG1=":red_circle: No response <:pepesad:666781477236768768>\n\n I'm probably just offline"
			try:
				statusUG2=":green_circle: "+str(len(requests.get(ServerAddress+":30131/players.json", timeout=2, verify=False).json()))+"/32 players"+" <:pepecool:666781477224054814>"+"\n\nFind me on the FiveM server listings!\nDirect connect via: `54.37.245.85:30131`"
			except:
				statusUG2=":red_circle: No response <:pepesad:666781477236768768>\n\n I'm probably just offline"
			StatusEmbed=discord.Embed(title="Velocity Networks Live Status", description="**This status was last updated: "+datetime.datetime.now().strftime("%H:%M:%S %d/%m/%y %Z")+"**\nTo join one of our servers, find us on the FiveM server listings!")
			StatusEmbed.add_field(name="\u200b", value="\u200b", inline=False)
			StatusEmbed.add_field(name="Los Santos #1", value=str(statusLS1), inline=True)
			StatusEmbed.add_field(name="Los Santos #2", value=str(statusLS2), inline=True)
			StatusEmbed.add_field(name="\u200b", value="\u200b", inline=False)
			StatusEmbed.add_field(name="Los Santos #3 (handling editor)", value=str(statusLS3), inline=True)
			StatusEmbed.add_field(name="Los Santos #4 (handling editor)", value=str(statusLS4), inline=True)
			StatusEmbed.add_field(name="\u200b", value="\u200b", inline=False)
			StatusEmbed.add_field(name="\u200b", value="\u200b", inline=False)
			StatusEmbed.add_field(name="Tracks #1", value=str(statusTR1), inline=True)
			StatusEmbed.add_field(name="Tracks #2", value=str(statusTR2), inline=True)
			StatusEmbed.add_field(name="\u200b", value="\u200b", inline=False)
			StatusEmbed.add_field(name="Tracks #3 (handling editor)", value=str(statusTR3), inline=True)
			StatusEmbed.add_field(name="Tracks #4 (handling editor)", value=str(statusTR4), inline=True)
			StatusEmbed.add_field(name="\u200b", value="\u200b", inline=False)
			StatusEmbed.add_field(name="\u200b", value="\u200b", inline=False)
			StatusEmbed.add_field(name="Underground #1", value=str(statusUG1), inline=True)
			StatusEmbed.add_field(name="Underground #2", value=str(statusUG2), inline=True)
			await ActiveMessageObject.edit(content=None, embed=StatusEmbed)
			sleep(10) # wait 10 seconds
client=MyClient() # instanciate client
client.run(BotToken) # start bot with defined token