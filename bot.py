#!/bin/python3.6
import discord
import asyncio
import toml as toml2
import pytoml as toml

from key import key as get_key

client   = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    print("USER    : " + str(message.author))
    print("CHANNEL : " + str(message.channel))
    print("MESSAGE : \n" + str(message.content))
    print("-------------------------------------------------------------\n")

    if message.content.startswith('~hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.author, msg)

    elif (message.content.startswith('~coucou')):
        msg = '#coucou {0.everyone.mention}'
        await client.send_message(message.channel, msg)

    elif (message.content.startswith('~spam')):
        msg = 'faggot {0.author.mention}'.format(message)
        await client.send_message(message.author, msg)

    elif (message.content.startswith('~sleep')):
        msg = str(message.content.split(' ')[1])
        await client.send_message(message.channel, 'Sleeping for {} sec.'.format(int(msg)))
        if (int(msg) < 3600):
            await asyncio.sleep(int(msg))
            await client.send_message(message.channel, 'Done sleeping')
        else :
            await client.send_message(message.channel, 'NOPE Fuck you')

    elif message.content.startswith('~deleteme'):
        msg = await client.send_message(message.channel, "Vous savez, moi je ne crois pas qu'il y ait de bonnes ou de mauvaises situations. Moi si je devais résumer ma vie, aujourd'hui, avec vous, je dirais que c'est d'abord des rencontres, des gens qui m'ont tendu la main, peut-être à un moment où je ne pouvais pas, où j'étais seul chez moi, et c'est assez curieux de se dire que les hasards, les rencontres forgent une destinée, parce que quand on a le goût de la chose, quand on a le goût de la chose bien faite, le beau geste, parfois on ne trouve pas l'interlocuteur en face, je dirais le miroir qui vous aide à avancer ; alors ce n'est pas mon cas comme je le disais là, puisque moi au contraire j'ai pu et je dis merci à la vie, je lui dis merci, je chante la vie, je danse la vie, je ne suis qu'amour, et finalement quand beaucoup de gens aujourd'hui me disent : Mais comment fais-tu pour avoir cette humanité ? Et bah je leur réponds très simplement, je leur dis : c'est ce goût de l'amour, ce goût donc qui m'a poussé, aujourd'hui, à entreprendre une construction mécanique mais demain, qui sait, peut-être, simplement à me mettre au service de la communauté, à faire le don, le don de soi...faggot")
        await asyncio.delete_message(msg)

    elif message.content.startswith("~pin"):
        msg = (" ".join(message.content.split()[1:]))
        await client.pin_message(msg, message.channel)

    elif message.content.startswith("~pylone"):
        if (member_has_role(message.author, "pylone") == True):
            string = str(message.content.split(' ')[1])
            if (string == '-n'):
                msg = message.content[10:] + "@everyone"
                await client.send_message(message.channel, msg)
        else:
            if (string == "-prix"):
                fichier = open("prix.toml")
                toml(ficher)



@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    s = client.get_server('296727226572079118')
    tab = []
    list_role = []
    for role in s.roles:
        list_role.append(str(role))

    for member in s.members:
        for role in member.roles:
            tab.append(str(member) + ';' + str(role.name))

def member_has_role(member, role_name):
    return role_name in map(lambda x: x.name, member.roles)

config = []
with open("serveur.config") as conffile:
    for ligne in conffile.readlines():
        config.append(ligne)
print (str(config[0].split("=")[1]))
client.run(get_key())
