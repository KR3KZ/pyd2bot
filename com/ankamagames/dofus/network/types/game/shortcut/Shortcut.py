from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class Shortcut(NetworkMessage):
    protocolId = 5511
    slot:int
    
