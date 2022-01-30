from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AllianceFactsErrorMessage(INetworkMessage):
    protocolId = 8954
    allianceId:int
    
    
