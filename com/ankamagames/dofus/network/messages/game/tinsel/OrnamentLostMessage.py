from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class OrnamentLostMessage(INetworkMessage):
    protocolId = 94
    ornamentId:int
    
    
