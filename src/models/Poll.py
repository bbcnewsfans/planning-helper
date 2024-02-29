import peewee
import random
import string
from typing import Optional

class PollStatus:
    open = 0
    timed = 1
    closed = 2

class PollType:
    normal = 0
    timed = 1

class Poll(peewee.Model):
    poll_id: str = peewee.CharField(max_length=10, unique=True)
    channel_and_message_id: str = peewee.CharField(max_length=999999) # {channel id}_{message id}
    creator_id: int = peewee.IntegerField()
    votes: str = peewee.CharField(max_length=999999) # dict
    status: PollStatus = peewee.IntegerField()
    closesAt: int = peewee.IntegerField() # only required if timed

    @staticmethod
    def votesToString(fromDict: dict):
        return str(fromDict)

    @staticmethod
    def stringToVotes(fromStr: str):
        return dict(fromStr)
    
    @staticmethod
    # if type is timed and no end time is specified a TypeError will be raised.
    def newPoll(messageId: int, creatorId: int, options: list, type: PollType, endsAt: Optional[int]):
        if type == PollType.normal or type == PollType.timed and endsAt is not None:
            optionsDict = {}
            for option in options:
                optionsDict[option] = []

            pollId = ''.join(random.choices(string.ascii_letters + string.digits), k=10)
        else:
            raise TypeError
