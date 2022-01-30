from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AllianceCreationResultMessage(NetworkMessage):
    protocolId = 4954
    result:int
    
