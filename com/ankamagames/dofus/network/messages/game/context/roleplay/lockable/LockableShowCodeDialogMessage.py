from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class LockableShowCodeDialogMessage(INetworkMessage):
    protocolId = 3045
    changeOrUse:bool
    codeSize:int
    
    
