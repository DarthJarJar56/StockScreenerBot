import discord
from discord.ext import commands
import requests
import pandas as pd

intents = discord.Intents.default()

client = commands.Bot(command_prefix="!", intents=intents)
file = open("token.txt")
token = file.read()

@client.event
async def on_ready():
    print('Screner bot is online')
    await client.change_presence(activity=discord.Game(name="Watching for low floaters!"))

lf_url = 'https://finviz.com/screener.ashx?v=131&f=cap_microunder,sh_float_u10,sh_outstanding_u10,sh_price_u10,sh_relvol_o2&ft=4'
op_url = 'https://finviz.com/screener.ashx?v=131&f=cap_mega,exch_nasd,sh_curvol_o1000,sh_opt_option,sh_price_o50,sh_relvol_o1,ta_perf_dup&ft=4'

def get_all(scan):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    if scan == "lf":
        screen = requests.get(lf_url, headers=headers).text
    elif scan == "options":
        screen = requests.get(op_url, headers=headers).text

    tables = pd.read_html(screen)
    tables = tables[-2]
    tables.columns = tables.iloc[0]
    tables = tables[1:]
    tables = tables[["Ticker", "Float", "Float Short", "Price", "Change", "Volume"]]

    return tables

err = discord.Embed(title="Error: No argument detected", description="Please specify which type of scan you would like to do:\n\n``!screen lf`` - Screen for low float micro cap stocks\n``!screen options`` - Screen for mega cap stocks with higher than usual volume at TL resistance.",
                    color=0xfa0000)
err.set_footer(text="Created by DarthJarJar#2002")
err.set_thumbnail(url="https://cdn.discordapp.com/attachments/869045095725420576/870573060292481024/red-x-red-x-11563060665ltfumg5kvi-removebg-preview.png")

err2 = discord.Embed(title="Error: Invalid argument detected", description="Please use one of the following arguments to screen:\n\n``!screen lf`` - Screen for low float micro cap stocks\n``!screen options`` - Screen for mega cap stocks with higher than usual volume at TL resistance.",
                    color=0xfa0000)
err2.set_footer(text="Created by DarthJarJar#2002")
err2.set_thumbnail(url="https://cdn.discordapp.com/attachments/869045095725420576/870573060292481024/red-x-red-x-11563060665ltfumg5kvi-removebg-preview.png")

@client.command()
async def screen(ctx, arg=None):

    if arg == "options":
        data = get_all(arg)
        em = discord.Embed(title="Screen Query Results", description=f'*_Here are the results of your screen:_*\n\n**Criteria used:**\n**Exchange:** NASDAQ\n**Market Cap:** Mega (Above $200b)\n**Price:** Over $50\n**Performance:** Today Up\n**Relative Volume:** Over 1\n**Current Volume:** Over 1M\n**Option/Short:** Optionable\n\n```{data}```', color=0x04fa98)
        em.set_footer(text="Made with ❤️ by DarthJarJar#2002")
        await ctx.send(embed=em)
    elif arg == "lf":
        data = get_all(arg)
        em = discord.Embed(title="Screen Query Results", description=f'*_Here are the results of your screen:_*\n\n**Criteria used:**\nMarket Cap: Micro (Under $300m)\nPrice: Under $10\nRelative Volume: Over 2\nShares Outstanding: Under 10M\nFloat: Under 10M\n```{data}```', color=0x04fa98)
        em.set_footer(text="Made with ❤️ by DarthJarJar#2002")
        await ctx.send(embed=em)
    else:
        await ctx.send(embed=err2)
        return
    return


@client.command()
async def find(ctx, arg=None):
    user = await client.fetch_user(arg)
    await ctx.send(f"@{user.name}#{user.discriminator}")
    

client.run(token)