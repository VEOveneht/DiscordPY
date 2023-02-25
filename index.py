import discord
from discord.ext import commands

PREFIX = 'v'
TOKEN = 'MTA0OTcwMjA0NjE3OTI2NjU4MA.G-NCl8.15Ldt4x722eqJgvS6CjZm1ALyvVBhLNuSNginc'
KASAR = "JANGAN KASAR!"


class MyBot(commands.Bot):
    def __init__(self, *args, **kwargs):
        intents = discord.Intents().all()
        super().__init__(*args, intents=intents, **kwargs)


bot = MyBot(command_prefix=PREFIX)


@ bot.event
async def on_ready():
    print(f'Connected: {bot.user.name}')


def on_disconnect():
    print(f'Reconnecting...')


# UTAMA
@ bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # With prefix and Without prefix
    if message.content.startswith(PREFIX):

        # Handle messages with prefix
        cmd = message.content[len(PREFIX):].split()[0].lower()
        if cmd == "hello":
            await message.add_reaction('\U0001F44D')
            await message.reply(f"Hewoo^^")
            # await message.channel.send(f"Hewoo^^ {message.author.mention}!")
        # Menu List
        if cmd == "menu":
            # Kirim pesan Menu
            await message.add_reaction('📜')
            menu = await message.reply("Please choose an option:\n1. Games")
            # Menambahkan emoji ke Menu
            await menu.add_reaction("1️⃣"), await menu.delete(delay=3)

            # Tunggu pengguna Klik emoji
            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ["1️⃣"]
            reaction, user = await bot.wait_for("reaction_add", check=check)
            # handle the user's choice
            if reaction.emoji == "1️⃣":
                await message.reply("Here are some games!")

        # Help List
        if cmd == "help":
            await message.add_reaction('🏳')
            help = await message.reply("Please choose an option: \n1. Prefix")
            await help.add_reaction("1️⃣"), await help.delete(delay=3)

            def check(reaction, user):
                return user == message.author and str(reaction.emoji) in ["1️⃣"]
            reaction, user = await bot.wait_for("reaction_add", check=check)
            if reaction.emoji == "1️⃣":
                pre = await message.reply("The prefix is 'v'")
                await pre.delete(delay=10)
    else:
        # Handle messages without prefix
        if "anjing" in message.content.lower():
            await message.add_reaction('😠'), await message.reply(f"{KASAR}!")
    print(
        f'{message.author.name}#{message.author.discriminator} sent a message: {message.content}')


@bot.event
async def on_member_join(member):
    # ID channel tempat pesan selamat datang akan dikirim
    channel = bot.get_channel(1078891935533629591)
    # pesan selamat datang yang akan dikirim
    welcome = await channel.send(f"Selamat datang di server kami! {member.mention}")
    await welcome.add_reaction('👋')


bot.run(TOKEN)
