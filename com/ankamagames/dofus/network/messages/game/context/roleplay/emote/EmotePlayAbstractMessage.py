from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class EmotePlayAbstractMessage(NetworkMessage):
    protocolId = 4497
    emoteId:int
    emoteStartTime:int
    
