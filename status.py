ServerAddress="http://localhost" # <==== CHANGE THIS TO THE IP OF YOUR SERVER IF IT'S NOT HOSTED ON THE SAME MACHINE (INCLUDE NO PORTS)
ChannelID=0 			 # <==== CHANNEL ID YOU WANT STATUS OUPUT
BotToken="" 			 # <==== BOT TOKEN 

import discord # import discord library
import requests # import requests library
import json # import json library
import datetime # import datetime library
from time import sleep # import sleep function from time library

ChannelObject=None # store object of channel
ActiveMessageObject=None # store object of status message


class MyClient(discord.Client):
	async def on_ready(self):
		print('Connected as {0}!'.format(self.user)) # identify self in conssole
		ChannelObject=await self.fetch_channel(ChannelID) # get channel from id specified
		MessageInvalid=True
		while True:
			if MessageInvalid: # if the message object is invalid, designate a new one
				await ChannelObject.purge() # clear channel
				ActiveMessageObject=await ChannelObject.send("Loading...") # add new message
				MessageInvalid=False # set mesagevalidity to valid
			else: # if message is valid
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
				# create embed
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

				try: # attempt to
					await ActiveMessageObject.edit(content=None, embed=StatusEmbed) # edit the message object
				except: # if it fails
					print("Message object invalid. Regenerating")
					MessageInvalid=True # mark object as invalid to be reassigned
			sleep(10) # wait 10 seconds
client=MyClient()
client.run(BotToken)
