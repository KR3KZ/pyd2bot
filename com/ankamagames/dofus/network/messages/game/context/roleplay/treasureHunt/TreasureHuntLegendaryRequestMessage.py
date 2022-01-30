from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class TreasureHuntLegendaryRequestMessage(NetworkMessage):
    protocolId = 6283
    legendaryId:int
    
