from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameActionFightCastRequestMessage(INetworkMessage):
    protocolId = 4946
    spellId:int
    cellId:int
    
    
