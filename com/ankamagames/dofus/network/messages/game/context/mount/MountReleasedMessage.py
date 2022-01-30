from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MountReleasedMessage(NetworkMessage):
    protocolId = 843
    mountId:int
    
