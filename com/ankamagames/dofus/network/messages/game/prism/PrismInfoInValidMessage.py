from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PrismInfoInValidMessage(NetworkMessage):
    protocolId = 7307
    reason:int
    
    
