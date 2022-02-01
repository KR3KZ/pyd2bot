from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PrismFightDefenderLeaveMessage(INetworkMessage):
    protocolId = 9481
    subAreaId:int
    fightId:int
    fighterToRemoveId:int
    
    
