import os
from twitchio.ext import commands

# set up the bot
bot = commands.Bot(
    irc_token=os.environ['TMI_TOKEN'],
    client_id=os.environ['CLIENT_ID'],
    nick=os.environ['BOT_NICK'],
    prefix=os.environ['BOT_PREFIX'],
    initial_channels=[os.environ['CHANNEL']]
)

@bot.event
async def event_ready():
    'Called once when the bot goes online.'
    print(f"{os.environ['BOT_NICK']} is online!")
    ws = bot._ws  # this is only needed to send messages within event_ready
    await ws.send_privmsg(os.environ['CHANNEL'], f"/Vai se fude me acordo fdp")


@bot.event
async def event_message(ctx):
    'Runs every time a message is sent in chat.'

    # make sure the bot ignores itself and the streamer
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        return

    await bot.handle_commands(ctx)

    # await ctx.channel.send(ctx.content)

    if ctx.author.name == 'forthejacs':
        await ctx.channel.send(f"que voz linda a sua")

    if 'minha gostosa' in ctx.content.lower():
        await ctx.channel.send(f"vai se fude luquinha!")

    # if 'oi' in ctx.content.lower():
    #     await ctx.channel.send(f"oi é o caralho, @{ctx.author.name}!")
    
    if 'foi o bototario' in ctx.content.lower():
        await ctx.channel.send(f"foi nada vai se fude")

    


@bot.command(name='oi')
async def test(ctx):
    await ctx.send('oi é o caralho')

@bot.command(name="tchau")
async def test(ctx):
    await ctx.send('ja vai embora porque arrombido?')

if __name__ == "__main__":
    bot.run()