from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildCharacsUpgradeRequestMessage(NetworkMessage):
    charaTypeTarget:int
    

    def init(self, charaTypeTarget:int):
        self.charaTypeTarget = charaTypeTarget
        
        super().__init__()
    
    