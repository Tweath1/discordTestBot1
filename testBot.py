import discord
import requests
from bs4 import BeautifulSoup
import os
import datetime

with open('token.txt', 'r') as file: #gets token from file that is not on github, but is on host server
    token = file.readline()




def split_by_char(string): #this function splits a string up into a list of its elements. It will be deleted a little later after redesigning its
  charList = []            #only use in the system
  for char in string:
    charList.append(char)
  return charList


def createPollEmbed(question): #this is a function to turn info from get_build into an embed that discord outputs
    embedVar = discord.Embed(color=0x7fffd4)
    embedVar.set_thumbnail(url="https://i.gyazo.com/881c313c685b52dd21ac8434dc87ad07.png")
    #embedVar.set_author(name=prettyGodName, url="https://smite.guru/builds/{}".format(godName), icon_url="https://static.smite.guru/i/champions/icons/{}.jpg".format(godName))
    embedVar.add_field(name=question, value="1:\n2:\n3:\n", inline=True)
    return embedVar


def mathStuff(equation):
    finalValue = 0
    num1 = float(equation[0])
    num2 = float(equation[2])
    operator = equation[1]

    if operator == "+":
        finalValue = num1 + num2
    if operator == "-":
        finalValue = num1 - num2
    if operator == "*" or operator == "x":
        finalValue = num1 * num2
    if operator == "/":
        finalValue = num1 / num2

    return finalValue


if __name__ == '__main__':
    print("hello world")

    intents = discord.Intents.all()
    client = discord.Client(intents=intents)

    @client.event
    async def on_connect():
        print("We have connected as {0.user}".format(client))


    @client.event
    async def on_ready():
        print("We have logged in as {0.user}".format(client))


    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith("$hello"):
            await message.channel.send("Hello!")

        if message.content.startswith("$test"):
            guild = message.guild
            await message.channel.send(guild.name)

        if message.content.startswith("$mute"):
            guild = message.guild
            message_content = message.content.split()
            if len(message_content) == 1:
                await message.channel.send("Please specify the user id of the user you would like to mute")
            else:
                user_id = message_content[1]
                timeoutRole = guild.get_role(839236832398671913)
                user = await message.guild.fetch_member(user_id)
                await user.add_roles(timeoutRole)

        if message.content.startswith("$unmute"):
            guild = message.guild
            message_content = message.content.split()
            if len(message_content) == 1:
                await message.channel.send("Please specify the user id of the user you would like to unmute")
            else:
                user_id = message_content[1]
                timeoutRole = guild.get_role(839236832398671913)
                user = await message.guild.fetch_member(user_id)
                await user.remove_roles(timeoutRole)

        if message.content.startswith("$kick"):
            guild = message.guild
            message_content = message.content.split()
            if len(message_content) == 1:
                await message.channel.send("Please specify the user id of the user you would like to kick")
            else:
                user_id = message_content[1]
                user = await message.guild.fetch_member(user_id)
                await guild.kick(user)

        if message.content.startswith("$rolekick"):
            guild = message.guild
            message_content = message.content.split()
            membersList = guild.members
            print(guild.members)
            if len(message_content) == 1:
                await message.channel.send("Please specify the role id of the roles you would like to kick")
            else:
                kickedRoleID = int(message_content[1])
                kickedRole = guild.get_role(kickedRoleID)
                #await message.channel.send(kickedRole.name)
                for member in membersList:
                    #await message.channel.send(membersList)
                    currentMemberRoleList = member.roles
                    for role in currentMemberRoleList:
                        if role == kickedRole:
                            #await message.channel.send("has role")
                            await guild.kick(member)
                        #else:
                            #await message.channel.send("does not have role")

        if message.content.startswith("$ban"):
            guild = message.guild
            message_content = message.content.split()
            if len(message_content) == 1:
                await message.channel.send("Please specify the role id of the roles you would like to ban")
            else:
                user_id = message_content[1]
                user = await message.guild.fetch_member(user_id)
                await guild.ban(user)

    client.run(token)
