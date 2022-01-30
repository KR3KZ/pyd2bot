from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class EmoteRemoveMessage(NetworkMessage):
    protocolId = 8124
    emoteId:int
    
    
