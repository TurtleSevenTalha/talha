import discord
from discord.ext import commands
import os 
import random 

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben bir botum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def naber(ctx, count_naber = 5):
    await ctx.send('iyilik senden naber') 

@bot.command()
async def sa(ctx, count_sa = 5):
    await ctx.send('as')  

@bot.command()
async def taha(ctx, count_taha = 5):
    await ctx.send('TAHA AĞLAMAA')

@bot.command()
async def tha(ctx, count_tha = 5):
    await ctx.send('TAHA AĞLAMAA')

@bot.command()
async def beyler (ctx, count_beyler = 5):
    await ctx.send('beyler come gelin artık uyaaan')
    
@bot.command()
async def joined(ctx, member: discord.Member):
    """Says when a member joined."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')



@bot.command()
async def mem(ctx):
    with open('image/mem1.jpg', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

@bot.command()
async def randommem(ctx):
    img_name =random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        # Dönüştürülen Discord kütüphane dosyasını bu değişkende saklayalım!
        picture = discord.File(f)
   # Daha sonra bu dosyayı bir parametre olarak gönderebiliriz!
    await ctx.send(file=picture)

print(os.listdir('images'))







bot.run("MTEzOTI1NzQ4NjQ5NTQ2NTU0Mg.G0oZOX.i58o8VJRLyRYDxvf2ofQ0x4zIVgwp_MJgj4eqY")

