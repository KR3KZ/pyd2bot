from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class CharacterCapabilitiesMessage(NetworkMessage):
    guildEmblemSymbolCategories:int
    

    def init(self, guildEmblemSymbolCategories:int):
        self.guildEmblemSymbolCategories = guildEmblemSymbolCategories
        
        super().__init__()
    
    