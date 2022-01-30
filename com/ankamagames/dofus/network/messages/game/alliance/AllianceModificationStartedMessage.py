from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class AllianceModificationStartedMessage(NetworkMessage):
    protocolId = 6240
    canChangeName:bool
    canChangeTag:bool
    canChangeEmblem:bool
    
    
