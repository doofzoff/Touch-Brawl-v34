from Utils.Writer import Writer
from database.DataBase import DataBase


class OwnHomeData(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        # sub_6BB088 start
        self.writeVInt(2021091) #Year * 1000 + day_of_year
        self.writeVInt(72152)
        self.writeVInt(99999)
        self.writeVInt(99999)
        self.writeVInt(122)
        self.writeVInt(200)
        self.writeVInt(99999)
        
        self.writeScID(28, 0) # Player icon
        self.writeScID(43, 0) # Player name color
        
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        self.writeVInt(0) # Array
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeByte(0) # boolean
        self.writeVInt(1000)
        self.writeVInt(10)
        self.writeVInt(20)
        self.writeVInt(30)
        
        # sub_5705E4 start
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        # sub_5705E4 end
        
        self.writeByte(0) # 3 bools
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(0) # v17 - Shop Array ?
        
        self.writeVInt(0) # v21 - Array
        
        self.writeVInt(200)
        self.writeVInt(0)
        
        self.writeVInt(0) # Array
        
        self.writeVInt(99999)
        self.writeVInt(0)
        
        self.writeScID(16, 45) # Menu Brawler
        
        self.writeString("CA")
        self.writeString("http://ultracore.cf/")
        
        self.writeVInt(1) # v26 - Array
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeVInt(1) # v29 - Array
        self.writeVInt(0)
        self.writeScID(16, 0)
        self.writeVInt(0)
        
        self.writeVInt(1) # SeasonArray (v32)
        self.writeVInt(4)
        self.writeVInt(0)
        self.writeByte(0)
        self.writeVInt(1)
        self.writeByte(2)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeByte(1)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeVInt(1) # v35 - Array
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeByte(1) # boolean need set to true!!!
        self.writeVInt(0) # Quests Array
        
        self.writeByte(1) # boolean need set to true!!!
        self.writeVInt(0) # Pins Array
        
        self.writeByte(1) # Array ?????
        self.writeVInt(0) 
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeByte(2)
        self.writeVInt(0)
        self.writeByte(0)
        self.writeVInt(0)
        self.writeByte(0)
        #sub_6BB088 end
        
        # sub_1B9CB8 start
        self.writeVInt(1) #v4
        
        self.writeVInt(1) #Array vint
        self.writeVInt(0)
        
        self.writeVInt(1) # Events
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(75992)
        self.writeVInt(10)
        
        self.writeScID(15, 7)
        
        self.writeVInt(3)
        self.writeVInt(0)
        self.writeString()
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0) #modifier array
        
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeByte(1) #ebanuty array
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeString()
        self.writeVInt(0)
        
        self.writeVInt(0) #??? DataReference
        
        self.writeInt(0) #bytesLength
        
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0) #result array
        
        self.writeVInt(0)
        
        self.writeByte(1)
        self.writeVInt(0)
        self.writeString()
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        #Event end
        
        self.writeVInt(0) # empty events array
        
        self.writeVInt(0) #sub_457814
        self.writeVInt(0) #sub_457814
        self.writeVInt(0) #sub_457814
        self.writeVInt(0) #sub_457814
        
        self.writeByte(0) #boolean
        
        self.writeVInt(0) # Array v18
        
        self.writeVInt(0) # Array v21
        
        self.writeVInt(0) # Array v24
        
        self.writeVInt(0) # Array result
        # sub_1B9CB8 end
        
        self.writeInt(0) #LongLong
        self.writeInt(1)
        
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeByte(0) # boolean
        self.writeVInt(0)
        
        self.writeVInt(0) # Array result
        
        #LogicClientAvatar start
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(1)
        
        self.writeString("Ultracore V34")
        self.writeByte(1) #nameset
        self.writeInt(0)
        
        self.writeVInt(8) # commodity count
        
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        #commoditys end
        
        self.writeVInt(999999)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(2) #result
        
        self.writeVInt(0) #timestamp end
        
        print("[*] Message OwnHomeData has been sent.")
