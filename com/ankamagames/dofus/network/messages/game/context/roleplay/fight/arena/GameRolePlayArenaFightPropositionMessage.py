from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayArenaFightPropositionMessage(INetworkMessage):
    protocolId = 2533
    fightId:int
    alliesId:int
    duration:int
    
    
