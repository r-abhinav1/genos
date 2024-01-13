import discord
import os
import random
import keep_alive
from discord.ext import commands
from aiohttp import request
from replit import db
import requests
import time
import json

client = commands.Bot(command_prefix='-')

token = os.environ['token']

imdb = os.environ['imdb']

a = 829592037552553994


@client.event
async def on_ready():
    e = discord.Embed(title='Genos is now online', color=0xFF0000)
    e.set_image(
        url=
        'https://i.pinimg.com/originals/ca/94/4b/ca944b18f7674274ba3bcabfa0621667.jpg'
    )
    gen = client.get_channel(829592037552553994)
    await gen.send(embed=e)


###########################CONVERSATION MODULE##############################################################################
@client.event
async def on_message(message):
    typ = message.channel.id
    if message.content.lower() in ('hi genos', 'sup genos', 'yo genos',
                                   'hello genos', 'hey genos', 'howdy'):
        general = client.get_channel(typ)
        response = random.choice([
            'Hi', 'Hello', 'Yo', 'Sup', 'Moshi Moshi', 'Konichiwa', 'Howdy',
            'hey'
        ])
        reply = random.choice(['How are you', 'How are you doing'])
        spac = '  '
        punc = '?'
        punc2 = ','
        mention = message.author.mention
        resp = response + spac + mention
        rep = reply + punc2 + mention + punc
        await general.send(resp)

    elif message.content.lower() in ('mornin genos', 'good morning genos',
                                     'ohayo genos', 'ohayo gosaimasu genos'):
        general = client.get_channel(typ)
        response = random.choice(
            ['Mornin', 'Good Morning', 'ohayo', 'ohayo gosaimasu'])
        spac = '  '
        mention = message.author.mention
        resp = response + spac + mention
        await general.send(resp)

    elif message.content.lower() in ('good afternoon genos',
                                     'afternoon genos'):
        general = client.get_channel(typ)
        response = random.choice(['good afternoon', 'afternoon'])
        spac = '  '
        mention = message.author.mention
        resp = response + spac + mention
        await general.send(resp)

    elif message.content.lower() in ('evening genos', 'good evening genos',
                                     'konbonwa genos'):
        general = client.get_channel(typ)
        response = random.choice(['evening', 'good evening', 'konbonwa'])
        spac = '  '
        mention = message.author.mention
        resp = response + spac + mention
        await general.send(resp)

    elif message.content.lower() in ('good night genos', 'night genos',
                                     'oyasuminasai genos'):
        general = client.get_channel(typ)
        response = random.choice([
            'good night',
            'night',
            'oyasuminasai',
        ])
        spac = '  '
        mention = message.author.mention
        resp = response + spac + mention
        await general.send(resp)

    elif message.content.lower() in ('bye genos', 'later genos',
                                     'sayonara genos',
                                     'matta athode ne genos'):
        general = client.get_channel(typ)
        response = random.choice(
            ['bye', 'later', 'sayonara', 'matta athode ne'])
        spac = '  '
        mention = message.author.mention
        resp = response + spac + mention
        await general.send(resp)

    elif message.content.lower() == 'introduce yourself':
        general = client.get_channel(typ)

        tembed = discord.Embed(title='Introducing Myself',
                               description='My name is Genos',
                               color=0xFF0000)
        tembed.add_field(name='Created by', value='Abhinav', inline=True)
        tembed.add_field(name='Date of Creation',
                         value='12/04/2021',
                         inline=True)
        tembed.add_field(name='Favourite food',
                         value='Brain cells',
                         inline=True)
        tembed.add_field(name='Hobbies', value='Watching anime', inline=True)
        tembed.add_field(name='Favourite anime character',
                         value='Itachi',
                         inline=True)
        tembed.add_field(name='Goal', value='Go to isekai', inline=True)
        tembed.set_author(name='Genos')

        await general.send(embed=tembed)
    elif message.content == 'per':
        ar = discord.Embed(title='hi')
        ar.set_thumbnail(url=message.author.avatar_url)
        general = client.get_channel(typ)
        await general.send(embed=ar)

    await client.process_commands(message)


######################################################MODERATION MODULE#######################################33##############
@client.command()
async def clear(ctx, arg: int):
    await ctx.channel.purge(limit=(arg + 1))


#####################################################CODEHELP MODULE#########################################################
@client.command()
async def codeh(ctx, arg):
    if arg == 'list':
        are = discord.Embed(
            title='Lists',
            description=
            'A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.\nIt is enclosed by square brackets[]',
            color=0X5A0CF5)
        are.add_field(
            name='l.append(a)',
            value=
            'Adds ,a, at the end of the list(only one element can be added to the list)',
            inline=False)
        are.add_field(name='l.extend()',
                      value='Adds a list of items at the of list l',
                      inline=False)
        are.add_field(name='l.insert(index)',
                      value="Inserts an element in the index 'a'",
                      inline=False)
        are.add_field(name='l.pop(index)',
                      value="Removes the element with the mentioned index",
                      inline=False)
        are.add_field(
            name='l.remove(element)',
            value=
            'Removes the element mentioned(If multiple are present,it removes the first occuring element)',
            inline=False)
        are.add_field(name='len(l)',
                      value="Prints the number of elements in the list 'l'",
                      inline=False)
        are.add_field(
            name='l.index(element)',
            value=
            'Prints the index of the element(If multiple are present,it prints the index of the first element)',
            inline=False)
        are.add_field(
            name='l.count(element)',
            value='Prints the number of times an element occurs in the list',
            inline=False)
        are.add_field(name='sum(l)',
                      value='Prints the sum of all elements in the list',
                      inline=False)
        are.add_field(name='max(l)',
                      value='Prints the largest element in the list',
                      inline=False)
        are.add_field(name='min(l)',
                      value='Prints the smallest element in the list',
                      inline=False)
        are.add_field(name='l.reverse()',
                      value='Reverses the order of elements in the list',
                      inline=False)
        are.add_field(
            name='l.sort()',
            value='Arranges all elements in the list into ascending order',
            inline=False)
        are.add_field(name='l.sort(reverse=False)',
                      value='Prints all all in descending order',
                      inline=False)
        are.set_author(name="Here, 'l' is list")
        are.set_thumbnail(
            url=
            'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png'
        )
        await ctx.send(embed=are)

    elif arg == 'str':
        are = discord.Embed(
            title='Strings',
            description=
            'A string in Python is a sequence of characters\nStrings are immutable.',
            color=0X5A0CF5)
        are.add_field(name='str.capitalize()',
                      value='Converts the first character to Capital letter',
                      inline=False)
        are.add_field(name='str.find(a)',
                      value='Returns with the index of "a" in the string ',
                      inline=False)
        are.add_field(
            name='str.isalnum()',
            value=
            "Returns with 'True'if the string has both alphabets and numbers",
            inline=False)
        are.add_field(
            name='str.isalpha()',
            value="Returns with 'True' if the string has only alphabets",
            inline=False)
        are.add_field(
            name='str.isdigit()',
            value="Returns with 'True' if the string has only numbers",
            inline=False)
        are.add_field(
            name='str.islower()',
            value=
            "Returns with 'True' if the letters in string are all in lower case ",
            inline=False)
        are.add_field(
            name='str.isupper()',
            value=
            "Returns with 'True'if the letters in string are all in upper case",
            inline=False)
        are.add_field(
            name='str.isspace()',
            value="Returns with 'True' if the string has only spaces",
            inline=False)
        are.add_field(name='str.upper()',
                      value='Returns the given string in uppercase characters',
                      inline=False)
        are.add_field(
            name='str.lower()',
            value='Returns the given strings in lowercase characters',
            inline=False)
        are.add_field(
            name='str.lstrip(a)',
            value=
            'Removes all occurances of "a" from left side of the given string',
            inline=False)
        are.add_field(
            name='str.rstrip(a)',
            value=
            'Removes all occurances of "a" from right side of the given string ',
            inline=False)
        are.add_field(
            name='str.strip(a)',
            value='Removes all occurances of "a" from the given list',
            inline=False)
        are.add_field(
            name='str.replace(old,new,count)',
            value=
            'old=characters that getting replaced\nnew=character that is replacing\ncount=frequency of the new term\nReplaces characters with the desired character in the string',
            inline=False)
        are.add_field(name='str.istitle()',
                      value='Checks for uppercase characters in the string',
                      inline=False)
        are.add_field(
            name='min(str)',
            value='Returns with the character with the least ASCII value',
            inline=False)
        are.add_field(
            name='max(str)',
            value='Returns with the character with the least ASCII value',
            inline=False)
        are.add_field(
            name='len(str)',
            value='Returns with the number of characters in the string',
            inline=False)
        are.set_thumbnail(
            url=
            'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png'
        )
        are.set_author(name="Here, 'str' is string")
        await ctx.send(embed=are)
    elif arg == 'dict':
        tio = discord.Embed(
            title='Dictionaries',
            description=
            'Dictionary in Python is an unordered collection of data values, used to store data values like a map',
            color=0X5A0CF5)
        tio.add_field(
            name='len(dict)',
            value=
            'Returns with the number of key:value pairs in the dictionary',
            inline=False)
        tio.add_field(
            name='dict() ',
            value='Creates a dictionary out of a sequence of (key,value) pairs',
            inline=False)
        tio.add_field(name='dict.keys()',
                      value='Displays all the keys in the dictionary',
                      inline=False)
        tio.add_field(name='dict.values()',
                      value='Displays all the values in the dictionary',
                      inline=False)
        tio.add_field(
            name='dict.items()',
            value=
            'Makes a list of tuple containing (key,value)pairs and displays',
            inline=False)
        tio.add_field(name='dict.get(key)',
                      value='Gets the value stored in the corresponding key',
                      inline=False)
        tio.add_field(name='dict.update(dict1)',
                      value='Adds all the key:value pairs from dict1 to dict',
                      inline=False)
        tio.add_field(name='dict.clear()',
                      value='Clears all the values from the given dictionary',
                      inline=False)
        tio.add_field(name='del dict(key)',
                      value='Deletes the item with the given key',
                      inline=False)
        tio.set_thumbnail(
            url=
            'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png'
        )
        await ctx.send(embed=tio)


###################################################################API MODULE################################################


@client.command()
async def send(ctx, arg):
    if arg == 'meme':
        url = 'https://some-random-api.ml/meme'
        async with request("GET", url) as response:

            if response.status == 200:
                data = await response.json()
                ast = discord.Embed(title='Memes', color=0x00FF00)
                ast.set_image(url=data["image"])
                await ctx.send(embed=ast)
            else:
                await ctx.send('ERROR.Please try again')
    elif arg == 'cat':
        url = 'https://some-random-api.ml/img/cat'
        async with request("GET", url) as response:

            if response.status == 200:
                data = await response.json()
                ast = discord.Embed(title='Cats', color=0x00FF00)
                ast.set_image(url=data["link"])
                await ctx.send(embed=ast)
            else:
                await ctx.send('ERROR.Please try again')
    elif arg == 'dog':
        url = 'https://some-random-api.ml/img/dog'
        async with request("GET", url) as response:

            if response.status == 200:
                data = await response.json()
                ast = discord.Embed(title='dogs', color=0x00FF00)
                ast.set_image(url=data["link"])
                await ctx.send(embed=ast)
            else:
                await ctx.send('ERROR.Please try again')


@client.command()
async def mov(ctx, *args):
    movie = ''
    for i in args:
        movie = movie + '%20' + i

    url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/search/" + movie

    headers = {
        'x-rapidapi-key': imdb,
        'x-rapidapi-host':
        "imdb-internet-movie-database-unofficial.p.rapidapi.com"
    }
    async with request("GET", url, headers=headers) as response:
		if response.status == 200:
      li =await response.json()
      dic = li[0]		
      code = dic["id"]

			url = "https://imdb-internet-movie-database-unofficial.p.rapidapi.com/film/" + code

			headers = {
			    'x-rapidapi-key':
			    imdb,
			    'x-rapidapi-host':
			    "imdb-internet-movie-database-unofficial.p.rapidapi.com"
			}

			respons = requests.request("GET", url, headers=headers)
			res = respons.json()

			ar = discord.Embed(title=res['title'], description=res['plot'])
			ar.set_image(url=res['poster'])
			ar.add_field(name='Rating', value=res['rating'], inline=False)
			ar.add_field(name='Length', value=res['length'], inline=False)

			await ctx.send(embed=ar)
		else:
			await ctx.send('404 ERROR')


#############################################################DATABASE MODULE##################################################


@client.command()
async def store(ctx, *args):
    if args[0] != 'random':
        bcv = ''
        spc = ' '
        for i in range(1, len(args)):
            bcv = bcv + args[i] + spc
        val = bcv
        key = str(args[0])
        if key in db.keys():
            ae = discord.Embed(title=key + ' already exists', color=0XFF0000)
            await ctx.send(embed=ae)
        else:
            db[key] = val
            re = discord.Embed(title=key + ' is successfully stored',
                               color=0x31DCBD)
            await ctx.send(embed=re)
    else:
        uyt = discord.Embed(
            title="Can't store the value as'random'.Please try something else",
            color=0XFF0000)
        await ctx.send(embed=uyt)


@client.command()
async def change(ctx, *args):
    if len(args) != 0:
        if args[0] in db.keys():
            if args[1] in db.keys():
                ture = discord.Embed(title=args[1] +
                                     ' already exists in database',
                                     color=0XFF0000)
                await ctx.send(embed=ture)
            else:
                trq = str(db[args[0]])
                db[args[1]] = trq
                del db[args[0]]
                tyru = discord.Embed(title=args[0] +
                                     ' is successfully changed to ' + args[1],
                                     color=0X00FF00)
                await ctx.send(embed=tyru)
        else:
            uty = discord.Embed(title=args[0] + ' doesnt exist in database',
                                color=0XFF0000)
            await ctx.send(embed=uty)
    else:
        tur = discord.Embed(title='Please type the changes you want to make',
                            color=0XFF0000)
        await ctx.send(embed=tur)


@client.command()
async def get(ctx, *args):
    if len(args) != 0:
        if args[0] != 'random':

            if args[0] in db.keys():
                aui = db[args[0]]
                await ctx.send(aui)
            else:

                art = discord.Embed(title=args[0] + ' doesnt exist',
                                    color=0XFF0000)
                await ctx.send(embed=art)
        else:
            keys = db.keys()
            oni = list(keys)
            at = len(oni)
            if at == 0:
                ytur = discor.Embed(title='The database is empty',
                                    color=0XFF0000)
                await ctx.send(embed=ytur)
            elif at == 1:
                ytr = discor.Embed(title='There is only one value in database',
                                   color=0XFF0000)
                await ctx.send(embed=ytr)
            else:
                huy = random.randint(1, at)
                yut = str(oni[huy - 1])
                await ctx.send(yut)
    else:
        tuyr = discord.Embed(title='You have to type the key to get value',
                             color=0XFF0000)
        await ctx.send(embed=tuyr)


@client.command()
async def getnum(ctx, arg: int):
    keys = db.keys()
    one = list(keys)
    at = len(one)
    if at >= arg:
        atp = str(one[arg - 1])
        ayu = db[atp]
        await ctx.send(ayu)
    else:
        tyir = discord.Embed(
            title=
            'The given number is greater than the number of data in the database',
            color=0XFF0000)
        await ctx.send(embed=tyir)


@client.command()
async def dele(ctx, arg: str):
    if arg in db.keys():
        del db[arg]
        re = discord.Embed(title=arg + ' is successfully deleted',
                           color=0xCF0029)
        await ctx.send(embed=re)

    elif arg == 'all':
        keys = db.keys()

        if len(keys) != 0:
            for i in keys:
                del db[i]
            art = discord.Embed(title='All the data deleted successfully',
                                color=0X00FF00)
            await ctx.send(embed=art)

        else:
            arty = discord.Embed(title='The database is empty', color=0XFF0000)
            await ctx.send(embed=arty)
    else:
        tuyr = discord.Embed(title='Given value title doesnt exist',
                             color=0XFF0000)
        await ctx.send(embed=tuyr)


@client.command()
async def delenum(ctx, arg: int):
    keys = db.keys()
    on = list(keys)
    at = len(on)
    if at >= arg:
        atr = str(on[arg - 1])
        del db[atr]
        tuy = discord.Embed(title=atr + ' is successfully deleted',
                            color=0X00FF00)
        await ctx.send(embed=tuy)
    else:
        tuy = discord.Embed(
            title=
            'The given number is more than the number of elements in database',
            color=0XFF0000)
        await ctx.send(embed=tuy)


@client.command()
async def all(ctx):
    keys = db.keys()
    car = list(keys)
    cart = []
    #for i in car:
    #if i[:3] in ['a3b','b9c']:
    # return
    #else:
    # cart.append(i)
    if len(cart) != 0:
        aty = discord.Embed(title='All stored values', color=0XD4EF0D)
        atr = (len(cart) + 1)
        for i in range(1, atr):
            adf = str(i)
            po = '.'
            aty.add_field(name=adf + po, value=cart[i - 1], inline=False)
        await ctx.send(embed=aty)

    else:
        atr = discord.Embed(title='Database is empty', color=0XFF0000)
        await ctx.send(embed=atr)


########################################################HELP COMMAND MODULE################################################
@client.command()
async def assist(ctx, *agrs):
    if len(agrs) != 0:
        if agrs[0] == 'codeh':
            tueie = discord.Embed(
                title='All "code help" related commands',
                description=
                'Code help commands have most commonly used syntaxes. They can be used for reference while coding',
                color=0x18F1EE)
            tueie.add_field(
                name='-codeh list',
                value='Shows most of the list manipulation syntaxes',
                inline=False)
            tueie.add_field(
                name='-codeh str',
                value='Shows most of the string manipulation syntaxs',
                inline=False)
            tueie.add_field(name='-codeh dict',
                            value='Shows dictionary manipulation syntaxes',
                            inline=False)
            tueie.set_thumbnail(
                url=
                'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/768px-Python-logo-notext.svg.png'
            )
            await ctx.send(embed=tueie)
        elif agrs[0] == 'send':
            uyr = discord.Embed(title='All APIs related commands',
                                description='Sends desired images from APIs',
                                color=0X18F1EE)
            uyr.add_field(name='-send meme', value='Sends memes', inline=False)
            uyr.add_field(name='-send cat',
                          value='Sends cat images',
                          inline=False)
            uyr.add_field(name='-send dog',
                          value='Sends dog images',
                          inline=False)
            uyr.set_thumbnail(
                url=
                'https://qph.fs.quoracdn.net/main-qimg-999b788fcdd27ea1768c5d57f96b8e33'
            )
            await ctx.send(embed=uyr)
        elif agrs[0] == 'db':
            tuy = discord.Embed(
                title='All database related commands',
                description=
                'Database can be used to store "values" in "key" to retrieve the information stored later. Although value can be anything from links to sentences,key can only be one word,that is letters with either numbers or characters or neither of them.Also,key cannot be the word "random".',
                color=0X18F1EE)
            tuy.add_field(
                name='-store key value',
                value=
                'Stores "value" into "key". key can be used to retrieve value later',
                inline=False)
            tuy.add_field(
                name='-change existing_key new_key',
                value=
                'changes the "existing key" into new desired key. The value in the key remains same',
                inline=False)
            tuy.add_field(
                name='-all',
                value=
                'Displays all keys in database with serial numbers.These S.No can be used later to retrieve values ',
                inline=False)
            tuy.add_field(name='-get key',
                          value='displays the value stored in the "key"',
                          inline=False)
            tuy.add_field(name='-get random',
                          value='Gets a random value from the database.',
                          inline=False)
            tuy.add_field(
                name='-getnum S.no',
                value='Gets the value store in the key with the entered S.No',
                inline=False)
            tuy.add_field(
                name='-dele key',
                value=
                'Deletes the key and the value stored in it from database',
                inline=False)
            tuy.add_field(
                name='-dele all',
                value='Deletes all the keys and values from database',
                inline=False)
            tuy.add_field(
                name='-delenum S.No',
                value='Deletes the value and key with the entered S.No ',
                inline=False)
            tuy.set_thumbnail(
                url=
                'https://thumbs.dreamstime.com/b/database-complex-like-puzzle-pictured-as-word-database-puzzle-pieces-to-show-database-can-be-difficult-needs-164222439.jpg'
            )
            await ctx.send(embed=tuy)
        elif args[0] == 'mod':
            tuy = discord.Embed(
                title='All moderation and server controlling commands',
                color=0X18F1EE)
            tuy.add_field(name='-clear n',
                          value='clears n messages in that particular channel',
                          inline=False)
            await ctx.send(embed=tuy)
        elif args[0] == 'game':
            tuy = discord.Embed(title='All gaming commands')
            ruy.add_field(name='-hn', value='Starts hangman', inline=False)
            ruy.add_field(name='stop',
                          value='stops game(no "-")',
                          inline=False)
            ruy.add_field(name='-top',
                          value='shows all   scores',
                          inline=False)
            await ctx.send(embed=ruy)
    else:
        tur = discord.Embed(
            title='All help commands',
            description=
            'These commands show all commands in their respective fields',
            color=0X18F1EE)
        tur.add_field(name='-assist codeh',
                      value='Shows all code help related commands',
                      inline=False)
        tur.add_field(name='-assist send',
                      value='Shows all API related commands',
                      inline=False)
        tur.add_field(name='-assist db',
                      value='Shows all database related commands',
                      inline=False)
        tur.add_field(name='-assist mod',
                      value='Shows all moderation commands',
                      inline=False)
        tur.add_field(name='-assist game',
                      value='Shows all game commands',
                      inline=False)
        #tur.add_thumbnail()
        await ctx.send(embed=tur)


@client.command()
async def datab(ctx):
    if len(list(db.keys())) != 0:
        for i in db.keys():
            await ctx.send(str(i) + '=' + str(db[i]))
    else:
        await ctx.send('nothing was there')


@client.command()
async def luffy(ctx):
    for i in db.keys():
        del db[i]
    await ctx.send('done')


#####################################################GAMES#####################################################
hp = [1, 2, 3, 4, 5, 6, 7]

hp1 = [
    'https://i.imgur.com/KBMsCp9.jpg', 'https://i.imgur.com/apN30T6.jpg',
    'https://i.imgur.com/w7QJQFH.jpg', 'https://i.imgur.com/UKiV6J9.jpg',
    'https://i.imgur.com/yHGrZqc.jpg', 'https://i.imgur.com/sAeTvqP.jpg',
    'https://i.imgur.com/cQmLMDO.jpg', 'https://i.imgur.com/hRzVg1N.jpg'
]

#last=max points i.e nobody
#first=zero no points

wor = os.environ['word']

allwords = []

dash = []
word = []
key = []
defi = []


@client.command()
async def hn(ctx):
    global ar
    ar = discord.Embed(title='Starting HangMan in 3sec...')  #color
    await ctx.send(embed=ar)
    time.sleep(3)
    await ctx.channel.purge(limit=1)

    url = "https://random-words-with-pronunciation.p.rapidapi.com/word"

    headers = {
        'x-rapidapi-key': str(wor),
        'x-rapidapi-host': "random-words-with-pronunciation.p.rapidapi.com"
    }

    async with request("GET", url, headers=headers) as response:
        dat = await response.json()
        data = dat[0]
        dad = data['word']
        a = dad.lower()
        deif = data['definition']
        c = a.replace('', ' ')
        b = len(a)
        da = ''
        for i in range(b):

            if a[i] == ' ':
                da = da + ' ' + '/'
            elif a[i] in ['a', 'e', 'i', 'o', 'u']:
                da = da + ' ' + '÷'
            else:

                da = da + ' ' + '-'
        ar = discord.Embed(
            title=
            f'It is a {len(a)} letter word.\nYou have {len(hp)}HP\n\ {da}\n\n(HINT-{deif})'
        )  #color
        ar.set_thumbnail(url='https://i.imgur.com/hRzVg1N.jpg')
        await ctx.send(embed=ar)
        key.append('32')
        dash.append(da)
        word.append(a)
        word.append(c)
        defi.append(deif)
        print(a)


@client.event
async def on_message(message):
    id = message.channel.id
    ctx = client.get_channel(id)
    player = str(message.author)
    if message.author == client.user:
        return

    if message.content.lower() == 'stop':
        wor = word[0]
        key.clear()
        dash.clear()
        word.clear()
        allwords.clear()

        for i in range(7 - len(hp)):
            hp.append(i)
        ar = discord.Embed(
            title=f'Game stopped.\nThe word was "{wor.capitalize()}"')
        await ctx.send(embed=ar)
    if message.content.lower() == 'hint':
        atr = discord.Embed(title=f'HINT={defi[0]}')
        await ctx.send(embed=atr)

    if '32' in key:
        if len(message.content) > 3:
            print('32')
        if message.content.lower() == 'stop':
            wor = word[0]
            key.clear()
            dash.clear()
            word.clear()
            allwords.clear()

            for i in range(7 - len(hp)):
                hp.append(i)
            ar = discord.Embed(
                title=f'Game stopped.\nThe word was "{wor.capitalize()}"')
            await ctx.send(embed=ar)

        global da
        global ad
        global keye
        global num
        tu = message.content.lower()
        a = word[0]
        c = word[1]
        da = dash[0]

        if len(message.content) == 1:

            if tu.isalpha():
                if tu in allwords:
                    ar = discord.Embed(title=f'You already tried "{tu}"')
                    await ctx.send(embed=ar)
                else:

                    allwords.append(tu)

                    if tu in c:

                        for i in range(len(c)):
                            ind = []
                            if tu == c[i]:

                                ind.append(i)
                                first = da[:ind[0]]
                                nex = da[(ind[0] + 1):]
                                da = first + tu + nex
                                if '/' in da:
                                    ada = da.replace(' ', '')
                                    ad = ada.replace('/', '')
                                else:
                                    ad = da.replace(' ', '')
                                dash.remove(dash[0])
                                dash.append(da)

                        if ad.isalpha():
                            key.remove('32')
                            url = hp1[len(hp)]
                            ar = discord.Embed(
                                title=
                                f'Congratulations,you guessed the word!You scored {len(hp) } points'
                            )
                            ar.add_field(name='Attempted Letters',
                                         value=allwords)  #color
                            ar.set_thumbnail(url=url)
                            await ctx.send(embed=ar)
                            dash.clear()
                            word.clear()
                            allwords.clear()
                            keye = 'a3b' + player
                            num = 'b9c' + player
                            if keye in db.keys():
                                prev = int(db[keye])
                                curr = prev + len(hp)
                                db[keye] = curr
                                nu = int(db[num])
                                db[num] = nu + 1

                            else:
                                db[keye] = str(len(hp))
                                db[num] = '1'
                            avg = str(int(db[keye]) / int(db[num]))
                            ac = discord.Embed(
                                title=f"{player}'s stats")  #color
                            ac.add_field(name='Current games score',
                                         value=f'{len(hp)}',
                                         inline=False)
                            ac.add_field(name='Total score',
                                         value=f'{db[keye]}',
                                         inline=False)
                            ac.add_field(name='Total games played',
                                         value=db[num],
                                         inline=False)
                            ac.add_field(name='Average score',
                                         value=avg,
                                         inline=False)

                            ac.set_thumbnail(url=message.author.avatar_url)
                            await ctx.send(embed=ac)

                            for i in range(7 - len(hp)):
                                hp.append(i)

                            return
                        else:
                            ar = discord.Embed(title=da)
                            ar.add_field(name='Attempted Letters',
                                         value=allwords)
                            ar.set_thumbnail(url=hp1[len(hp)])
                            await ctx.send(embed=ar)  #color
                            return

                    else:
                        hp.remove(hp[0])
                        if len(hp) != 0:
                            ar = discord.Embed(
                                title=
                                f'{tu} is not there in the word :( . You have {len(hp)} tries left'
                            )
                            ar.add_field(
                                name=da,
                                value=f'Attempted Letters\n{allwords}')
                            ar.set_thumbnail(url=hp1[len(hp)])
                            await ctx.send(embed=ar)

                        else:
                            key.remove('32')
                            ar = discord.Embed(
                                title=
                                f'The word is "{dad}". Better luck next time')
                            ar.set_thumbnail(
                                url='https://i.imgur.com/KBMsCp9.jpg')
                            await ctx.send(embed=ar)
                            dash.clear()
                            word.clear()
                            allwords.clear()
                            num = 'b9c' + player
                            keye = 'a3b' + player

                            if num in db.keys():
                                rt = int(db[num])
                                curr = rt + 1
                                db[num] = str(curr)
                            else:
                                db[num] = '1'
                            avg = str(int(db[keye]) / int(db[num]))
                            ac = discord.Embed(
                                title=f"{player}'s stats")  #color
                            ac.add_field(name='Current games score',
                                         value='0',
                                         inline=False)
                            ac.add_field(name='Total score',
                                         value=f'{db[keye]}',
                                         inline=False)
                            ac.add_field(name='Total games played',
                                         value=db[num],
                                         inline=False)
                            ac.add_field(name='Average score',
                                         value=avg,
                                         inline=False)
                            ac.set_thumbnail(url=message.author.avatar_url)
                            await ctx.send(embed=ac)

                            for i in range(1, 8):
                                hp.append(i)

            else:
                ar = discord.Embed(title=f'{tu} is not a letter')
                ar.add_field(name=da, value=f'Attempted Letters\n{allwords}')

                ar.set_thumbnail(url=hp1[len(hp)])
                await ctx.send(embed=ar)  #embed+pic+word

        else:
            ar = discord.Embed(title='Enter one letter at a time')
            ar.add_field(name=da, value=f'Attempted Letters\n{allwords}')

            ar.set_thumbnail(url=hp1[len(hp)])
            await ctx.send(embed=ar)  #embed+pic+word

            #embed+pic

    await client.process_commands(message)


@client.command()
async def top(ctx):
    global nakey
    nakey = []
    keys = list(db.keys())
    for i in range(len(keys)):

        tot = keys[i]

        if tot[:3] == 'a3b':
            nakey.append(tot[3:])
    global scor
    scor = []
    for i in nakey:

        scor.append(int(db['a3b' + i]))
    dic = {}
    for i in range(len(scor)):
        dic[scor[i]] = nakey[i]

    scor.sort(reverse=True)
    num = 'b9c'
    global ayr
    ayr = discord.Embed(title='LEADERBOARD')
    for i in scor:
        nu = db['b9c' + dic[i]]
        r = scor.index(i) + 1
        ayr.add_field(
            name=f'{r}.{dic[i]}',
            value=
            f'Score={i}\n->Number of games played-{nu}\n->Average={i/int(nu)}',
            inline=False)
    await ctx.send(embed=ayr)


keep_alive.keep_alive()
client.run(token)
