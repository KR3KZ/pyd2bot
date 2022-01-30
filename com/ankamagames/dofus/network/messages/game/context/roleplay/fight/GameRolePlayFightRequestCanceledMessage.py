from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayFightRequestCanceledMessage(NetworkMessage):
    protocolId = 4478
    fightId:int
    sourceId:float
    targetId:float
    
