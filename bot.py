import os
import json
from twitchio.ext import commands
from operator import itemgetter

curse_words = {}
with open('curse_words.json') as json_file:
    curse_words = json.load(json_file)

users = []

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
    if ctx.author.name.lower() == os.environ['BOT_NICK'].lower():
        # make sure the bot ignores itself and the streamer
        return

    #content aimed to him
    if 'bototario' in ctx.content.lower():
        await bot.handle_commands(ctx)
        

        #timeout user if he curses bototario five times
        for curse in curse_words['listen']:
            if curse in ctx.content.lower():
                if ctx.author.name in map(itemgetter('user'), users):
                    index = list(map(itemgetter('user'), users)).index(ctx.author.name)
                    users[index]['times_cursed'] += 1


                    if users[index]['times_cursed'] <= 2: 
                        await ctx.channel.send(f"mano, to sem paciência nem vem")
                        return
                    if users[index]['times_cursed'] == 3: 
                        await ctx.channel.send(f"@{ctx.author.name} ce ta me irritano")
                        return
                    if users[index]['times_cursed'] == 4: 
                        await ctx.channel.send(f"se chingar de novo vai toma TO")
                        return
                    if users[index]['times_cursed'] == 5: 
                        await ctx.channel.send(f"tomaaa, agora fica quieto ai palhaço")
                        users[index]['times_cursed'] = 0
                        await ctx.channel.timeout(ctx.author.name, 60)
                        return

                    return

                else:
                    users.append({
                        "user":ctx.author.name,
                        "times_cursed":0
                    })
                    await ctx.channel.send(f"oxi, te dei liberdade de falar coisas chulas comigo é?")
                    return


        content = ctx.content.lower()
        #greetings
        if 'olá' in content or 'eae' in content or 'oi' in content or 'fala' in content or 'oie' in content:
            await ctx.channel.send(f"que cê quer @{ctx.author.name}")
            return
        
        #good byes
        if 'tchau' in content or 'xau' in content or 'flw' in content or 'boa noite' in content:
            await ctx.channel.send(f"ja vai embora porque arrombido?")
            return
        
        # Usa pra ativar quando alguem fala
        # if ctx.author.name == 'forthejacs':
        #     await ctx.channel.send(f"que voz linda a sua")

        

        
        
    #content not aimed to him    
    if 'minha gostosa' in ctx.content.lower():
        await ctx.channel.send(f"vai se fude luquinha, fica chamando os otro de minha gostosa eu ein!")
        return

    if 'foi o bot' in ctx.content.lower():
        await ctx.channel.send(f"foi nada, se fude")
        return

    if 'jac é um bot?' in ctx.content.lower():
        await ctx.channel.send(f"ela eh!! e ta no mesmo servidor que eu")
        return


# @bot.command(name="tchau")
# async def tchau(ctx):
#     await ctx.send('ja vai embora porque arrombido?')

if __name__ == "__main__":
    bot.run()