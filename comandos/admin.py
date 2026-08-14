import discord
from discord import app_commands
from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self,bot): self.bot=bot

    @app_commands.command(name="criar_cargo",description="Cria um cargo")
    @app_commands.checks.has_permissions(manage_roles=True)
    async def criar_cargo(self,i,nome:str):
        r=await i.guild.create_role(name=nome,reason=f"Criado por {i.user}")
        await i.response.send_message(f"🎭 Cargo criado: {r.mention}")

    @app_commands.command(name="criar_canal",description="Cria um canal de texto")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def criar_canal(self,i,nome:str):
        c=await i.guild.create_text_channel(nome,reason=f"Criado por {i.user}")
        await i.response.send_message(f"📁 Canal criado: {c.mention}")

    @app_commands.command(name="renomear_canal",description="Renomeia o canal atual")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def renomear(self,i,nome:str):
        await i.channel.edit(name=nome); await i.response.send_message(f"✏️ Canal renomeado para **{nome}**.")

    @app_commands.command(name="deletar_canal",description="Deleta o canal atual")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def deletar(self,i):
        c=i.channel
        await i.response.send_message("🗑️ Canal será excluído.")
        await c.delete(reason=f"Excluído por {i.user}")

    @app_commands.command(name="criar_categoria",description="Cria uma categoria")
    @app_commands.checks.has_permissions(manage_channels=True)
    async def categoria(self,i,nome:str):
        c=await i.guild.create_category(nome); await i.response.send_message(f"📂 Categoria criada: **{c.name}**")

    @app_commands.command(name="nick_bot",description="Altera o apelido do Tatuzinho")
    @app_commands.checks.has_permissions(manage_nicknames=True)
    async def nickbot(self,i,nome:str):
        await i.guild.me.edit(nick=nome); await i.response.send_message(f"🐢 Meu apelido agora é **{nome}**.")

    @app_commands.command(name="renomear_servidor",description="Renomeia o servidor")
    @app_commands.checks.has_permissions(manage_guild=True)
    async def renomear_servidor(self,i,nome:str):
        await i.guild.edit(name=nome); await i.response.send_message(f"🏠 Servidor renomeado para **{nome}**.")

async def setup(bot): await bot.add_cog(Admin(bot))
