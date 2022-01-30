from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MountInformationRequestMessage(NetworkMessage):
    protocolId = 2112
    id:int
    time:int
    
