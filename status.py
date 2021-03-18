#######################################
#######################################
################ ABOUT ################
#######################################
#######################################

# GITHUB REPO: https://github.com/jcfoxtrot54/FiveM-Discord-Bot
# AUTHOR: JCF#7536
# NOTE: edit this to your heart's content, it's less than 100 lines, if you're generous plz give credit xoxo
# VERSION: 3

#######################################
#######################################
############ CONFIGURATION ############
#######################################
#######################################

ChannelID=709801509210030160 # CHANNEL ID YOU WANT STATUS OUPUT
Servers=[ # LIST OF SERVERS TO DISPLAY // NOTE: IF BYPASS IS SET TO TRUE IT WILL ACT AS A LINE BREAK
	{"URL": "http://localhost:30120", "DisplayName":"Los Santos #1", "Bypass":False},
	{"URL": "http://localhost:30122", "DisplayName":"Los Santos #2", "Bypass":False},
	{"Bypass":True},
	{"URL": "http://localhost:30124", "DisplayName":"Los Santos #3", "Bypass":False},
	{"URL": "http://localhost:30126", "DisplayName":"Los Santos #4", "Bypass":False},
	{"Bypass":True},
	{"Bypass":True},
	{"URL": "http://localhost:30121", "DisplayName":"Tracks #1", "Bypass":False},
	{"URL": "http://localhost:30123", "DisplayName":"Tracks #2", "Bypass":False},
	{"Bypass":True},
	{"URL": "http://localhost:30125", "DisplayName":"Tracks #3", "Bypass":False},
	{"URL": "http://localhost:30127", "DisplayName":"Tracks #4", "Bypass":False},
	{"Bypass":True},
	{"Bypass":True},
	{"URL": "http://localhost:30130", "DisplayName":"Underground #1", "Bypass":False},
	{"URL": "http://localhost:30131", "DisplayName":"Underground #2", "Bypass":False},
]
EmbedTitle="Velocity Networks FiveM Server Status (https://github.com/jcfoxtrot54/FiveM-Discord-Bot)" # TITLE OF THE EMBED
UpdateDelay=5 # DELAY FOR STATUS TO UPDATE (SECONDS)
CounterCap=30 # HOW MANY TIMES THE MESSAGE SHOULD UPDATE BEFORE IT IS REGENERATED
PublicIP="velocitynetworks.org" # PUBLIC IP TO DISPLAY
BotToken="lmao no" # BOT TOKEN 

#######################################
#######################################
######## DON'T EDIT BELOW HERE ########
#######################################
#######################################

try:
	import discord # import discord library
	import requests # import requests library
	import json # import json library
	import datetime # import datetime library
	from time import sleep # import sleep function from time library
except ImportError as module: # if an import error is raised
	print("ERROR: CANNOT IMPORT '"+module.name+"' LIBRARY. IS IT INSTALLED?")
	exit() # halt execution

class MyClient(discord.Client):
	def __init__(self, CounterCap, Servers, ChannelID, EmbedTitle, Delay, PublicIP):
		super().__init__() # inherit parent class' attributes (discord.Client)
		self.ChannelObject=None
		self.ActiveMessageObject=None
		self.Counter=50
		self.CounterCap=CounterCap
		self.Servers=Servers
		self.ChannelID=ChannelID
		self.EmbedTitle=EmbedTitle
		self.Delay=Delay
		self.PublicIP=PublicIP

	async def on_ready(self): # when bot is ready
		print('Connected as {0}!'.format(self.user)) # identify self in conssole
		self.ChannelObject=await self.fetch_channel(self.ChannelID) # get channel from id specified
		while True:
			if self.Counter>=self.CounterCap: # if counter is not greater than or equal to defined limit
				await self.ChannelObject.purge() # purge channel
				self.ActiveMessageObject=await self.ChannelObject.send("Loading...") # add new message
				self.Counter=0 # reset counter
			StatusEmbed=discord.Embed(title=self.EmbedTitle, description="**This status was last updated: "+datetime.datetime.now().strftime("%H:%M:%S %d/%m/%y %Z")+"**\nTo join one of our servers, find us on the FiveM server listings!") # date time pulls HOUR:MINUTE:SECOND DAY:MONTH:YEAR TIMEZONE (so you know if bot's crashed)
			for serverObj in self.Servers: # for each dictionary in Servers object
				if serverObj["Bypass"]: # if bypass is set to True
					StatusEmbed.add_field(name="\u200b", value="\u200b", inline=False) # insert blanking object
				else:
					try:
						StatusEmbed.add_field(name=serverObj["DisplayName"], value=":green_circle: "+str(len(requests.get(serverObj["URL"]+"/players.json", timeout=2, verify=False).json()))+"/32 players"+" <:pepecool:666781477224054814>"+"\n\nFind me on the FiveM server listings!\nDirect connect via: `"+PublicIP+":"+serverObj["URL"][-5:]+"`", inline=True)
						# runs HTTP request to specified endpoint with a timeout of 2 seconds, encodes it into JSON then gets the length of it (to get number of players). Verify is false because who needs SSL anyway :shrug:
					except: # if this errors (endpoint isn't reachable)
						StatusEmbed.add_field(name=serverObj["DisplayName"], value=":red_circle: No response <:pepesad:666781477236768768>\n\n I'm probably just offline", inline=True)
			await self.ActiveMessageObject.edit(content=None, embed=StatusEmbed) # edit the message object
			self.Counter+=1 # incremement counter by one
			sleep(self.Delay) # wait for specified delay in seconds
client=MyClient(CounterCap, Servers, ChannelID, EmbedTitle, UpdateDelay, PublicIP) # instanciate client from class
client.run(BotToken) # run client with specified bot token
