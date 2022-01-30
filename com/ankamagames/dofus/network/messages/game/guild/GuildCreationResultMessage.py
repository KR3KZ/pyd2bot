from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GuildCreationResultMessage(NetworkMessage):
    protocolId = 42
    result:int
    
    
