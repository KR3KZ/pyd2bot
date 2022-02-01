from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class TreasureHuntShowLegendaryUIMessage(INetworkMessage):
    protocolId = 117
    availableLegendaryIds:int
    
    
