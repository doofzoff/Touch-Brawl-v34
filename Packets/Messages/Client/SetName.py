from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.SetNameCallback import SetNameCallback

from Utils.Reader import BSMessageReader


class SetName(BSMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.name = self.read_string()

    def process(self):
        SetNameCallback(self.client, self.player).send()