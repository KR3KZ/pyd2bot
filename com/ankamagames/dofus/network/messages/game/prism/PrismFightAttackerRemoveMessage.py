from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class PrismFightAttackerRemoveMessage(NetworkMessage):
    subAreaId:int
    fightId:int
    fighterToRemoveId:int
    
    
