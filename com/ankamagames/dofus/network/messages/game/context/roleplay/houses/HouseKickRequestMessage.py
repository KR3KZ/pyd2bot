from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class HouseKickRequestMessage(INetworkMessage):
    protocolId = 8499
    id:int
    
    
