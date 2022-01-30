from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PauseDialogMessage(INetworkMessage):
    protocolId = 8906
    dialogType:int
    
    
