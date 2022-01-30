from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayAggressionMessage(INetworkMessage):
    protocolId = 2660
    attackerId:int
    defenderId:int
    
    
