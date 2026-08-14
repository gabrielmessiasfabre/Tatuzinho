import discord, datetime, random
from discord import app_commands
from discord.ext import commands

class Utilidades(commands.Cog):
    def __init__(self,bot): self.bot=bot

    @app_commands.command(name="hora",description="Mostra a hora atual do sistema")
    async def hora(self,i): await i.response.send_message("🕒 "+datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

    @app_commands.command(name="enquete",description="Cria uma enquete simples")
    async def enquete(self,i,pergunta:str):
        e=discord.Embed(title="📊 Enquete",description=pergunta,color=discord.Color.blurple())
        await i.response.send_message(embed=e); m=await i.original_response(); await m.add_reaction("👍"); await m.add_reaction("👎")

    @app_commands.command(name="sorteio_numero",description="Sorteia um número")
    async def sorteio(self,i,minimo:int=1,maximo:int=100):
        await i.response.send_message(f"🎉 Número sorteado: **{random.randint(minimo,maximo)}**")

    @app_commands.command(name="convite_servidor",description="Cria um convite para o canal atual")
    async def convite(self,i):
        if not i.channel.permissions_for(i.guild.me).create_instant_invite: return await i.response.send_message("❌ Não tenho permissão para criar convites.",ephemeral=True)
        inv=await i.channel.create_invite(max_age=3600,max_uses=1,reason="Tatuzinho")
        await i.response.send_message(f"🔗 {inv.url}")

    @app_commands.command(name="lembrete",description="Envia uma mensagem de lembrete")
    async def lembrete(self,i,mensagem:str):
        await i.response.send_message(f"⏰ Lembrete: **{mensagem}**")

    @app_commands.command(name="cor",description="Mostra um código hexadecimal")
    async def cor(self,i): await i.response.send_message(f"🎨 Cor aleatória: `#{random.randint(0,0xFFFFFF):06X}`")

    @app_commands.command(name="texto",description="Repete um texto")
    async def texto(self,i,mensagem:str): await i.response.send_message(mensagem)

    @app_commands.command(name="caixa",description="Cria uma caixa de informação")
    async def caixa(self,i,titulo:str,mensagem:str):
        e=discord.Embed(title=titulo,description=mensagem,color=discord.Color.blue()); await i.response.send_message(embed=e)

    @app_commands.command(name="emoji",description="Mostra um emoji")
    async def emoji(self,i): await i.response.send_message("😀 😎 🤖 🐢 🎉 🔥 ⭐")

    @app_commands.command(name="dica",description="Mostra uma dica aleatória")
    async def dica(self,i): await i.response.send_message(random.choice(["💡 Organize seus canais.","💡 Use cargos para separar funções.","💡 Ative logs de moderação.","💡 Não compartilhe seu token."]))

async def setup(bot): await bot.add_cog(Utilidades(bot))
