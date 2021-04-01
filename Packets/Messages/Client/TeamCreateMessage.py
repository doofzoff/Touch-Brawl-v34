from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.TeamMessage import TeamMessage
from database.DataBase import DataBase

from Utils.Reader import BSMessageReader


class TeamCreateMessage(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.mapID = 7

    def decode(self):
        self.read_Vint()
        self.mapID = self.read_Vint()

    def process(self):
        if self.mapID == 1:
            self.player.mapID = 7
        elif self.mapID == 2:
            self.player.mapID = 32
        elif self.mapID == 3:
            self.player.mapID = 17
        elif self.mapID == 4:
            self.player.mapID = 57
        elif self.mapID == 5:
            self.player.mapID = 38
        elif self.mapID == 6:
            self.player.mapID = 24
        elif self.mapID == 7:
            self.player.mapID = 202
        elif self.mapID == 8:
            self.player.mapID = 97
        elif self.mapID == 9:
            self.player.mapID = 167
        DataBase.replaceValue(self, 'mapID', self.player.mapID)
        TeamMessage(self.client, self.player).send()
