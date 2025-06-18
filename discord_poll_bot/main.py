import discord 
import os
import random
import re

from dataclasses import dataclass
from dotenv import load_dotenv
from typing import List, Dict, Optional


REGEX = re.compile(r'"(.*?)"')

class PollException(Exception):
    pass


@dataclass
class Poll:
    question: str
    choices: List[str]

    @classmethod
    def from_str(cls, poll_str: str) -> "Poll":
        quotes_count = poll_str.count('"')
        if quotes_count == 0 or quotes_count % 2 != 0:
            raise PollException("Polll must have an even number of double quotes")
        
        fields = re.findall(REGEX, poll_str)
        return cls(fields[0], fields[1:] if len(fields)> 0 else [])

    def get_message(self):
        return f"📊 {self.question}"
    
    def get_embed(self) -> Optional[discord.Embed]:

        if not self.choices:
            return None
        description = "\n".join(f"{self.get_regional_indicator_symbol(idx)} {choice}" for idx, choice in enumerate(self.choices))
        return discord.Embed(description= description, color= discord.Color.dark_red())
    
    def reactions(self) -> List[str]:
        if self.choices:
            return [self.get_regional_indicator_symbol(i) for i in range(len(self.choices))]
        else: 
            return ["👍", "👎"]
        
    @staticmethod
    def get_regional_indicator_symbol(idx: int) -> str:
        return chr(ord("\U0001F1E6") + idx) if 0 <= idx < 26 else ""
    
class PollBot(discord.Client):

    def __init__(self, **options):
        intents = discord.Intents().all()
        intents.messages = True
        intents.message_content = True
        intents.members =True
        super().__init__(intents = intents,**options)
        self.polls: Dict[int, Poll] = {}
    
    @staticmethod
    def help() -> discord.Embed:
        description = """/poll "Question"
        Or
        /poll "Question" "Choice A" "Choice B" "Choice C"
        """
        embed = discord.Embed(title= "Usage:", description=description, color = discord.Color.dark_red())
        embed.set_footer(text = "HEPIA powered")
        return embed
    
    async def on_ready(self) -> None:
        print(f"{self.user} has connected to Discord!")
        activity = discord.Game("/poll")
        await self.change_presence(activity=activity)

    # async def send_reactions(self, message: discord.message) -> None:
    #     print(f"Trying to add reactions to message with ID: {message.id}")
    #     if poll:= self.polls.get(message.id):
    #         print("Poll found.Adding Reactions...")
    #         for reaction in poll.reactions():
    #             print(f"Adding: {reaction}")
    #             await message.add_reaction(reaction)
    #         self.polls.pop(message.id)
    #     else:
    #         print("No matching poll found for message")

    async def send_poll(self, message: discord.message) -> None:
        poll = Poll.from_str(message.content)
        await message.delete()
        sent = await message.channel.send(poll.get_message(), embed = poll.get_embed())

        self.polls[sent.id] = poll
        print(f"Poll stored with message ID: {sent.id}")

        for reaction in poll.reactions():
            print(f"Adding: {reaction}")
            await sent.add_reaction(reaction)

        self.polls.pop(sent.id)


    async def on_message(self, message:discord.message) -> None:
        if message.author == self.user:
            return 
        if message.content.startswith("/poll"):
            try:
                await self.send_poll(message)
            except PollException:
                await message.channel.send(embed=self.help())

if __name__ == "__main__":
    load_dotenv()
    TOKEN = os.getenv("DISCORD_TOKEN")
    client = PollBot()
    client.run(TOKEN)


    
    


