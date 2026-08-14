import random, discord
from discord import app_commands
from discord.ext import commands

class Diversao(commands.Cog):
    def __init__(self,bot): self.bot=bot

    async def msg(self,i,text): await i.response.send_message(text)

    @app_commands.command(name="dado",description="Rola um dado")
    async def dado(self,i,lados:app_commands.Range[int,2,100]=6): await self.msg(i,f"🎲 Resultado: **{random.randint(1,lados)}**")

    @app_commands.command(name="cara_ou_coroa",description="Joga cara ou coroa")
    async def cc(self,i): await self.msg(i,f"🪙 Deu **{random.choice(['Cara','Coroa'])}**!")

    @app_commands.command(name="escolher",description="Escolhe entre duas opções")
    async def escolher(self,i,opcao1:str,opcao2:str): await self.msg(i,f"🎯 Escolhi: **{random.choice([opcao1,opcao2])}**")

    @app_commands.command(name="numero",description="Gera um número aleatório")
    async def numero(self,i,minimo:int=1,maximo:int=100):
        if minimo>maximo: return await self.msg(i,"❌ O mínimo não pode ser maior que o máximo.")
        await self.msg(i,f"🔢 Número: **{random.randint(minimo,maximo)}**")

    @app_commands.command(name="sorte",description="Diz seu nível de sorte")
    async def sorte(self,i): await self.msg(i,f"🍀 Sua sorte hoje é **{random.randint(0,100)}%**.")

    @app_commands.command(name="moeda",description="Joga uma moeda")
    async def moeda(self,i): await self.cc(i)

    @app_commands.command(name="avaliar",description="Avalia algo de 0 a 10")
    async def avaliar(self,i,coisa:str): await self.msg(i,f"📊 Eu dou **{random.randint(0,10)}/10** para **{coisa}**.")

    @app_commands.command(name="8ball",description="Responde uma pergunta")
    async def ball(self,i,pergunta:str):
        r=["Sim.","Não.","Talvez.","Provavelmente.","Com certeza.","Não conte com isso."]
        await self.msg(i,f"🎱 {random.choice(r)}")

    @app_commands.command(name="pedra_papel_tesoura",description="Joga pedra, papel e tesoura")
    async def ppt(self,i,escolha:str):
        op=escolha.lower(); jog=random.choice(["pedra","papel","tesoura"])
        if op not in ["pedra","papel","tesoura"]: return await self.msg(i,"❌ Escolha pedra, papel ou tesoura.")
        resultado="Empate!" if op==jog else ("Você ganhou!" if (op,jog) in [("pedra","tesoura"),("papel","pedra"),("tesoura","papel")] else "Eu ganhei!")
        await self.msg(i,f"🎮 Você: **{op}** | Eu: **{jog}**\n**{resultado}**")

    @app_commands.command(name="embaralhar",description="Embaralha um texto")
    async def embaralhar(self,i,texto:str):
        l=list(texto); random.shuffle(l); await self.msg(i,"🔀 "+''.join(l))

    @app_commands.command(name="sim_ou_nao",description="Responde sim ou não")
    async def simnao(self,i): await self.msg(i,random.choice(["✅ Sim!","❌ Não!"]))

    @app_commands.command(name="percentual",description="Gera uma porcentagem divertida")
    async def percentual(self,i,coisa:str): await self.msg(i,f"📈 **{coisa}**: {random.randint(0,100)}%")

    @app_commands.command(name="contador",description="Conta de 1 até um limite")
    async def contador(self,i,limite:app_commands.Range[int,1,20]):
        await self.msg(i,"🔢 "+" ".join(map(str,range(1,limite+1))))

async def setup(bot): await bot.add_cog(Diversao(bot))
