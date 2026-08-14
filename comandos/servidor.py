import discord
from discord import app_commands
from discord.ext import commands

class Servidor(commands.Cog):
    def __init__(self,bot): self.bot=bot

    @app_commands.command(name="servidor",description="Informações do servidor")
    async def servidor(self,i):
        g=i.guild
        e=discord.Embed(title=f"🏠 {g.name}",color=discord.Color.blurple())
        e.add_field(name="👥 Membros",value=str(g.member_count))
        e.add_field(name="💬 Canais",value=str(len(g.channels)))
        e.add_field(name="🎭 Cargos",value=str(len(g.roles)))
        e.add_field(name="📅 Criado",value=g.created_at.strftime("%d/%m/%Y"))
        if g.icon: e.set_thumbnail(url=g.icon.url)
        await i.response.send_message(embed=e)

    @app_commands.command(name="canais",description="Lista a quantidade de canais")
    async def canais(self,i):
        g=i.guild; await i.response.send_message(f"📚 Texto: **{len(g.text_channels)}** | Voz: **{len(g.voice_channels)}** | Total: **{len(g.channels)}**")

    @app_commands.command(name="cargos_servidor",description="Lista os cargos")
    async def cargos(self,i):
        cargos=[r.mention for r in i.guild.roles if r.name!="everyone"]
        await i.response.send_message("🎭 "+(", ".join(cargos) if cargos else "Nenhum"))

    @app_commands.command(name="dono",description="Mostra o dono")
    async def dono(self,i): await i.response.send_message(f"👑 Dono: {i.guild.owner.mention if i.guild.owner else 'Desconhecido'}")

    @app_commands.command(name="membros",description="Mostra a quantidade de membros")
    async def membros(self,i): await i.response.send_message(f"👥 Este servidor tem **{i.guild.member_count}** membros.")

    @app_commands.command(name="id_servidor",description="Mostra o ID")
    async def idservidor(self,i): await i.response.send_message(f"🆔 `{i.guild.id}`")

async def setup(bot): await bot.add_cog(Servidor(bot))
