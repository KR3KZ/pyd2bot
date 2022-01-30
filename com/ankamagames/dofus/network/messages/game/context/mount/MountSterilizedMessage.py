from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class MountSterilizedMessage(INetworkMessage):
    protocolId = 3777
    mountId:int
    
    
