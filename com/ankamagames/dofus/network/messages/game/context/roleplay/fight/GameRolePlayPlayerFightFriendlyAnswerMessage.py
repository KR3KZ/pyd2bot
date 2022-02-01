from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameRolePlayPlayerFightFriendlyAnswerMessage(INetworkMessage):
    protocolId = 9468
    fightId:int
    accept:bool
    
    
