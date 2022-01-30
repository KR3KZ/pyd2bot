from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class OrnamentGainedMessage(INetworkMessage):
    protocolId = 3920
    ornamentId:int
    
    
