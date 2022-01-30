from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class OrnamentSelectRequestMessage(INetworkMessage):
    protocolId = 4149
    ornamentId:int
    
    
