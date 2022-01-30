from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayPlayerFightFriendlyAnswerMessage(INetworkMessage):
    protocolId = 9468
    fightId:int
    accept:bool
    
    
