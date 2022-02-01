from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayArenaFightPropositionMessage(NetworkMessage):
    fightId:int
    alliesId:list[int]
    duration:int
    
    
