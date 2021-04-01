import time

from Utils.Writer import Writer


class LoginOkMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20104
        self.version = 1

    def encode(self):
        self.writeInt(0)
        self.writeInt(1)
        # HighID, lowID
        self.writeInt(0)
        self.writeInt(1)
        # HighID, lowID
        self.writeString(self.player.Token)  # Token
        self.writeString()
        self.writeString()
        self.writeInt(34)  # MajorVersion
        self.writeInt(151)  # Build
        self.writeInt(1)  # MinorVersion
        self.writeString("integration")  # Environment
        self.writeInt(1) 
        self.writeInt(1)  
        self.writeInt(62) 
        self.writeString()  
        self.writeString() 
        self.writeString()  
        self.writeInt(0)
        self.writeString() 
        self.writeString("CA")
        self.writeString()
        self.writeInt(1)
        self.writeString()  
        self.writeString() 
        self.writeString() 
        self.writeVInt(0)
        self.writeString()
        self.writeVInt(1)
        print("[*] Message LoginOk has been sent.")