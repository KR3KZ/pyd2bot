from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildSpellUpgradeRequestMessage(NetworkMessage):
    spellId:int
    

    def init(self, spellId:int):
        self.spellId = spellId
        
        super().__init__()
    
    