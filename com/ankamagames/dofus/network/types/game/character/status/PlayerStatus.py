from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PlayerStatus(INetworkMessage):
    protocolId = 3077
    statusId:int
    
    
