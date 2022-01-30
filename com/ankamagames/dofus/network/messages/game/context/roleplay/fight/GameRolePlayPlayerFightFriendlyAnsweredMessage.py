from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayPlayerFightFriendlyAnsweredMessage(INetworkMessage):
    protocolId = 5417
    fightId:int
    sourceId:int
    targetId:int
    accept:bool
    
    
