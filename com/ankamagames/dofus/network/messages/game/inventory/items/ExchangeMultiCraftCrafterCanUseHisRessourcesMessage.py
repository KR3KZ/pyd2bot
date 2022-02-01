from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeMultiCraftCrafterCanUseHisRessourcesMessage(INetworkMessage):
    protocolId = 264
    allowed:bool
    
    
