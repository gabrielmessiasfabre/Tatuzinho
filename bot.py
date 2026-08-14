import os
import asyncio
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN=os.getenv("TOKEN")
if not TOKEN:
    raise RuntimeError("TOKEN não configurado no arquivo .env")

intents=discord.Intents.default()
intents.members=True
intents.message_content=True
intents.guilds=True

bot=commands.Bot(command_prefix="!", intents=intents)

EXTENSIONS=[
    "comandos.sistema","comandos.usuario","comandos.moderacao",
    "comandos.diversao","comandos.economia","comandos.niveis",
    "comandos.utilidades","comandos.servidor","comandos.admin","comandos.extras"
]

@bot.event
async def on_ready():
    print(f"🐢 Tatuzinho online como {bot.user}")
    try:
        cmds=await bot.tree.sync()
        print(f"✅ {len(cmds)} comandos sincronizados")
    except Exception as e:
        print("Erro ao sincronizar:",e)

async def main():
    async with bot:
        for ext in EXTENSIONS:
            await bot.load_extension(ext)
        await bot.start(TOKEN)

if __name__=="__main__":
    asyncio.run(main())
