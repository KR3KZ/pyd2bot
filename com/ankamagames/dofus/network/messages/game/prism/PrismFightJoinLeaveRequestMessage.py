from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PrismFightJoinLeaveRequestMessage(INetworkMessage):
    protocolId = 7653
    subAreaId:int
    join:bool
    
    
