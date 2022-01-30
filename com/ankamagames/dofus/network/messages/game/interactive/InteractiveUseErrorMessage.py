from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class InteractiveUseErrorMessage(INetworkMessage):
    protocolId = 778
    elemId:int
    skillInstanceUid:int
    
    
