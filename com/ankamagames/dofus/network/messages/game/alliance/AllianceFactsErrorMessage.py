from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AllianceFactsErrorMessage(INetworkMessage):
    protocolId = 8954
    allianceId:int
    
    
