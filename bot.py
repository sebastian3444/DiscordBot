from discord_webhooks import DiscordWebhooks
import discord

Bot=DiscordWebhooks (webhook_url="https://discordapp.com/api/webhooks/591404084477558806/kfnSdUIe5RXtAzr7ROuXncZo3G4a-f9G9KPSfGGoISdCIfgYnvBxQ-dvaPa8SHhmwTaE")


def readToken():
    with open("token.txt","r") as f:
        linea=f.readlines()
        return linea[0].strip()




token=readToken()
client=discord.Client()



@client.event
async def on_message(message):
    if message.content.find("!Hola") != -1:
        await message.channel.send("Hola pvto :v")
    if message.content.find("!Una de pubg") != -1:
        await message.channel.send("Bomba :v")
    if message.content.find("!Miembros") != -1:
        await message.channel.send(str(client.get_all_members()))
    if message.content.startswith("!Suma "):
        vals=message.content.split(" ")
        x=int(vals[1])
        y=int(vals[3])
        res=x+y
        msg="Facilingo loco es "+str(res)+" :v"
        await message.channel.send(msg)
    if message.content.startswith("!Multiplica "):
        vals=message.content.split(" ")
        x=int(vals[1])
        y=int(vals[3])
        res=x*y
        msg="Facilingo loco es "+str(res)+" :v"
        await message.channel.send(msg)
    if message.content.startswith("!Resta "):
        vals=message.content.split(" ")
        x=int(vals[1])
        y=int(vals[3])
        res=x-y
        msg="Facilingo loco es "+str(int(res))+" :v"
        await message.channel.send(msg)
    if message.content.startswith("!DivideEntero "):
        vals=message.content.split(" ")
        x=int(vals[1])
        y=int(vals[3])
        res=x/y
        res1=x%y
        msg="Facilingo loco es "+str(int(res))+" y el residuo es "+str(res1)
        await message.channel.send(msg)
    if message.content.startswith("!Divide "):
        vals=message.content.split(" ")
        x=int(vals[1])
        y=int(vals[3])
        res=x/y
        res1=x%y
        msg="Facilingo loco es "+str(res)+" y el residuo es "+str(res1)
        await message.channel.send(msg)

client.run(token)
