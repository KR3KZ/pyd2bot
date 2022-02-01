from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class CharacterCapabilitiesMessage(INetworkMessage):
    protocolId = 344
    guildEmblemSymbolCategories:int
    
    
