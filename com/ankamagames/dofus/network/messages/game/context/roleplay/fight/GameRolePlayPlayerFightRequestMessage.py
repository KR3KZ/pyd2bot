from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightRequestMessage(NetworkMessage):
    protocolId = 6364
    targetId:float
    targetCellId:int
    friendly:bool
    
