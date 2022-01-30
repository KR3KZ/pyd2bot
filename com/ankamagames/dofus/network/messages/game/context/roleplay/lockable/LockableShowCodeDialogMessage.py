from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class LockableShowCodeDialogMessage(NetworkMessage):
    protocolId = 3045
    changeOrUse:bool
    codeSize:int
    
    
