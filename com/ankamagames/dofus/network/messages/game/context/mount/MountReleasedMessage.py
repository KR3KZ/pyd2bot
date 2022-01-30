from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MountReleasedMessage(INetworkMessage):
    protocolId = 843
    mountId:int
    
    
