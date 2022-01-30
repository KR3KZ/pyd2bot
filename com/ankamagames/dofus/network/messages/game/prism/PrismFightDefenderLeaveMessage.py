from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class PrismFightDefenderLeaveMessage(INetworkMessage):
    protocolId = 9481
    subAreaId:int
    fightId:int
    fighterToRemoveId:int
    
    
