from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class PrismFightDefenderLeaveMessage(NetworkMessage):
    protocolId = 9481
    subAreaId:int
    fightId:int
    fighterToRemoveId:float
    
