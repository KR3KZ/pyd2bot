from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class GameRolePlayArenaFightAnswerMessage(INetworkMessage):
    protocolId = 5799
    fightId:int
    accept:bool
    
    
