from com.ankamagames.dofus.network.messages.NetworkMessage import NetworkMessage


class ExchangeMultiCraftSetCrafterCanUseHisRessourcesMessage(NetworkMessage):
    protocolId = 4258
    allow:bool
    
