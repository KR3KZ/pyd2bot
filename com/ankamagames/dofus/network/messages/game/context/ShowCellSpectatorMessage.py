from com.ankamagames.dofus.network.messages.game.context.ShowCellMessage import ShowCellMessage


class ShowCellSpectatorMessage(ShowCellMessage):
    playerName:str
    

    def init(self, playerName:str, sourceId:int, cellId:int):
        self.playerName = playerName
        
        super().__init__(sourceId, cellId)
    
    