from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PrismInfoJoinLeaveRequestMessage(INetworkMessage):
    protocolId = 6247
    join:bool
    
    
