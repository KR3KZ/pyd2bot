from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class EmoteAddMessage(NetworkMessage):
    protocolId = 8736
    emoteId:int
    
    
