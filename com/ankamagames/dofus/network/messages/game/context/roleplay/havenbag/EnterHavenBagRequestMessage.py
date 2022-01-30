from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class EnterHavenBagRequestMessage(NetworkMessage):
    protocolId = 8214
    havenBagOwner:int
    
    
