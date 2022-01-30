from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SetEnablePVPRequestMessage(NetworkMessage):
    protocolId = 4228
    enable:bool
    
    
