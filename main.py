import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive
from faker import *
from discord.ext import commands
import time
import string
import io
import wikipedia

client = discord.Client()


sad_words = [ "pakaya", "utto", "huth","lesbian", "lgbt", "wtf", "cringey", "manuka","boob", "pussy", "dickpic", "dick", "teengirl", "egirl", "sex", "esex", "online sex", "girlfriend", "suck a dick", "suckadick", "gay niger" ]

starter_encouragement = [
    "You are downbad person!",
    "You are fking GAY",
    "katawahapan kari ponnaya",
    "Manuka is a fking cringey person",
    "Please send me boob pic and pussy pics :)",
    "OHH! PLEASE FUK ME!",
    "STFU, YOU ARE DOG WATER",
    "YOU ARE LITERALLY PUSSY WATER",
    "Please stop talking little faggot, its annoying AF",
    "Good luck with your boob job"
]

if "responding" not in db.keys():
    db["responding"] = True

def get_quote():
    r = requests.get("https://zenquotes.io/api/random")
    json_data = json.loads(r.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return(quote)

def update_encouragements(encouraging_message):
    if "encouragements" in db.keys():
        encouragements = db["encouragements"]
        encouragements.append(encouraging_message)
        db["encouragements"] = encouragements
    else:
        db["encouragements"] = [encouraging_message]

def delete_encouragement(index):
    encouragements = db["encouragements"]
    if len(encouragements) > index:
        del encouragements[index]
        db["encouragements"] = encouragements

def ipinfoshit(ipfromuser):
        r = requests.get('http://ip-api.com/json/' + str(ipfromuser)) # include the ip
        data = r.json()
        ipinfo = f'\n[+] Status: {data["status"]} \n[+] Country: {data["country"]} \n[+] Country Code: {data["countryCode"]} \n[+] Region: {data["region"]} \n[+] Region Name: {data["regionName"]} \n[+] City: {data["city"]} \n[+] ZIP: {data["zip"]} \n[+] Latitude: {data["lat"]} \n[+] Longitude: {data["lon"]} \n[+] TimeZone: {data["timezone"]} \n[+] ISP: {data["isp"]} \n[+] Organization: {data["org"]} \n[+] ASN: {data["as"]} \n[+] Query: {data["query"]} \n'
        return ipinfo

def show_help():
  help_string = """Thank you for using 'Good Bot'
Available Commands - 
$hello -> Talk to the bot
$inspire -> Message an inspirational quote
$ip 24.48.0.1 -> will give information about 24.48.0.1 ip
$new Message Here -> will add any message after '$new ' to the message database
$help -> will show you this message
$inv -> will send the invite link to this bot!
$fake help -> will take you to the help page of Fake Info Generator
$mfp 3 -> will generate 3 fake profiles and send, any number is possible
$nitro 3 -> will generate 3 random nitro codes
$pervert -> will send a fun, perverty text
$color -> will generate random hex of a color
$btc -> will show the price of 1BTC
$info -> will show information about this discord bot
$dog -> send a random dog picture
$fox -> send a random fox picture
$covid -> get the current global covid information
$wiki Sri Lanka -> will send the first two sentenes about Sri Lanka in wikipedia
$bored -> will tell something to do, if you dont have any

Made by ZeaCeR#5641 :)
"""
  return help_string

def send_inv_link_to_server():
  inv_link = """https://discord.com/api/oauth2/authorize?client_id=856443669979856896&permissions=2148002880&scope=bot"""
  return inv_link

def FAKE_PROFILE(howmuchinfo):
  if howmuchinfo == "high":
    fake = Faker()
    simple_dict = fake.profile()
    fake_info_simple = "Name: " + str(simple_dict['name']) + "\nJob: " + str(simple_dict['job']) + "\nBirthdate: " + str(simple_dict['birthdate']) + "\nCompany: " + str(simple_dict['company']) + "\SSN: " + str(simple_dict['ssn']) + "\nRecidence: " + simple_dict['residence'] + "\nCurrent Location:" + str(simple_dict['current_location']) + "\nBlood Group: " + str(simple_dict['blood_group']) + "\nUsername: " + str(simple_dict['username']) + "\nAddress: " + str(simple_dict['address']) + "\nMail: " + str(simple_dict['mail'])
    return fake_info_simple

  elif howmuchinfo == "name":
    faker = Faker()
    try:
      USname = faker.name()
      return "Name: " + str(USname)
    except:
      return "Unable to generate a random name"

  elif howmuchinfo == "dob":
    faker = Faker()
    try:
      USdob = faker.date_of_birth()
      return "DOB: " + str(USdob)
    except:
      return "Unable to generate a random name"
  
  elif howmuchinfo == "addr":
    faker = Faker()
    try:
      USaddress = faker.address()
      return "Address: \n" + str(USaddress)
    except:
      return "Unable to generate a random address"
  
  elif howmuchinfo == "job":
    faker = Faker()
    try:
      USjob = faker.job()
      return "Job: " + str(USjob)
    except:
      return "Unable to generate a random job"
  
  elif howmuchinfo == "color":
    faker = Faker()
    try:
      USfavColor = faker.color_name()
      return "Color: " + str(USfavColor)
    except:
      return "Unable to generate a random color"
  
  elif howmuchinfo == "zipcode":
    faker = Faker()
    try:
      USzip = faker.zipcode()
      return "Zip Code: " + str(USzip)
    except:
      return "Unable to generate a random zipcode"
  
  elif howmuchinfo == "city":
    faker = Faker()
    try:
      UScity = faker.city()
      return "City: " + str(UScity)
    except:
      return "Unable to generate a random zipcode"
  
  elif howmuchinfo == "license plate":
    faker = Faker()
    try:
      USnumberPlate = faker.license_plate()
      return "Number Plate: " + str(USnumberPlate)
    except:
      return "Unable to generate a random license plate"

  elif howmuchinfo == "bban":
    faker = Faker()
    try:
      USbasicBankAccountNumber = faker.bban()
      return "Basic Bank Account Number: " + str(USbasicBankAccountNumber)
    except:
      return "Unable to generate a random Basic Bank Account Number"
  
  elif howmuchinfo == "iban":
    faker = Faker()
    try:
      USinternationalBankAccountNumber = faker.iban()
      return "International Bank Account Number: " + str(USinternationalBankAccountNumber)
    except:
      return "Unable to generate a random International Bank Account Number"
  
  elif howmuchinfo == "bs":
    faker = Faker()
    try:
      USbs = faker.bs()
      return "BS: " + str(USbs)
    except:
      return "Unable to generate a random BS"
  
  elif howmuchinfo == "cc":
    faker = Faker()
    try:
      UScreditcard = faker.credit_card_full()
      return "Credit Card: \n" + str(UScreditcard)
    except:
      return "Unable to generate a random Credit Card"
  
  elif howmuchinfo == "cemail":
    faker = Faker()
    try:
      UScompanyemail = faker.company_email()
      return "Email: " + str(UScompanyemail)
    except:
      return "Unable to generate a random Email"
  
  elif howmuchinfo == "pno":
    faker = Faker()
    try:
      USphoneNumber = faker.phone_number()
      return "Phone Number: " + str(USphoneNumber)
    except:
      return "Unable to generate a random Phone Number"
  
  elif howmuchinfo == "cp":
    faker = Faker()
    try:
      UScatchPhrase = faker.catch_phrase()
      return "Catch Phrase: " + str(UScatchPhrase)
    except:
      return "Unable to generate a random catch phrase"
  
  elif howmuchinfo == "ssn":
    faker = Faker()
    try:
      USssa = faker.ssn()
      return "SSN: " + str(USssa)
    except:
      return "Unable to generate a random SSN"
  
  elif howmuchinfo == "ua":
    faker = Faker()
    try:
      USuseragent = faker.ssn()
      return "User Agent: " + str(USuseragent)
    except:
      return "Unable to generate a random User Agent"
  
  elif howmuchinfo == "low":
    fake_low = Faker()
    shitthing_simple = fake_low.simple_profile()

    fake_info_low_info = "Name: " + str(shitthing_simple['name']) + "\nSex: " + str(shitthing_simple['sex']) + "\nAddress: " + str(shitthing_simple['address']) + "\nMail: " + str(shitthing_simple['mail']) + "\nBirthday: " + str(shitthing_simple['birthdate'])

    return fake_info_low_info
  
  elif howmuchinfo == "help":
    fake_help = """$fake high -> Generate a fake profile with high amount of  information
$fake name -> create a fake name
$fake dob -> create a fake Date of Birth
$fake addr -> create a fake address
$fake job -> create a fake job
$fake color -> create a fake color
$fake zipcode -> create a fake zipcode
$fake city -> create a fake city
$fake lp -> create a fake Lisence Number Plate
$fake bban -> create a random Basic Bank Account Number
$fake iban -> create a random International Bank Account Number
$fake bs -> create a fake BS / Degree
$fake cc -> create credit card details ( not valid )
$fake pno -> create a fake phone number
$fake cemail -> create a company email number
$fake cp -> create a random catch phrase
$fake ssn -> create a fake ssn number
    """
    return fake_help
  
  else:
    pass

def CREATE_FAKE_PROFILES_MANY():
  fake = Faker()
  simple_dict = fake.profile()
  fake_info_simple = "Name: " + str(simple_dict['name']) + "\nJob: " + str(simple_dict['job']) + "\nBirthdate: " + str(simple_dict['birthdate']) + "\nCompany: " + str(simple_dict['company']) + "\SSN: " + str(simple_dict['ssn']) + "\nRecidence: " + simple_dict['residence'] + "\nCurrent Location:" + str(simple_dict['current_location']) + "\nBlood Group: " + str(simple_dict['blood_group']) + "\nUsername: " + str(simple_dict['username']) + "\nAddress: " + str(simple_dict['address']) + "\nMail: " + str(simple_dict['mail'])
  return fake_info_simple

def show_pervert_text():
  pervert_text = """Can I get a booty pic with your panties on? And one without them on? Can I also get 3 different pics of your boobs in any position. Also can I get a pic of your pussy from the front and one where it’s spread open. Can I get a picture of you fingering your self? Can I get a pic of you doing a kissing face but with your boobs in it? Can I get a picture of your pussy and ass from behind in one shot? Can I also get a pic of your full front body in just a bra and panties? And can I get a pic of your ass when your pants are all the way up? Also can I get a pic of your boobs when you’re in the shower? Also can I get another pussy pic while you’re in the shower? For the rest of the pics can you just send whatever other sexy things you want? For the videos can I get a video of you twerking in really short shorts? And one of you fingering yourself? One of you actually cumming? Also can I get a video of you playing with your tits while not wearing a shirt? u be squirtin? or u on the cream team? what color the inside? your booty real wet? do it clap? do it fart? do it grip the meat? it’s tight? how many fingers u use? what it taste like? can i smell it? is it warm? it’s real juicy? do it drip? you be moaning?"""
  return pervert_text

def give_nice_codes():
  code = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
  return f'https://discord.gift/{code}'

def give_rand_color():
  randcolor = discord.Color(random.randint(0x000000, 0xFFFFFF))
  return randcolor

def get_bitcoin_status():
  r = requests.get('https://api.coindesk.com/v1/bpi/currentprice/btc.json').json()
  value = r['bpi']['USD']['rate']
  return value

def info_about_good_bot():
  info_of_gb = """This is created by ZeaCeR#5641

Source Code: https://replit.com/@HirushaAdikari/Good-Bot#main.py
Github: https://github.com/hirusha-adi/firrst-discord-bot

This is my first discord bot
This bot is not supposed to be offensive to anyone!
'$help' command will show you the help menu
I JUST WANT EVERYONE TO HAVE FUN! ENJOY!
Stealing the code is very much not appreciated
"""
  return info_of_gb

def get_covid_info():
  r = requests.get('https://coronavirus-19-api.herokuapp.com/all') 
  data = r.json()
  covid_data = f'[+] Confirmed Cases : {data["cases"]} \n[+] Deaths : {data["deaths"]} \n[+] Recovered : {data["recovered"]}'
  return covid_data

def search_wikipedia(wordToSearch):
  result = wikipedia.summary(wordToSearch, sentences = 2)
  return result

def bored_activity():
  r = requests.get('http://www.boredapi.com/api/activity/')
  data = r.json()
  what_to_do_when_bored = f'[+] Activity: {data["activity"]} \n[+] Type: {data["type"]} \n[+] Participants: {data["participants"]} \n[+] Key: {data["key"]} \n[+] Accessibility: {data["accessibility"]} '
  return what_to_do_when_bored

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Please pass in all requirements :rolling_eyes:.')
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You dont have all the requirements :angry:")




@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_guild_join(guild):
    for channel in guild.text_channels:
        if channel.permissions_for(guild.me).send_messages:
            await channel.send('Hey there! Looking forward to make your lives fun:) ')
        break

# Join command, joins the voice channel of whoever sent the command
@client.event
async def join(context):
  channel = context.author.voice.channel
  await channel.connect()

# Leave command, leaves the voice channel
@client.event
async def leave(context):
    await context.voice_client.disconnect()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content

    db["responding"] = True
    
    if msg.startswith('$hello'):
        await message.channel.send('HELLO THERE! ' + str(message.author.mention))
    
    if msg.startswith('$hey'):
        await message.channel.send('SAYONARA! ' + str(message.author.mention))

    if msg.startswith('$hi'):
        await message.channel.send('Hi ' + str(message.author.mention))
    
    if msg.startswith('$cheese'):
        await message.channel.send('BUTTER ' + str(message.author.mention))

    if msg.startswith("$sup"):
      await message.channel.send("Wassup " + str(message.author.mention))
    
    if msg.startswith("$fuck"):
      await message.channel.send("FUCK YOU! " + str(message.author.mention))
    
    if msg.startswith("$fuck you"):
      await message.channel.send("FUCK YOU NIGER! " + str(message.author.mention))
    
    if msg.startswith("$downbad"):
      await message.channel.send("yes, you are! lol " + str(message.author.mention))
    
    if msg.startswith("$wassup"):
      await message.channel.send("Wassup " + str(message.author.mention))
    
    if msg.startswith("$ssup"):
      await message.channel.send("Wassup " + str(message.author.mention))
    
    if msg.startswith("$how is life"):
      await message.channel.send("IM DOIN FINE! " + str(message.author.mention))
    
    if msg.startswith('$help'):
        await message.channel.send("```" + show_help() + "```")
    
    if msg.startswith('$btc'):
      await message.channel.send("```1 BTC = " + str(get_bitcoin_status()) + " USD```")
    
    if msg.startswith('$color'):
      await message.channel.send(give_rand_color())
    
    if msg.startswith('$info'):
      await message.channel.send(info_about_good_bot())
    
    if msg.startswith('$whoami'):
      await message.channel.send(info_about_good_bot())
    
    if msg.startswith('$whoareyou'):
      await message.channel.send(info_about_good_bot())
    
    if msg.startswith('$whoareu'):
      await message.channel.send(info_about_good_bot())
    
    if msg.startswith('$whoru'):
      await message.channel.send(info_about_good_bot())
    
    if msg.startswith('$dog'):
      r = requests.get("https://dog.ceo/api/breeds/image/random").json()
      em = discord.Embed(title="a Dog", color=16202876)
      em.set_image(url=str(r['message']))
      try:
        await message.channel.send(embed=em)
      except:
        await message.channel.send(str(r['message']))
    
    if msg.startswith('$fox'):
      r = requests.get('https://randomfox.ca/floof/').json()
      em = discord.Embed(title="a Fox", color=16202876)
      em.set_image(url=r["image"])
      try:
        await message.channel.send(embed=em)
      except:
        await message.channel.send(r['image'])
    
    # i have no idea on how to do this :(
    # if msg.startswith('$pfp'):
    #   await message.channel.send(discord.Member.avatar_url)

    if msg.startswith('$covid'):
      await message.channel.send("```" + get_covid_info() + "```")
    
    if msg.startswith('$wiki'):
      try:
        whattosearchFOR = msg.split('$wiki ', 1)[1]
        result = wikipedia.summary(whattosearchFOR, sentences = 2)
        # the line below uses the above function and the line below the line below doesnt use it
        # await message.channel.send("```" + str(search_wikipedia(wordToSearch=whattosearchFOR)) + "```")
        await message.channel.send("```" + str(result) + "```")
      except Exception as e:
        await message.channel.send("```Error has occured: " + str(e) + "```")
    
    if msg.startswith('$bored'):
      await message.channel.send("```" + bored_activity() + "```")

    if msg.startswith('$inv'):
        await message.channel.send("```Hey there! Make sure you have me in your server too! Bot Invite link:```" + send_inv_link_to_server())
    
    if msg.startswith('$spam'):
      number_of_times = msg.split('$spam ', 1)[1]
      await message.channel.send("```Spaming " + str(number_of_times) + " times!```")
      for iteration, x in enumerate(range(int(number_of_times))):
        await message.channel.send("NEI NIGAH NEI NEI, NIGAH NIGAH NEI NEI")
        time.sleep(0.5)
    
    if msg.startswith('$spamall'):
      number_of_times = msg.split('$spam ', 1)[1]
      if int(number_of_times) >= 25:
        await message.channel.send("```Spaming " + str(number_of_times) + " times!```")
        for iteration, x in enumerate(range(int(number_of_times))):
          await message.channel.send("@everyone NEI NIGAH NEI NEI, NIGAH NIGAH NEI NEI")
          time.sleep(0.5)
      else:
        await message.channel.send("```JUST STOP IT MATE!```")
    
    if msg.startswith('$spam_zeacer_5641_ngarca'):
      number_of_times = msg.split('$spam ', 1)[1]
      await message.channel.send("```Spaming " + str(number_of_times) + " times!```")
      for iteration, x in enumerate(range(int(number_of_times))):
        await message.channel.send("@everyone @here lol")
        time.sleep(0.5)
    
    if msg.startswith('$nitro'):
      number_of_times = msg.split('$nitro ', 1)[1]
      if int(number_of_times) <= 10:
        await message.channel.send("```Sending " + str(number_of_times) + " Random Nitro Codes!```")
        for iteration, x in enumerate(range(int(number_of_times))):
          await message.channel.send(give_nice_codes())
          time.sleep(0.5)
      else:
        await message.channel.send("```Please enter a value less than 10```")

    
    if msg.startswith('$pervert'):
        await message.channel.send("```" + show_pervert_text() + "```")

    
    if msg.startswith('$inspire'):
        quote = get_quote()
        await message.channel.send("```" + quote + "```")
    
    if msg.startswith('$fake'):
      fake_mode = msg.split("$fake ", 1)[1]
      await message.channel.send("```" + FAKE_PROFILE(fake_mode) + "```")
    
    if msg.startswith('$mfp'):
      fake_mode = msg.split("$mfp ", 1)[1]
      for i in range(int(fake_mode)):
        await message.channel.send("```" + CREATE_FAKE_PROFILES_MANY() + "```")
    
    if db["responding"]:
        options = starter_encouragement
        if "encouragements" in db.keys():
            options.extend(db["encouragements"])
            # options = options + db["encouragements"]
        
        if any(word in msg for word in sad_words):
            await message.channel.send(random.choice(options))
    
    if msg.startswith('$new'):
        encouraging_message = msg.split("$new ", 1)[1]
        update_encouragements(encouraging_message)
        await message.channel.send("```New message added```")
    
    if msg.startswith("$del"):
        encouragements = []
        if "encouragements" in db.keys():
            index = int(msg.split("$del", 1)[1]) # to enter the index as its an integer
            delete_encouragement(index)
            db["encouragements"] = encouragements
        await message.channel.send(encouragements)

    # add a function to find info about ip addresses
    if msg.startswith("$ip"):
      ipaddr = msg.split("$ip ", 1)[1]
      # ipinfo = ipinfoshit(ipaddr)
      await message.channel.send("```" + str(ipinfoshit(ipaddr)) + "```")

    if msg.startswith("$list"):
        encouragements = []
        if "encouragements" in db.keys():
            encouragements = db["encouragements"]
        await message.channel.send(encouragements)
    
    if msg.startswith("$responding"):
        value = msg.split("$responding", 1)[1]

        if value.lower() == "true":
            db["responding"] = True
            await message.channel.send("```Responding is on.```")
        
        else:
            db["responding"] = False
            await message.channel.send("```Responding is off.```")
    
    

keep_alive()

client.run(os.getenv('TOKEN')) # if you are running this on a private server, we can just paste the string here!




