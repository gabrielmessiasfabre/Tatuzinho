import discord
from discord import app_commands
from discord.ext import commands

class Moderacao(commands.Cog):
    def __init__(self,bot): self.bot=bot

    @app_commands.command(name="banir",description="Bane um membro")
    @app_commands.checks.has_permissions(ban_members=True)
    async def banir(self,i,membro:discord.Member,motivo:str="Não informado"):
        await membro.ban(reason=motivo); await i.response.send_message(f"🔨 {membro} foi banido. Motivo: {motivo}")

    @app_commands.command(name="expulsar",description="Expulsa um membro")
    @app_commands.checks.has_permissions(kick_members=True)
    async def expulsar(self,i,membro:discord.Member,motivo:str="Não informado"):
        await membro.kick(reason=motivo); await i.response.send_message(f"👢 {membro} foi expulso. Motivo: {motivo}")

    @app_commands.command(name="silenciar",description="Aplica timeout a um membro")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def silenciar(self,i,membro:discord.Member,minutos:app_commands.Range[int,1,40320],motivo:str="Não informado"):
        from datetime import timedelta
        await membro.timeout(timedelta(minutes=minutos),reason=motivo)
        await i.response.send_message(f"🔇 {membro.mention} silenciado por **{minutos} min**.")

    @app_commands.command(name="dessilenciar",description="Remove o timeout")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def dessilenciar(self,i,membro:discord.Member):
        await membro.timeout(None); await i.response.send_message(f"🔊 Timeout removido de {membro.mention}.")

    @app_commands.command(name="limpar",description="Apaga mensagens")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def limpar(self,i,quantidade:app_commands.Range[int,1,100]):
        await i.response.defer(ephemeral=True)
        apagadas=await i.channel.purge(limit=quantidade)
        await i.followup.send(f"🧹 {len(apagadas)} mensagens apagadas.",ephemeral=True)

    @app_commands.command(name="avisar",description="Adverte um membro")
    @app_commands.checks.has_permissions(moderate_members=True)
    async def avisar(self,i,membro:discord.Member,motivo:str="Não informado"):
        await i.response.send_message(f"⚠️ {membro.mention} recebeu uma advertência. Motivo: {motivo}")

    @app_commands.command(name="trancar",description="Tranca o canal")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def trancar(self,i):
        ow=i.guild.default_role
        await i.channel.set_permissions(ow,send_messages=False)
        await i.response.send_message("🔒 Canal trancado.")

    @app_commands.command(name="destrancar",description="Destranca o canal")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def destrancar(self,i):
        await i.channel.set_permissions(i.guild.default_role,send_messages=True)
        await i.response.send_message("🔓 Canal destrancado.")

    @app_commands.command(name="apelidar",description="Altera o apelido")
    @app_commands.checks.has_permissions(manage_nicknames=True)
    async def apelidar(self,i,membro:discord.Member,apelido:str):
        await membro.edit(nick=apelido); await i.response.send_message(f"🏷️ Apelido de {membro.mention} alterado.")

    @app_commands.command(name="dar_cargo",description="Dá um cargo")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def dar_cargo(self,i,membro:discord.Member,cargo:discord.Role):
        await membro.add_roles(cargo); await i.response.send_message(f"🎭 Cargo {cargo.mention} dado a {membro.mention}.")

    @app_commands.command(name="remover_cargo",description="Remove um cargo")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def remover_cargo(self,i,membro:discord.Member,cargo:discord.Role):
        await membro.remove_roles(cargo); await i.response.send_message(f"🎭 Cargo removido de {membro.mention}.")

    @app_commands.command(name="anunciar",description="Envia um anúncio no canal")
    @app_commands.checks.has_permissions(manage_messages=True)
    async def anunciar(self,i,mensagem:str):
        e=discord.Embed(title="📢 Anúncio",description=mensagem,color=discord.Color.gold())
        await i.response.send_message(embed=e)

    @app_commands.command(name="slowmode",description="Define o modo lento do canal")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def slowmode(self,i,segundos:app_commands.Range[int,0,21600]):
        await i.channel.edit(slowmode_delay=segundos); await i.response.send_message(f"🐢 Slowmode: **{segundos}s**.")

async def setup(bot): await bot.add_cog(Moderacao(bot))
