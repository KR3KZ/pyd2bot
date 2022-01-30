from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class SetEnablePVPRequestMessage(INetworkMessage):
    protocolId = 4228
    enable:bool
    
    
