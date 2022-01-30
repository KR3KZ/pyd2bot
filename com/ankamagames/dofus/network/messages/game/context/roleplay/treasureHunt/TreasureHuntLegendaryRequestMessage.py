from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class TreasureHuntLegendaryRequestMessage(INetworkMessage):
    protocolId = 6283
    legendaryId:int
    
    
