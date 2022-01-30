from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightFriendlyAnsweredMessage(NetworkMessage):
    protocolId = 5417
    fightId:int
    sourceId:int
    targetId:int
    accept:bool
    
