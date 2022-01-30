from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameContextKickMessage(NetworkMessage):
    protocolId = 2712
    targetId:int
    
