import discord
import requests
from bs4 import BeautifulSoup
import os

with open('token.txt', 'r') as file: #gets token from file that is not on github, but is on host server
    token = file.readline()




def split_by_char(string): #this function splits a string up into a list of its elements. It will be deleted a little later after redesigning its
  charList = []            #only use in the system
  for char in string:
    charList.append(char)
  return charList


def createItemBuildEmbed(godName, itemString): #this is a function to turn info from get_build into an embed that discord outputs
    prettyGodName = ""
    prettyGodNameList = godName.split("-")
    for index in range(len(prettyGodNameList)):
        prettyGodNameList[index] = prettyGodNameList[index].capitalize()
    for item in prettyGodNameList:
        prettyGodName = prettyGodName + item + " "
    embedVar = discord.Embed(color=0x7fffd4)
    embedVar.set_thumbnail(url="https://static.smite.guru/i/champions/icons/{}.jpg".format(godName))
    embedVar.set_author(name=prettyGodName, url="https://smite.guru/builds/{}".format(godName), icon_url="https://static.smite.guru/i/champions/icons/{}.jpg".format(godName))
    embedVar.add_field(name="Here are the 6 most popular items for {}".format(prettyGodName), value=itemString, inline=True)
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

    client = discord.Client()


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

        if message.content.startswith("$tierlist"):
            tierlistEmbed = discord.Embed(color=0x7fffd4)
            tierlistEmbed.set_thumbnail(url="https://i.gyazo.com/3a842d3c9a7e1a6f3bc2b6588f0ca548.png")
            #tierlistEmbed.set_author(name=prettyGodName, url="https://smite.guru/builds/{}".format(godName),
            #                   icon_url="https://static.smite.guru/i/champions/icons/{}.jpg".format(godName))
            #tierlistEmbed.add_field(name="Here are the 6 most popular items for {}".format(prettyGodName), value=itemString,
            #                   inline=True)
            await message.channel.send(embed=tierlistEmbed)

        if message.content.startswith("$hello"):
            await message.channel.send("Hello friends")

        if message.content.startswith("$math"):
            equation = message.content.split()
            equation.pop(0)
            await message.channel.send(mathStuff(equation))

        if message.content.startswith("$test"):
            guild = message.guild
            await message.channel.send(guild.name)

        if message.content.startswith("$kick"):
            guild = message.guild
            message_content = message.content.split()
            user_id = message_content[1]
            user = await message.guild.fetch_member(user_id)
            await guild.kick(user)

            await message.channel.send(guild.name)

    client.run(token)
