from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TreasureHuntLegendaryRequestMessage(INetworkMessage):
    protocolId = 6283
    legendaryId:int
    
    
