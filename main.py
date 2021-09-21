import discord
from cleverbotfree import Cleverbot
from cleverbotfree import CleverbotAsync

client = discord.Client()
cb = Cleverbot


#fires off whenver alyona turns on
@client.event
async def on_ready():
    print("Alyona is now turned on. Not in that way!")


#fires off whenever someone sends a message in the Alyona-channel
@client.event
async def on_message(message):
    #so that Alyona does not get stuck in a chat loop .-.
    if (message.author.id == 430118371598663680):
        return
    if (message.content.find("Alyona, shutdown") != -1):
        if (message.author.id == 254086442228252683):
            await message.channel.send("Goodbye!!!")
            await client.close()
            print("Shutting down...")
        else:
            await message.channel.send("You're not the boss of me")
    else:
        if message.channel.name == "alyona-channel":
            user_input = message.content
            reply = await async_chat(user_input)
            await message.channel.send(reply)


# Returns a response from Cleverbot with the given user input
# Must be asynchronous
@CleverbotAsync.connect
async def async_chat(bot, user_input):
    reply = await bot.single_exchange(user_input)
    await bot.close()
    return reply


client.run("NDMwMTE4MzcxNTk4NjYzNjgw.WsFQ8w.1jN3UkUKvSdGHG7Z7tY-cLcLW78")
