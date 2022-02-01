from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class PrismFightAttackerRemoveMessage(INetworkMessage):
    protocolId = 300
    subAreaId:int
    fightId:int
    fighterToRemoveId:int
    
    
