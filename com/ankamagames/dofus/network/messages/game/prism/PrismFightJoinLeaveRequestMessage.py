from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PrismFightJoinLeaveRequestMessage(INetworkMessage):
    protocolId = 7653
    subAreaId:int
    join:bool
    
    
