from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class LeaveDialogMessage(INetworkMessage):
    protocolId = 2209
    dialogType:int
    
    
