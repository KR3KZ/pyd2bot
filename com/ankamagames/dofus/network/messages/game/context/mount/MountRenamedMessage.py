from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class MountRenamedMessage(NetworkMessage):
    protocolId = 7698
    mountId:int
    name:str
    
