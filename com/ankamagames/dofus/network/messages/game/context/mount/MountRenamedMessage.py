from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MountRenamedMessage(INetworkMessage):
    protocolId = 7698
    mountId:int
    name:str
    
    
