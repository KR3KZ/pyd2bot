from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class SlaveNoLongerControledMessage(INetworkMessage):
    protocolId = 4540
    masterId:int
    slaveId:int
    
    
