from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayAggressionMessage(NetworkMessage):
    protocolId = 2660
    attackerId:int
    defenderId:int
    
    
