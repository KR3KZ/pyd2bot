from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class LeaveDialogMessage(NetworkMessage):
    protocolId = 2209
    dialogType:int
    
