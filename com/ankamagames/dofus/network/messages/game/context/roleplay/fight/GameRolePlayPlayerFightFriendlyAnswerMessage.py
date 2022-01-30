from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightFriendlyAnswerMessage(NetworkMessage):
    protocolId = 9468
    fightId:int
    accept:bool
    
    
