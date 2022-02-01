from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class OrnamentGainedMessage(INetworkMessage):
    protocolId = 3920
    ornamentId:int
    
    
