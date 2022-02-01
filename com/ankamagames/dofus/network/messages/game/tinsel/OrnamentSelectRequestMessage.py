from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class OrnamentSelectRequestMessage(INetworkMessage):
    protocolId = 4149
    ornamentId:int
    
    
