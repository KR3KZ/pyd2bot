from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PauseDialogMessage(INetworkMessage):
    protocolId = 8906
    dialogType:int
    
    
