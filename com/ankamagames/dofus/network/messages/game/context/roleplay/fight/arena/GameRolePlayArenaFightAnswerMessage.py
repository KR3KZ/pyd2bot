from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayArenaFightAnswerMessage(NetworkMessage):
    protocolId = 5799
    fightId:int
    accept:bool
    
    
