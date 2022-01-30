from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MountEquipedErrorMessage(INetworkMessage):
    protocolId = 1774
    errorType:int
    
    
