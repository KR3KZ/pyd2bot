from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildApplicationReceivedMessage(NetworkMessage):
    playerName:str
    playerId:int
    

    def init(self, playerName:str, playerId:int):
        self.playerName = playerName
        self.playerId = playerId
        
        super().__init__()
    
    