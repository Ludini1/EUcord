import discord
from discord.ext import commands

TOKEN = "NTA4Mjk0NDAxODE1MjE2MTI4.Dr9L6Q.pdqoyzUwlvbbCx22NRUYHr3kQw4"

client = commands.Bot(command_prefix='.')

admin_list = ["91114093598998528", "123563744314916865", "157151405960855553"]


@client.event
async def on_ready():
    print("Bot is ready.")


@client.command(pass_context=True)
async def make_all_member(ctx):
    serv = ctx.message.author.server
    role = discord.utils.get(serv.roles, name="member")
    for memb in serv.members:
        if role not in memb.roles:
            client.say("{} now a member".format(memb.name))
            await client.add_roles(memb, role)
    await client.say("All users have member role")

client.run(TOKEN)
