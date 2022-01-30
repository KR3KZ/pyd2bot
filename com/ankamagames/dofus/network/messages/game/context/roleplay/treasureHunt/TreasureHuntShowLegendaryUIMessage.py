from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TreasureHuntShowLegendaryUIMessage(INetworkMessage):
    protocolId = 117
    availableLegendaryIds:int
    
    
