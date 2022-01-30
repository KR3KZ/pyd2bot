from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeCrafterJobLevelupMessage(NetworkMessage):
    protocolId = 6591
    crafterJobLevel:int
    
