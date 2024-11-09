import discord
from discord import app_commands
import random 

id_do_servidor = 1071588948238942268  #Coloque aqui o ID do seu servidor

class client(discord.Client):
    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Nós usamos isso para o bot não sincronizar os comandos mais de uma vez

    async def on_ready(self):
        await self.wait_until_ready()
        if not self.synced: #Checar se os comandos slash foram sincronizados 
            await tree.sync(guild = discord.Object(id=id_do_servidor)) # Você também pode deixar o id do servidor em branco para aplicar em todos servidores, mas isso fará com que demore de 1~24 horas para funcionar.
            self.synced = True
        print(f"Entramos como {self.user}.")

aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'dado', description='Rola um dado de 6 lados') #Comando específico para seu servidor
async def slash2(interaction: discord.Interaction):
    numero = random.randint(1,6)
    await interaction.response.send_message(f"número {numero}", ephemeral = False) 

@tree.command(guild = discord.Object(id=id_do_servidor), name = 'teste', description='Testando') #Comando específico para seu servidor
async def slash3(interaction: discord.Interaction):
    await interaction.response.send_message(f"Estou funcionando!", ephemeral = False) 

aclient.run('MTMwNDg1NjM5OTU3ODI2NzY4OQ.GvWhlX.Bjd5rQ3lgQW5_s1afq_ywoI2b9gAMwQc1eO0ko')