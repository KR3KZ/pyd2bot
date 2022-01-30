from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class EnterHavenBagRequestMessage(INetworkMessage):
    protocolId = 8214
    havenBagOwner:int
    
    
