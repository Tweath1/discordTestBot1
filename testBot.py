import discord
import requests
from bs4 import BeautifulSoup
import os
import datetime
from discord.ext import commands

with open('token.txt', 'r') as file: #gets token from file that is not on github, but is on host server
    token = file.readline()

if __name__ == '__main__':
    print("hello world")

    intents = discord.Intents.all()
    client = commands.Bot(command_prefix="$", intents = intents)
    # client = discord.Client(intents=intents)

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

    # @client.command()
    # async def mute(ctx):
    #     if ctx.message.content == "$mute help":
    #         await ctx.send("To mute someone, type $mute followed directly by a user's ID")
    #         return
    #
    #     guild = ctx.message.guild
    #     timeoutRole = guild.get_role(839236832398671913)
    #
    #     try:
    #         message_content = ctx.message.content.split()
    #         user_id = message_content[1]
    #         user = await ctx.message.guild.fetch_member(user_id)
    #     except:
    #         await ctx.send("To mute someone, type $mute followed directly by a user's ID")
    #         return
    #
    #     await user.add_roles(timeoutRole)

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
