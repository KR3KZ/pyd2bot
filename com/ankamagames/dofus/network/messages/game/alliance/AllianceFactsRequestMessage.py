from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AllianceFactsRequestMessage(INetworkMessage):
    protocolId = 8146
    allianceId:int
    
    
