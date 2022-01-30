from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PrismInfoJoinLeaveRequestMessage(NetworkMessage):
    protocolId = 6247
    join:bool
    
