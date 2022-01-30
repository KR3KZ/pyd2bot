from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightFriendlyRequestedMessage(NetworkMessage):
    protocolId = 2157
    fightId:int
    sourceId:int
    targetId:int
    
