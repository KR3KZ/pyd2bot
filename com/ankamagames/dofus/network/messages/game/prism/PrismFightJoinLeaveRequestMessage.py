from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PrismFightJoinLeaveRequestMessage(NetworkMessage):
    protocolId = 7653
    subAreaId:int
    join:bool
    
    
