from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ObjectItemInRolePlay(INetworkMessage):
    protocolId = 4848
    cellId:int
    objectGID:int
    
    
