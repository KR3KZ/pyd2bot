from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class GameActionFightCastOnTargetRequestMessage(INetworkMessage):
    protocolId = 8001
    spellId:int
    targetId:int
    
    
