from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SlaveNoLongerControledMessage(INetworkMessage):
    protocolId = 4540
    masterId:int
    slaveId:int
    
    
