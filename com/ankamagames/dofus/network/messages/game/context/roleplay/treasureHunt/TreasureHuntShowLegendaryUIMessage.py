from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntShowLegendaryUIMessage(NetworkMessage):
    protocolId = 117
    availableLegendaryIds:int
    
