from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class MoodSmileyUpdateMessage(NetworkMessage):
    accountId:int
    playerId:int
    smileyId:int
    

    def init(self, accountId:int, playerId:int, smileyId:int):
        self.accountId = accountId
        self.playerId = playerId
        self.smileyId = smileyId
        
        super().__init__()
    
    