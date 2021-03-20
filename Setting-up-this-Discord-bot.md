# How to setup the Discord bot
## Prerequisites
- A Discord account
- Python
- A Discord guild (server) that you have administrative access on

## Step 1 - register your bot
- go to https://discord.com/developers/applications
- login/make a Discord account
- create an application (press "New Application" button)
- enter name of bot (it's shown to everyone, choose wisely)
- open bot tab on left, then press "Add Bot"

## Step 2 - add bot to your server
- copy your bot's client ID into this string and go to it in your web browser - you can get your client ID from the bot's "General Information" tab (https://discord.com/oauth2/authorize?client_id=CLIENTIDGOESHERE&scope=bot)

## Step 3 - configure the bot
- enable Developer Mode in Discord (https://www.discordtips.com/how-to-enable-developer-mode-in-discord/)
- copy the ID of the channel into `ChannelID`
- put the servers you want in the `Servers` array
- change the title of the embed in `EmbedTitle`
- if you need to, you can change `UpdateDelay` and `CounterCap`
- `PublicIP` is used so people can opt to direct connect to the servers. Change it to your server's public IP
- set `BotToken` to your bot's token (you can get this from the bot's "Bot" tab by clicking "Copy" under "Token")

## Step 4 - setup Python
- make sure you have Python3 installed. If you're on Windows 10, you can find it on the Windows Store, if not download it from their website (https://www.python.org/)
- install the required libraries - discord, requests, and json (you can do this by copying `pythom3 -m pip install LIBRARYNAME` in command prompt, where `LIBRARYNAME` are the three libraries)
- run the code!

## NOTES
- all links in this document are accurate as of date of last update.
- feel free to pr anything if you think it could do with being improved