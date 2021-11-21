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
    
    
insult = ["tu as réussis l'exploit d'être plus cringe qu'évan", "tu as les rotations d'un bronze","tu es cringe", "ratio", "tu es un inter professionnelle"]
@bot.command()
async def flame(ctx, member : discord.Member, *, reason=None,a=None) :
    if a == None:
        a = randint(0,2)
    await ctx.send(f" Salut {member.mention} {insult[a]}")
    
@bot.command()
async def help(ctx) :
    embed = discord.Embed(title="Je suis Sylvain Pierre Durif, grand monarque christ cosmique le messi, l'homme vert, messager de Dieu, et crée par @LucasS") #,color=Hex code
    embed.add_field(name="!flame (tag) (insulte optionnelle)", value="Insulte violemment tes mates avec la force du messi")   
    await ctx.send(embed=embed)
bot.run("ODkwMzAzMDA0OTM3NDUzNjA4.YUt1SQ.mcjcu0e2EdUA60rNKO_jJbOX7kk")
