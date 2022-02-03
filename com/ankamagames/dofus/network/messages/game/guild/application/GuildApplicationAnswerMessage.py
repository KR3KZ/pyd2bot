from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildApplicationAnswerMessage(NetworkMessage):
    accepted:bool
    playerId:int
    

    def init(self, accepted:bool, playerId:int):
        self.accepted = accepted
        self.playerId = playerId
        
        super().__init__()
    
    