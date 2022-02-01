from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class MountEquipedErrorMessage(INetworkMessage):
    protocolId = 1774
    errorType:int
    
    
