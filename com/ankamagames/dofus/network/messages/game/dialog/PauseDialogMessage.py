from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PauseDialogMessage(NetworkMessage):
    protocolId = 8906
    dialogType:int
    
