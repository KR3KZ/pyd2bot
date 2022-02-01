from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class SlaveNoLongerControledMessage(NetworkMessage):
    masterId:int
    slaveId:int
    
    
