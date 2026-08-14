import discord
from discord import app_commands
from discord.ext import commands

class Usuario(commands.Cog):
    def __init__(self,bot): self.bot=bot

    @app_commands.command(name="usuario",description="Mostra informações de um usuário")
    async def usuario(self,i,membro:discord.Member=None):
        m=membro or i.user
        e=discord.Embed(title=f"👤 {m.display_name}",color=discord.Color.blue())
        e.set_thumbnail(url=m.display_avatar.url)
        e.add_field(name="ID",value=str(m.id),inline=False)
        e.add_field(name="Conta criada",value=m.created_at.strftime("%d/%m/%Y"))
        e.add_field(name="Entrou no servidor",value=m.joined_at.strftime("%d/%m/%Y") if m.joined_at else "N/A")
        await i.response.send_message(embed=e)

    @app_commands.command(name="avatar",description="Mostra o avatar")
    async def avatar(self,i,membro:discord.Member=None):
        m=membro or i.user
        e=discord.Embed(title=f"🖼️ Avatar de {m.display_name}")
        e.set_image(url=m.display_avatar.url)
        await i.response.send_message(embed=e)

    @app_commands.command(name="id",description="Mostra o ID de um usuário")
    async def id(self,i,membro:discord.Member=None):
        m=membro or i.user
        await i.response.send_message(f"🆔 ID de **{m.display_name}**: `{m.id}`")

    @app_commands.command(name="cargos",description="Lista os cargos de um usuário")
    async def cargos(self,i,membro:discord.Member=None):
        m=membro or i.user
        cargos=[r.mention for r in m.roles if r.name!="everyone"]
        await i.response.send_message("🎭 Cargos: "+(", ".join(cargos) if cargos else "Nenhum"))

    @app_commands.command(name="permissoes",description="Mostra as permissões de um usuário")
    async def permissoes(self,i,membro:discord.Member=None):
        m=membro or i.user
        p=[n.replace("_"," ").title() for n,v in m.guild_permissions if v]
        await i.response.send_message("🔑 Permissões:\n"+", ".join(p))

    @app_commands.command(name="conta",description="Mostra a data de criação da conta")
    async def conta(self,i,membro:discord.Member=None):
        m=membro or i.user
        await i.response.send_message(f"📅 Conta criada em **{m.created_at.strftime('%d/%m/%Y às %H:%M')}**")

    @app_commands.command(name="entrada",description="Mostra quando entrou no servidor")
    async def entrada(self,i,membro:discord.Member=None):
        m=membro or i.user
        await i.response.send_message(f"📥 Entrada: **{m.joined_at.strftime('%d/%m/%Y às %H:%M') if m.joined_at else 'N/A'}**")

    @app_commands.command(name="bot",description="Diz se um usuário é bot")
    async def bot(self,i,membro:discord.Member=None):
        m=membro or i.user
        await i.response.send_message(f"🤖 {m.mention} {'é' if m.bot else 'não é'} um bot.")

    @app_commands.command(name="nome",description="Mostra o nome de usuário")
    async def nome(self,i,membro:discord.Member=None):
        m=membro or i.user
        await i.response.send_message(f"🏷️ Nome: **{m.name}**")

    @app_commands.command(name="apelido_atual",description="Mostra o apelido atual")
    async def apelido_atual(self,i,membro:discord.Member=None):
        m=membro or i.user
        await i.response.send_message(f"🏷️ Apelido: **{m.display_name}**")

async def setup(bot): await bot.add_cog(Usuario(bot))
