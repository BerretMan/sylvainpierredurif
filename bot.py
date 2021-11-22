import discord
from discord.ext import commands
from random import*

bot = commands.Bot(command_prefix = "!", description = "Je suis le Bot et L'esclave de @LucasS#2717",help_command=None)

@bot.event
async def on_ready():
    print("Ready ")


@bot.command()
async def speak(ctx, arg):
    await ctx.send(arg)
    await ctx.delete(arg)
    
    
insult = ["tu as réussis l'exploit d'être plus cringe qu'evan", "tu as les rotations d'un bronze","f'in fréro, tu es cringe", "ratio", "fin frerot allume l'écran"]
@bot.command()
async def flame(ctx, member : discord.Member,a=None) :
    if a == None:
        a = randint(0,5)
    await ctx.send(f" Salut {member.mention} {insult[a]}")
    

lovelist = ["Tu travaillerais pas chez AirFrance? Parceque j'ai un avion de chasse en face de moi","Tu serais pas un dm de maths? Parceque j'ai vraiment envie de te terminer à 4h du mat sur une table"]
@bot.command()
async def seduce(ctx, member : discord.Member,a=None) :
    if a == None:
        a = randint(0,1)
    await ctx.send(f" Salut {member.mention} {lovelist[a]}")
    

@bot.command()
async def help(ctx) :
    embed = discord.Embed(title="Je suis Sylvain Pierre Durif, grand monarque christ cosmique le messi, l'homme vert, messager de Dieu, et crée par @LucasS") #,color=Hex code
    embed.add_field(name="!flame (tag) (insulte optionnelle)", value="Insulte violemment tes mates avec la force du messi")  
    embed.add_field(name="!seduce (tag) (insulte optionnelle)", value="Utilise la puissance du messi pour conquérir ta dulciné (ne fonctionne pas si vous jouer à lol)")    
    await ctx.send(embed=embed)












bot.run("NonTuAurasPasMonToken")
