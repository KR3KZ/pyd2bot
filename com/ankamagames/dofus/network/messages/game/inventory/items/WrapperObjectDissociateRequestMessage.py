from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class WrapperObjectDissociateRequestMessage(INetworkMessage):
    protocolId = 9634
    hostUID:int
    hostPos:int
    
    
