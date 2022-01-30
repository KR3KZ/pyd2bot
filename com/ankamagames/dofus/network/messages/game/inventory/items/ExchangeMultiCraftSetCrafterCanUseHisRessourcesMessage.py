from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeMultiCraftSetCrafterCanUseHisRessourcesMessage(INetworkMessage):
    protocolId = 4258
    allow:bool
    
    
