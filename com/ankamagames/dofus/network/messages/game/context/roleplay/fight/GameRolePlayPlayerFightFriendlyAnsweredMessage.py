from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightFriendlyAnsweredMessage(NetworkMessage):
    protocolId = 5417
    fightId:int
    sourceId:float
    targetId:float
    accept:bool
    
