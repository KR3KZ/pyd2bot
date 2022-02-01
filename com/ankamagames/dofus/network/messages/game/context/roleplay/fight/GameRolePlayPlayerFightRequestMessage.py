from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class GameRolePlayPlayerFightRequestMessage(NetworkMessage):
    targetId:int
    targetCellId:int
    friendly:bool
    
    
