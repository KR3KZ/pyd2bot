from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildFightJoinRequestMessage(NetworkMessage):
    taxCollectorId:int
    

    def init(self, taxCollectorId:int):
        self.taxCollectorId = taxCollectorId
        
        super().__init__()
    
    