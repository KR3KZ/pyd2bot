from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class StartupActionFinishedMessage(NetworkMessage):
    protocolId = 6394
    actionId:int
    
