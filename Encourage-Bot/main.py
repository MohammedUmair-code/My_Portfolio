import discord
import os
import requests
import json
import random
from replit import db
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

sad_words = ["sad", "depressed", "unhappy", "angry", "depressing", "miserable"]

starter_encouragements =  ["chear up!", "hang in there.","you are a great person / bot!", "you are not alone", "you are amazing", "you are the best", "you are great", "you are best", "you are the bestestest"]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote(): #helper function to get a quote from the API
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " - " + json_data[0]["a"]
  return quote

def update_encouragements(encouraging_message): #how is this thing working?
  encouraging_message = encouraging_message.lower()
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def delete_encouragements(encourage):  #how is this helper function working? 
  encourage = encourage.strip().lower()
  encouragements = db["encouragements"]
  if encourage in encouragements:
    encouragements.remove(encourage)
    db["encouragements"] = encouragements
    return True
  else:
    return False
     
@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return  #the bot will not register its own messages

  msg = message.content

  if msg.startswith("$inspire"):
    await message.channel.send(get_quote())

  options = starter_encouragements
  db_encouragements = db["encouragements"]
  if db["responding"] == True:
    if "encouragements" in db.keys():
      options = options + list(db_encouragements)
      
  
    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new"): #Review how does this work?
    encouraging_message = msg.split("$new ", 1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added!")

  if msg.startswith("$del"): #review how does this work?
    encouragements = []
    if "encouragements" in db.keys():
      encourage = str(msg.split("$del", 1)[1])
      
      if delete_encouragements(encourage) == False:
        await message.channel.send(f"The encouragement {encourage} is not found in our database.")
      else:
        encouragements = db["encouragements"]
        await message.channel.send(f"The encouragement {encourage} is successfully removed.")
        await message.channel.send(encouragements)
    

  if msg.startswith("$show"):
    encouragements = options + []
    if "encouragements" in db.keys():
      encouragements = options + list(db_encouragements)
    await message.channel.send(encouragements)

  if msg.startswith("$encourage_respond"): #how does it save whether to respond or not even when the code is stopped and executed again?
    value = msg.split("$encourage_respond ", 1)[1]
    if value.upper() == "OFF":
      db["responding"] = False
      await message.channel.send("Responding Encouragements: Turned OFF")
    elif value.upper() == "ON":
      db["responding"] = True
      await message.channel.send("Responding Encouragements: Turned ON")
    else:
      await message.channel.send("Invalid Command!")
    
         
keep_alive()
client.run(os.getenv('TOKEN')) #there is a workaround?


    



