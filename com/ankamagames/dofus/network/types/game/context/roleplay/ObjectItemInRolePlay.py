from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ObjectItemInRolePlay(INetworkMessage):
    protocolId = 4848
    cellId:int
    objectGID:int
    
    
