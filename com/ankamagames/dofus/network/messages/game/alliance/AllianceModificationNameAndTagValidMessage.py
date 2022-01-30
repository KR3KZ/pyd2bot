from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AllianceModificationNameAndTagValidMessage(NetworkMessage):
    protocolId = 8950
    allianceName:str
    allianceTag:str
    
