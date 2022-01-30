from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PrismInfoJoinLeaveRequestMessage(INetworkMessage):
    protocolId = 6247
    join:bool
    
    
