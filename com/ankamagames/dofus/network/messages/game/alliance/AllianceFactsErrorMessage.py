from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AllianceFactsErrorMessage(NetworkMessage):
    protocolId = 8954
    allianceId:int
    
