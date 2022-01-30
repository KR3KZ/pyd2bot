from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AllianceModificationNameAndTagValidMessage(INetworkMessage):
    protocolId = 8950
    allianceName:str
    allianceTag:str
    
    
