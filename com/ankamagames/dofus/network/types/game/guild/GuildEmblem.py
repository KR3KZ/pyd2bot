from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GuildEmblem(NetworkMessage):
    symbolShape:int
    symbolColor:int
    backgroundShape:int
    backgroundColor:int
    

    def init(self, symbolShape:int, symbolColor:int, backgroundShape:int, backgroundColor:int):
        self.symbolShape = symbolShape
        self.symbolColor = symbolColor
        self.backgroundShape = backgroundShape
        self.backgroundColor = backgroundColor
        
        super().__init__()
    
    