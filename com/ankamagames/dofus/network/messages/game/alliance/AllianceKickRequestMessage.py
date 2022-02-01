from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AllianceKickRequestMessage(INetworkMessage):
    protocolId = 1648
    kickedId:int
    
    
