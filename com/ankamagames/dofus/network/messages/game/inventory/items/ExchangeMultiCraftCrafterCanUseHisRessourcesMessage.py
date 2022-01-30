from com.ankamagames.dofus.network.messages.INetworkMessage import INetworkMessage


class ExchangeMultiCraftCrafterCanUseHisRessourcesMessage(INetworkMessage):
    protocolId = 264
    allowed:bool
    
    
