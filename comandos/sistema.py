import discord
from discord import app_commands
from discord.ext import commands

class Sistema(commands.Cog):
    def __init__(self,bot): self.bot=bot

    @app_commands.command(name="ping",description="Mostra a latência do Tatuzinho")
    async def ping(self,i): await i.response.send_message(f"🏓 Pong! **{round(self.bot.latency*1000)}ms**")

    @app_commands.command(name="sobre",description="Informações sobre o Tatuzinho")
    async def sobre(self,i):
        e=discord.Embed(title="🐢 Tatuzinho",description="Bot completo em português.",color=discord.Color.blurple())
        e.add_field(name="Versão",value="1.0")
        e.add_field(name="Comandos",value="100+")
        await i.response.send_message(embed=e)

    @app_commands.command(name="ajuda",description="Mostra a central de ajuda")
    async def ajuda(self,i):
        await i.response.send_message("🐢 **Tatuzinho — Central de Ajuda**\nUse `/comandos` para ver as categorias.")

    @app_commands.command(name="comandos",description="Lista as categorias de comandos")
    async def comandos(self,i):
        await i.response.send_message("🛡️ Moderação • 👤 Usuários • 💰 Economia • ⭐ Níveis • 🎮 Diversão • 🛠️ Utilidades • ⚙️ Servidor • 🔧 Administração")

    @app_commands.command(name="estatisticas",description="Mostra estatísticas do bot")
    async def estatisticas(self,i):
        await i.response.send_message(f"🐢 Servidores: **{len(self.bot.guilds)}** | Latência: **{round(self.bot.latency*1000)}ms**")

    @app_commands.command(name="convite",description="Mostra instrução para convidar o bot")
    async def convite(self,i): await i.response.send_message("Use o link de instalação gerado no Discord Developer Portal para convidar o Tatuzinho.")

    @app_commands.command(name="status",description="Mostra o status do bot")
    async def status(self,i): await i.response.send_message("🟢 **Online e operacional**")

    @app_commands.command(name="servidores",description="Quantidade de servidores conectados")
    async def servidores(self,i): await i.response.send_message(f"🌐 Estou em **{len(self.bot.guilds)}** servidor(es).")

async def setup(bot): await bot.add_cog(Sistema(bot))
