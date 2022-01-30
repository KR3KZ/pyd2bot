from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class OrnamentSelectedMessage(INetworkMessage):
    protocolId = 7637
    ornamentId:int
    
    
