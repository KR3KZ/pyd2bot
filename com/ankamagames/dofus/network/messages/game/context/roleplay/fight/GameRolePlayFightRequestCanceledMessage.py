from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayFightRequestCanceledMessage(INetworkMessage):
    protocolId = 4478
    fightId:int
    sourceId:int
    targetId:int
    
    
