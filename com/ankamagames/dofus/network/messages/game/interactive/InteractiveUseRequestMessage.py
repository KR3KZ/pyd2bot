from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class InteractiveUseRequestMessage(INetworkMessage):
    protocolId = 9714
    elemId:int
    skillInstanceUid:int
    
    
