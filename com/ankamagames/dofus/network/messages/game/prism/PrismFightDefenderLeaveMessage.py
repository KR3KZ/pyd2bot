from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismFightDefenderLeaveMessage(NetworkMessage):
    subAreaId:int
    fightId:int
    fighterToRemoveId:int
    
    
