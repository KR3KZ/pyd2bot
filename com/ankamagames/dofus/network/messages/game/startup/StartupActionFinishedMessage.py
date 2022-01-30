from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class StartupActionFinishedMessage(INetworkMessage):
    protocolId = 6394
    actionId:int
    success:bool
    automaticAction:bool
    
    
