from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayArenaFightAnswerMessage(INetworkMessage):
    protocolId = 5799
    fightId:int
    accept:bool
    
    
