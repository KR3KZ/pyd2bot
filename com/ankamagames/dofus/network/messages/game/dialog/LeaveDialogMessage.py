from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class LeaveDialogMessage(INetworkMessage):
    protocolId = 2209
    dialogType:int
    
    
