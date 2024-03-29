from discord.ext import commands

TOKEN = "[INSERT BOT TOKEN HERE]"

client = commands.Bot(command_prefix='.')

admin_list = [""[ADMIN_USER_ID]", "[ADMIN_USER_ID]", "[ADMIN_USER_ID]"]


@client.event
async def on_ready():
    print("Bot is ready.")


@client.event
async def on_message(message):
    if message.channel == client.get_channel("501385723610660864"):
        channel_name = message.channel
        author = message.author
        content = message.content
        if author.bot:
            return
        print("{} said '{}' in {}".format(author, content, channel_name))
        await client.add_reaction(message, "\U00002B06")
        await client.add_reaction(message, "\U00002B07")


@client.event
async def on_reaction_add(reaction, user):
    emoji = reaction.emoji
    check_box = "\U00002611"
    channel = reaction.message.channel
    feedback = client.get_channel("501385723610660864")
    if emoji == check_box and channel == feedback and user.id in admin_list:
        print("{} reacted to '{}' with {}".format(user, reaction.message.content, emoji))
        await client.clear_reactions(reaction.message)
        await client.add_reaction(reaction.message, "\U00002611")

client.run(TOKEN)
