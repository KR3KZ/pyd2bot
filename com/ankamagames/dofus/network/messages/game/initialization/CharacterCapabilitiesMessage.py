from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class CharacterCapabilitiesMessage(INetworkMessage):
    protocolId = 344
    guildEmblemSymbolCategories:int
    
    
