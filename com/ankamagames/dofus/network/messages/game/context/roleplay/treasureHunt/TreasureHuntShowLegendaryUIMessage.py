from com.ankamagames.jerakine.network.NetworkMessage import NetworkMessage


class TreasureHuntShowLegendaryUIMessage(NetworkMessage):
    availableLegendaryIds:list[int]
    
    
