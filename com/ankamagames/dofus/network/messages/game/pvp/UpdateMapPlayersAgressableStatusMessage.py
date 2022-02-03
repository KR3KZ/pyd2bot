from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class UpdateMapPlayersAgressableStatusMessage(NetworkMessage):
    playerIds:list[int]
    enable:list[int]
    

    def init(self, playerIds:list[int], enable:list[int]):
        self.playerIds = playerIds
        self.enable = enable
        
        super().__init__()
    
    