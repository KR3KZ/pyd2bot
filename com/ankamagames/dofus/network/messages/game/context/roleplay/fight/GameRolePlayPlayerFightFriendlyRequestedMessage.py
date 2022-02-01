from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayPlayerFightFriendlyRequestedMessage(INetworkMessage):
    protocolId = 2157
    fightId:int
    sourceId:int
    targetId:int
    
    
