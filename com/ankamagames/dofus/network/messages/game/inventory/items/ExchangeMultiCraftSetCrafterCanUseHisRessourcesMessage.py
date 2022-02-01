from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeMultiCraftSetCrafterCanUseHisRessourcesMessage(INetworkMessage):
    protocolId = 4258
    allow:bool
    
    
