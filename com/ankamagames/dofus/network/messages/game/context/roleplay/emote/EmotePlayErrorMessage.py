from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class EmotePlayErrorMessage(NetworkMessage):
    protocolId = 9167
    emoteId:int
    
    
