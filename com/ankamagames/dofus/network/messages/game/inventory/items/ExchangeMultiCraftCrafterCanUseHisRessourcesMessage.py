from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeMultiCraftCrafterCanUseHisRessourcesMessage(NetworkMessage):
    protocolId = 264
    allowed:bool
    
    
