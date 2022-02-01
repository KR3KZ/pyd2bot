from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismFightJoinLeaveRequestMessage(NetworkMessage):
    subAreaId:int
    join:bool
    
    
