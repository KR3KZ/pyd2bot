from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class LockableShowCodeDialogMessage(INetworkMessage):
    protocolId = 3045
    changeOrUse:bool
    codeSize:int
    
    
