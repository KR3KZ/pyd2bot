from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AllianceFactsRequestMessage(INetworkMessage):
    protocolId = 8146
    allianceId:int
    
    
