from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MountRenameRequestMessage(INetworkMessage):
    protocolId = 8042
    name:str
    mountId:int
    
    
