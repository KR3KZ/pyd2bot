from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildEmblem(NetworkMessage):
    protocolId = 2994
    symbolShape:int
    symbolColor:int
    backgroundShape:int
    backgroundColor:int
    
