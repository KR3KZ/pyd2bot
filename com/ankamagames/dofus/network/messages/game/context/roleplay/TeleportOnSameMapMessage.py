from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TeleportOnSameMapMessage(INetworkMessage):
    protocolId = 9521
    targetId:int
    cellId:int
    
    
