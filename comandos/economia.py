import random, aiosqlite, discord
from discord import app_commands
from discord.ext import commands

DB="tatuzinho.db"

class Economia(commands.Cog):
    def __init__(self,bot): self.bot=bot

    async def init(self):
        async with aiosqlite.connect(DB) as db:
            await db.execute("CREATE TABLE IF NOT EXISTS contas (id INTEGER PRIMARY KEY, saldo INTEGER DEFAULT 0)")
            await db.commit()

    async def get(self,uid):
        await self.init()
        async with aiosqlite.connect(DB) as db:
            cur=await db.execute("SELECT saldo FROM contas WHERE id=?",(uid,))
            row=await cur.fetchone()
            if not row:
                await db.execute("INSERT INTO contas(id,saldo) VALUES(?,0)",(uid,)); await db.commit(); return 0
            return row[0]

    async def add(self,uid,n):
        await self.init()
        async with aiosqlite.connect(DB) as db:
            await db.execute("INSERT INTO contas(id,saldo) VALUES(?,?) ON CONFLICT(id) DO UPDATE SET saldo=saldo+excluded.saldo",(uid,n))
            await db.commit()

    @app_commands.command(name="saldo",description="Mostra seu saldo")
    async def saldo(self,i): await i.response.send_message(f"💰 Saldo: **R$ {await self.get(i.user.id):,}**".replace(",","."))

    @app_commands.command(name="diario",description="Recebe R$ 500")
    async def diario(self,i): await self.add(i.user.id,500); await i.response.send_message("🎁 Você recebeu **R$ 500**.")

    @app_commands.command(name="trabalhar",description="Trabalha e recebe dinheiro")
    async def trabalhar(self,i):
        n=random.randint(100,700); await self.add(i.user.id,n); await i.response.send_message(f"💼 Você trabalhou e ganhou **R$ {n}**.")

    @app_commands.command(name="bonus",description="Recebe um bônus")
    async def bonus(self,i): await self.add(i.user.id,250); await i.response.send_message("🎉 Bônus de **R$ 250** recebido.")

    @app_commands.command(name="pagar",description="Paga outro usuário")
    async def pagar(self,i,membro:discord.Member,valor:app_commands.Range[int,1,1000000]):
        if await self.get(i.user.id)<valor: return await i.response.send_message("❌ Saldo insuficiente.",ephemeral=True)
        await self.add(i.user.id,-valor); await self.add(membro.id,valor); await i.response.send_message(f"💸 Você pagou **R$ {valor}** para {membro.mention}.")

    @app_commands.command(name="apostar",description="Aposta dinheiro de brincadeira")
    async def apostar(self,i,valor:app_commands.Range[int,1,10000]):
        if await self.get(i.user.id)<valor: return await i.response.send_message("❌ Saldo insuficiente.")
        if random.random()<0.5: await self.add(i.user.id,valor); r=f"Você ganhou **R$ {valor}**!"
        else: await self.add(i.user.id,-valor); r=f"Você perdeu **R$ {valor}**."
        await i.response.send_message("🎲 "+r)

    @app_commands.command(name="ranking_dinheiro",description="Mostra o ranking econômico")
    async def ranking(self,i):
        await self.init()
        async with aiosqlite.connect(DB) as db:
            cur=await db.execute("SELECT id,saldo FROM contas ORDER BY saldo DESC LIMIT 10"); rows=await cur.fetchall()
        txt="\n".join(f"**{n}.** <@{uid}> — R$ {saldo:,}".replace(",",".") for n,(uid,saldo) in enumerate(rows,1)) or "Nenhuma conta."
        await i.response.send_message("🏆 **Ranking**\n"+txt)

    @app_commands.command(name="resetar_saldo",description="Zera seu próprio saldo")
    async def reset(self,i): 
        async with aiosqlite.connect(DB) as db:
            await db.execute("INSERT INTO contas(id,saldo) VALUES(?,0) ON CONFLICT(id) DO UPDATE SET saldo=0",(i.user.id,)); await db.commit()
        await i.response.send_message("♻️ Seu saldo foi zerado.")

async def setup(bot): await bot.add_cog(Economia(bot))
