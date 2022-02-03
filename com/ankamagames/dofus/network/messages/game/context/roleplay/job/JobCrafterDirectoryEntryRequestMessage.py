from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class JobCrafterDirectoryEntryRequestMessage(NetworkMessage):
    playerId:int
    

    def init(self, playerId:int):
        self.playerId = playerId
        
        super().__init__()
    
    