from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MountRenameRequestMessage(NetworkMessage):
    protocolId = 8042
    name:str
    mountId:int
    
