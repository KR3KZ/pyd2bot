from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AllianceModificationNameAndTagValidMessage(INetworkMessage):
    protocolId = 8950
    allianceName:str
    allianceTag:str
    
    
