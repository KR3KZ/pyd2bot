from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class LockableShowCodeDialogMessage(NetworkMessage):
    changeOrUse:bool
    codeSize:int
    
    
