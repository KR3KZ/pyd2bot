from com.ankamagames.jerakine.network.INetworkMessage import INetworkMessage


class ExchangeSetCraftRecipeMessage(INetworkMessage):
    protocolId = 1333
    objectGID:int
    
    
