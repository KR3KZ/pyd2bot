from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class AreaFightModificatorUpdateMessage(INetworkMessage):
    protocolId = 4779
    spellPairId:int
    
    
