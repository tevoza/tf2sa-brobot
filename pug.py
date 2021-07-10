from queue import Queue
from enum import Enum

class PugStatus(Enum):
    IDLE            = 1     #no pug currently being played
    CONFIRMATION    = 2     #confirm status before starting pug
    ACTIVE          = 3     #pug in progress

class PugPlayer:
    def __init__(self, name, readytime,votedmap=None):
        self.Name       = name
        self.ReadyTime  = readytime
        self.VotedMap   = votedmap

class Pug:
    def __init__(self, maps, server, recent_cooldown, player_amount):
        self.Server         = server
        self.Status         = PugStatus.IDLE
        self.PlayerAmount   = player_amount
        self.PlayersQueue   = Queue(maxsize = player_amount)    #
        self.PlayersInPug   = []
        self.Maps           = maps
        self.RecentlyPlayed = Queue(maxsize = recent_cooldown)
        return

    def __str__(self):
        info = (
            f"Pug at {self.Server} in {self.Status} state\n"
            f"PLAYERS: {self.PlayerAmount}\n"
            f"QUEUE: {self.PlayersQueue}\n"
            f"IN PUG: {self.PlayersInPug}\n"
            f"MAPS:{self.Maps}\n"
            f"RECENTLY PLAYED:{self.RecentlyPlayed}\n"
        )
        return info
