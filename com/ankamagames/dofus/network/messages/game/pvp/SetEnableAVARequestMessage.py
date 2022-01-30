from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class SetEnableAVARequestMessage(NetworkMessage):
    protocolId = 3626
    enable:bool
    
