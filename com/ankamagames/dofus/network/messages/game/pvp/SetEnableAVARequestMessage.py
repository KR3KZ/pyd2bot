from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SetEnableAVARequestMessage(INetworkMessage):
    protocolId = 3626
    enable:bool
    
    
