from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class EmotePlayRequestMessage(NetworkMessage):
    protocolId = 5775
    emoteId:int
    
    
