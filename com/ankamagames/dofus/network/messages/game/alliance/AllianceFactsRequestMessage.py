from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AllianceFactsRequestMessage(NetworkMessage):
    protocolId = 8146
    allianceId:int
    
    
