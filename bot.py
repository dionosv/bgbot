from command import run_all,hitung,run_pres
import discord
import os
from discord.ext import commands

intents = discord.Intents(messages=True, guilds=True)
intents.members=True 
intents.reactions=True

client = commands.Bot(command_prefix='d.', case_insensitive=True, help_command=None)

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Photoshop'))

@commands.dm_only()
@client.command(aliases=["receive","rec"])
async def r(ctx):
    dm = await ctx.author.create_dm()
    loop=len(ctx.message.attachments)

    c=0
    hit=0
    while(c<loop):
        if ctx.message.attachments[c].filename.endswith(".jpg") or ctx.message.attachments[c].filename.endswith(".jpeg") or ctx.message.attachments[c].filename.endswith(".png") or ctx.message.attachments[c].filename.endswith(".JPG"):
            await ctx.message.attachments[c].save(fp=f"./input/{ctx.message.attachments[c].filename}")
            hit=hit+1
        else:
            msg=discord.Embed(title="File Rejected",description=f"Incorrect file type !\n``{ctx.message.attachments[c].filename}``\n**  .jpg|  .jpeg|  .png|  .JPG**\n", color=0xFF2D00)
            await dm.send(embed=msg)
        c=c+1

    msg=discord.Embed(title="File Upload Success",description=f"[{hit}/{loop}] file received\nWaiting for other file, to proccess file type in ``d.run``|``d.pres``|``d.off``", color=0x00FFFF)
    await dm.send(embed=msg)

# Dion Osvaldo Hananto

@commands.dm_only()
@client.command()
async def run(ctx):
    dm = await ctx.author.create_dm()
    jml=hitung()
    if jml !=0 :
        msg=discord.Embed(title="File Processing",description=f"{jml} file proccesed !\nPlease wait !", color=0x00FFFF)
        await dm.send(embed=msg)
        run_all(jml)

        loop=1
        while(loop<=jml):
            pdir=f"./output/out_{loop}.png"
            x=discord.File(pdir)
            await dm.send(file=x)
            os.remove(pdir)
            loop=loop+1
        msg=discord.Embed(title="File Processing Completed !",description=f"{jml} file already proccesed !", color=0x7CFC00)
        await dm.send(embed=msg)
    else:
        msg=discord.Embed(title="No File !",description="Please upload a file !", color=0xFF0000)
        await dm.send(embed=msg)

@commands.dm_only()
@client.command(aliases=["pres","pre"])
async def prestige(ctx):
    dm = await ctx.author.create_dm()
    jml=hitung()
    if jml !=0:
        msg=discord.Embed(title="Please wait !",description=f"**File Processing**\n{jml} file proccesed !", color=0xFFD700)
        await dm.send(embed=msg)
        run_pres(jml)

        loop=1
        while(loop<=jml):
            pdir=f"./prestige/prestige_{loop}.jpg"
            tmp_img=f'./output/pres_{loop}.png'
            rmbg_tmp=f"./output/out_{loop}.png"
            x=discord.File(pdir)
            await dm.send(file=x)
            os.remove(tmp_img)
            os.remove(pdir)
            os.remove(rmbg_tmp)
            loop=loop+1

        msg=discord.Embed(title="Prestige",description=f"**File Processing Completed !**\n{jml} file already proccesed !", color=0x7CFC00)
        await dm.send(embed=msg)

    else:
        msg=discord.Embed(title="No File !",description="Please upload a file !", color=0xFF0000)
        await dm.send(embed=msg)
  
client.run("insert your token here")