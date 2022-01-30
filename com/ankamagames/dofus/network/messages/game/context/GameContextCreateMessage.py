from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameContextCreateMessage(NetworkMessage):
    protocolId = 4950
    context:int
    
