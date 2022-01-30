from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class CharacterCapabilitiesMessage(NetworkMessage):
    protocolId = 344
    guildEmblemSymbolCategories:int
    
