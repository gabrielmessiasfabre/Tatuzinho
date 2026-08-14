import discord, aiosqlite
from discord import app_commands
from discord.ext import commands
DB="tatuzinho.db"

class Niveis(commands.Cog):
    def __init__(self,bot): self.bot=bot

    async def init(self):
        async with aiosqlite.connect(DB) as db:
            await db.execute("CREATE TABLE IF NOT EXISTS xp (id INTEGER PRIMARY KEY, pontos INTEGER DEFAULT 0)")
            await db.commit()

    @app_commands.command(name="nivel",description="Mostra seu nível")
    async def nivel(self,i):
        await self.init()
        async with aiosqlite.connect(DB) as db:
            cur=await db.execute("SELECT pontos FROM xp WHERE id=?",(i.user.id,)); r=await cur.fetchone()
        xp=r[0] if r else 0
        await i.response.send_message(f"⭐ **{i.user.display_name}** — XP: **{xp}** | Nível: **{xp//100+1}**")

    @app_commands.command(name="xp",description="Mostra seu XP")
    async def xp(self,i): await self.nivel(i)

    @app_commands.command(name="ranking_xp",description="Ranking de XP")
    async def ranking(self,i):
        await self.init()
        async with aiosqlite.connect(DB) as db:
            cur=await db.execute("SELECT id,pontos FROM xp ORDER BY pontos DESC LIMIT 10"); rows=await cur.fetchall()
        txt="\n".join(f"**{n}.** <@{uid}> — {xp} XP" for n,(uid,xp) in enumerate(rows,1)) or "Ainda não há XP."
        await i.response.send_message("⭐ **Ranking de XP**\n"+txt)

    @app_commands.command(name="adicionar_xp",description="Adiciona XP a um usuário")
    @app_commands.checks.has_permissions(manage_guild=True)
    async def addxp(self,i,membro:discord.Member,quantidade:app_commands.Range[int,1,100000]):
        await self.init()
        async with aiosqlite.connect(DB) as db:
            await db.execute("INSERT INTO xp(id,pontos) VALUES(?,?) ON CONFLICT(id) DO UPDATE SET pontos=pontos+excluded.pontos",(membro.id,quantidade)); await db.commit()
        await i.response.send_message(f"⭐ {quantidade} XP adicionados a {membro.mention}.")

async def setup(bot): await bot.add_cog(Niveis(bot))
