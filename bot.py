#!/bin/python3.6
""" Bot Discord """
import discord
import os

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if (message.content.startswith(">")):
        if (message.content.startswith(">repete")):
            tmp = await client.send_message(message.channel, message.content[7:])
        if (message.content.startswith(">ping")):
            print("ping")
            os.system("ping -c 1 8.8.8.8 > coucou")
            file = open("coucou", "r")
            await client.send_message(message.channel,file.read())
        if (message.content.startswith(">mp")):
            await client.send_message(message.author, "hey pd")


client.run("token")
