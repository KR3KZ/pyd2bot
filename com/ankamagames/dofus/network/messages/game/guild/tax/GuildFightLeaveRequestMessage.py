from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildFightLeaveRequestMessage(NetworkMessage):
    taxCollectorId:int
    characterId:int
    

    def init(self, taxCollectorId:int, characterId:int):
        self.taxCollectorId = taxCollectorId
        self.characterId = characterId
        
        super().__init__()
    
    