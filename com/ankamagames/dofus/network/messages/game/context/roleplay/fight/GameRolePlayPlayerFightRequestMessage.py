from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightRequestMessage(NetworkMessage):
    protocolId = 6364
    targetId:int
    targetCellId:int
    friendly:bool
    
    
