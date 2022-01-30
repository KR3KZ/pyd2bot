from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MountSterilizedMessage(NetworkMessage):
    protocolId = 3777
    mountId:int
    
