from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AllianceCreationResultMessage(INetworkMessage):
    protocolId = 4954
    result:int
    
    
