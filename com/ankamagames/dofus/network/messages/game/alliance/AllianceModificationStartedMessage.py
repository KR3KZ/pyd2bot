from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class AllianceModificationStartedMessage(INetworkMessage):
    protocolId = 6240
    canChangeName:bool
    canChangeTag:bool
    canChangeEmblem:bool
    
    
