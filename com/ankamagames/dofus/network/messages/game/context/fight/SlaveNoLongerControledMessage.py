from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SlaveNoLongerControledMessage(NetworkMessage):
    protocolId = 4540
    masterId:int
    slaveId:int
    
    
